import os
import time

LOG_DIR = "/var/log"
DAYS_THRESHOLD = 7

def delete_old_logs(log_directory, days_threshold):
    now = time.time()
    for root, dirs, files in os.walk(log_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_age = now - os.path.getmtime(file_path)
                if file_age > (days_threshold * 86400):
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    delete_old_logs(LOG_DIR, DAYS_THRESHOLD)

