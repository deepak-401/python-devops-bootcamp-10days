import docker

client = docker.from_env()

def auto_restart_containers():
    containers = client.containers.list(all=True)
    for container in containers:
        status = container.status
        name = container.name

        if status == 'exited':
            print(f"í´ Restarting exited container: {name}")
            container.restart()
        elif status == 'running':
            # Check health status if defined
            container_info = client.api.inspect_container(container.id)
            health_status = container_info.get("State", {}).get("Health", {}).get("Status")
            if health_status == 'unhealthy':
                print(f"íº‘ Restarting unhealthy container: {name}")
                container.restart()

if __name__ == "__main__":
    print("í´ Checking Docker containers for restart...")
    auto_restart_containers()

