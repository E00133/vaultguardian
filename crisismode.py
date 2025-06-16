
import os
import platform
import time
import shutil
import getpass
from datetime import datetime

LOG_FILE = "crisismode_log.txt"

def write_log(message):
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now().isoformat()}] {message}\n")

def clear_downloads():
    path = os.path.join(os.path.expanduser("~"), "Downloads")
    if os.path.exists(path):
        for file in os.listdir(path):
            try:
                full_path = os.path.join(path, file)
                if os.path.isfile(full_path):
                    os.remove(full_path)
                    write_log(f"Removed: {full_path}")
            except:
                write_log(f"Failed to remove: {full_path}")

def kill_discord_slack_telegram():
    targets = ['discord', 'slack', 'telegram']
    for t in targets:
        os.system(f"pkill -f {t}")
        write_log(f"Attempted to kill process: {t}")

def logout_user():
    write_log("Attempting logout...")
    if platform.system() == "Linux":
        os.system("gnome-session-quit --no-prompt || pkill -KILL -u $USER")
    elif platform.system() == "Darwin":
        os.system("osascript -e 'tell application "System Events" to log out'")
    elif platform.system() == "Windows":
        os.system("shutdown -l")
    write_log("Logout command issued")

def crisis_mode():
    print("⚠️  CRISIS MODE ENGAGED ⚠️")
    write_log("CrisisMode™ Activated by user.")
    clear_downloads()
    kill_discord_slack_telegram()
    logout_user()

if __name__ == "__main__":
    confirm = input("This will clear traces and log you out. Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        crisis_mode()
    else:
        print("CrisisMode™ aborted.")
