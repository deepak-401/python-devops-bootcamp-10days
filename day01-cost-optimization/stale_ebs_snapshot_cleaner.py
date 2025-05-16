import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Fetch all EBS snapshots owned by self
    logger.info("Fetching all EBS snapshots...")
    response = ec2.describe_snapshots(OwnerIds=['self'])
    snapshots = response.get('Snapshots', [])
    logger.info(f"Found {len(snapshots)} snapshots.")

    # Fetch all running and stopped EC2 instance IDs
    logger.info("Fetching all active EC2 instances (running + stopped)...")
    instances_response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}]
    )

    active_instance_ids = set()
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])
    logger.info(f"Active EC2 instances: {active_instance_ids}")

    # Process each snapshot
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        # Optional: skip if tag 'Keep=true' is present
        tags = {tag['Key']: tag['Value'] for tag in snapshot.get('Tags', [])}
        if tags.get('Keep', '').lower() == 'true':
            logger.info(f"Skipping snapshot {snapshot_id} (tagged to keep).")
            continue

        logger.info(f"Checking snapshot: {snapshot_id}, Volume ID: {volume_id}")

        if not volume_id:
            # Delete snapshot if no volume ID
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                logger.info(f"Deleted snapshot {snapshot_id} (no volume associated).")
            except Exception as e:
                logger.error(f"Failed to delete snapshot {snapshot_id}: {str(e)}")
        else:
            # Check if the volume exists and is attached
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                attachments = volume_response['Volumes'][0].get('Attachments', [])

                if not attachments:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    logger.info(f"Deleted snapshot {snapshot_id} (volume not attached).")
                else:
                    logger.info(f"Snapshot {snapshot_id} kept (volume still attached).")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # Delete snapshot if volume is deleted
                    try:
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        logger.info(f"Deleted snapshot {snapshot_id} (volume not found).")
                    except Exception as e:
                        logger.error(f"Failed to delete snapshot {snapshot_id}: {str(e)}")
                else:
                    logger.error(f"Unexpected error for snapshot {snapshot_id}: {str(e)}")

