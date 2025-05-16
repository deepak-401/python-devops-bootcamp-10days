## ��� Day 1 – AWS Cloud Cost Optimization: Stale EBS Snapshot Deletion

### ��� Project: EBS Snapshot Cleanup using Lambda

**Description:**  
This Python-based AWS Lambda function identifies and deletes stale EBS snapshots that are no longer associated with any active EC2 volumes. It helps reduce unnecessary storage costs.

### ���️ Key Features:
- Scheduled using **EventBridge** (cron: `0 1 ? * SUN *`)
- Logs actions to **CloudWatch Logs**
- Uses `boto3` to:
  - List all snapshots
  - Identify snapshots with missing or unattached volumes
  - Delete stale snapshots

### ��� Architecture:
- **EventBridge** → triggers → **Lambda Function**
- **Lambda** uses **EC2 APIs** and logs to **CloudWatch Logs**

### ��� AWS Services Used:
- AWS Lambda
- Amazon EC2 (Snapshots & Volumes)
- Amazon EventBridge
- Amazon CloudWatch Logs
- IAM Roles (for access control)

### ��� Cost Estimate:
- Lambda + EventBridge + CloudWatch Logs ≈ **$0.01 – $0.03/month**
- Deletion of stale snapshots can save **$0.05 per GB/month**

> This solution is lightweight and stays within the AWS Free Tier for most users.

