
import os
import re
import json
from datetime import datetime, timedelta

SENSITIVE_KEYWORDS = ['password', 'passwd', 'pin', 'secret', 'apikey']
BACKUP_EXTENSIONS = ['.bak', '.zip', '.copy', '.tar', '.gz']
SCAN_PATH = os.path.expanduser("~")  # Hemkatalog
REPORT_FILE = "backupscanner_report.json"

def is_sensitive_content(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read().lower()
            return any(keyword in content for keyword in SENSITIVE_KEYWORDS)
    except:
        return False

def is_old(file_path):
    try:
        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        return file_time < datetime.now() - timedelta(days=180)
    except:
        return False

def is_large(file_path):
    try:
        return os.path.getsize(file_path) > 10 * 1024 * 1024  # över 10 MB
    except:
        return False

def has_backup(file_path):
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    for ext in BACKUP_EXTENSIONS:
        if os.path.exists(os.path.join(dir_name, base_name + ext)):
            return True
    return False

def scan_directory(path):
    report = {"sensitive_files": [], "old_large_unbacked": []}
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            if file.endswith(('.txt', '.log', '.ini', '.cfg', '.json')):
                if is_sensitive_content(full_path):
                    report["sensitive_files"].append(full_path)
            if is_old(full_path) and is_large(full_path) and not has_backup(full_path):
                report["old_large_unbacked"].append(full_path)
    return report

def main():
    print(f"Scanning directory: {SCAN_PATH}")
    result = scan_directory(SCAN_PATH)
    print(f"Scan complete. Results written to {REPORT_FILE}")
    with open(REPORT_FILE, 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
