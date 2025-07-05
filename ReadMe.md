# Ollama Chat UI

A simple browser-based chat UI that connects to [Ollama](https://ollama.com) running locally on your Windows machine.  
Supports LLaMA 3.1, syntax-highlighted code, Markdown formatting, and shows a “thinking...” indicator while waiting for responses.

---

## How to Install Ollama on Windows

### 1. Download and Install
- Go to: [https://ollama.com/download](https://ollama.com/download)
- Click **Download for Windows** and run the installer

> The installer sets up WSL2 and background services automatically.

### 2. Restart Your PC (important)

---

## How to Install Python to run the webserver

- Run this link: [https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe](Python)
- Run installer.
- **Make sure to include python in path for the webserver.bat to work** (If you're on OS X or Linux, I'm sure you know how to get it 😉)

## Verify Installation

Open **PowerShell** or **Command Prompt** and run:

```bash
ollama --version
```

You should see something like 
```bash
ollama version 0.x.x"
```

## Download and run llama3.1

```bash
ollama pull llama3
ollama run llama3
```

## Use the included source code examples

- Run webserver.bat (or on other platforms just execute the line within)
- In your browser go to http://localhost:8000 and click the appropriate file
- **Note: Only sample 4 and 5 actually work for querying the models**
