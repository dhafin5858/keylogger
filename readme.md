# 🔐 Keylogger Project

A **Python-based keylogger** developed for **educational and research** purposes only. This tool captures keystrokes on a Windows machine and securely transfers the logs to a Kali Linux system using **SSH/SCP**.

---

## ✨ Features

- ✅ Logs all keystrokes to `keystrokes.log`
- 🚀 Automatically transfers the log to a Kali Linux host every 10 seconds
- 🛡️ Runs silently in the background (no visible console)
- 🧵 Multi-threaded design for smooth performance

---

## ⚙️ Prerequisites

### 🔸 On Windows

- [Python 3.x](https://www.python.org/downloads/)
- Required libraries (install with `pip`):
  ```bash
   pynput paramiko
🔸 On Kali Linux
SSH Server must be active:

`sudo apt install openssh-server`

🚀 Setup Instructions
Clone the repository

`git clone https://github.com/dhafin5858/keylogger.git`

`cd keylogger`

Configure connection settings

Edit keylogger_service.pyw and update these variables:

`kali_ip = "192.168.18.150"  # Your Kali Linux or VPS IP`

`username = "kali"           # Your SSH username`

`password = "kali"           # Your SSH password`

Install requirements

`pip install -r requirements.txt`

🛑 Stopping the Keylogger

To terminate the keylogger, open Task Manager and manually end the python.exe process.

📌 How It Works
🔤 Keystroke Logging
Captures all keyboard input and appends it to a file named keystrokes.log.

📤 Periodic Log Transfer
Every 10 seconds, the file is securely transferred to the Kali Linux host using SCP over SSH.

🕶 Background Execution
When run with pythonw, the script executes silently (without opening a console window), making it ideal for automated testing or stealthy demonstrations.

📄 License
Licensed under the MIT License. See the LICENSE file for more details.

⚠️ Disclaimer
This project is intended for ethical and educational use only.
Do not deploy this tool without the explicit consent of all parties involved.
Misuse can result in severe legal consequences.
