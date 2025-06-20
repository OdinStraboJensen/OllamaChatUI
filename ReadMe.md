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

## Verify Installation

Open **PowerShell** or **Command Prompt** and run:

```bash
ollama --version

You should see something like "ollama version 0.x.x"

## Download and run llama3.1

```bash
ollama pull llama3
ollama run llama3
