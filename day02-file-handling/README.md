# � Day 2 – Log File Cleaner Script

## � Project: Automatic Old Log File Deletion

This Python script deletes log files older than a specified number of days from a given directory. It helps in cleaning up disk space and keeping log folders manageable.

### ✅ Features:
- Walks through all files in `/var/log`
- Deletes files older than 7 days
- Logs deleted files to the console
- Easily configurable

### � Concepts Covered:
- File handling
- `os` and `time` modules
- Directory traversal
- File age comparison

### ⚠️ Warning:
Run with caution and **never test directly on production log folders**.

> Tip: Test with a custom folder before using `/var/log`.

### �️ Run Command:
```bash
python3 log_cleaner.py

