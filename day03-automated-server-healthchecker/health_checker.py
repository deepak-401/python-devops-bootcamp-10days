import psutil

def check_cpu(threshold=80):
    cpu = psutil.cpu_percent(interval=1)
    if cpu > threshold:
        print(f"⚠️ High CPU Usage: {cpu}%")
    else:
        print(f"✅ CPU Usage: {cpu}%")

def check_memory(threshold=80):
    memory = psutil.virtual_memory()
    if memory.percent > threshold:
        print(f"⚠️ High Memory Usage: {memory.percent}%")
    else:
        print(f"✅ Memory Usage: {memory.percent}%")

def check_disk(threshold=80):
    disk = psutil.disk_usage('/')
    if disk.percent > threshold:
        print(f"⚠️ High Disk Usage: {disk.percent}%")
    else:
        print(f"✅ Disk Usage: {disk.percent}%")

if __name__ == "__main__":
    print("Running Server Health Checks...\n")
    check_cpu()
    check_memory()
    check_disk()

