# ASTRAM
## A Local AI Agent with Full System Access

Astram is a powerful local AI agent built with FastAPI and DeepSeek Coder and llama models, capable of executing commands directly on your system. It features a robust memory system, tool integration, and a user-friendly web interface.

## Features

- **Full System Access**: Execute commands directly on your system with full permissions
- **Memory System**: Maintains conversation history and context
- **Tool Integration**: Built-in tools for file operations and command execution
- **Web Interface**: User-friendly chat interface for seamless interaction
- **Local Execution**: Runs entirely locally with no external dependencies

## File tree structure
```
├── 📁 app
│   ├── 📁 core
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 agent.py
│   │   ├── 🐍 llm.py
│   │   ├── 🐍 memory.py
│   │   └── 🐍 tools.py
│   ├── 🐍 __init__.py
│   └── 🐍 main.py
├── 📁 frontend
│   ├── 📁 src
│   │   ├── 📄 App.jsx
│   │   ├── 🎨 index.css
│   │   └── 📄 main.jsx
│   ├── 🌐 index.html
│   ├── ⚙️ package.json
│   ├── 📄 postcss.config.js
│   ├── 📄 tailwind.config.js
│   └── 📄 vite.config.js
├── ⚙️ .gitignore
├── 🐍 config.py
├── ⚙️ memory.json
├── 📄 requirements.txt
├── 🐍 run.py
├── 🐍 test_agent.py
└── 🐍 verification.py
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
python run.py
```

4. Open the web interface:
```
http://localhost:5000
```

## Usage

### Chat Interface

Open the web interface at `http://localhost:5000` and start chatting with Astram. You can ask it to perform various tasks, such as:

- Create files and directories
- Read and write file contents
- Execute commands
- And much more!

### API

Astram exposes a REST API for easy integration with other applications. The API is available at `http://localhost:5000/api`.

#### Endpoints

- `POST /chat`: Send a message to the agent

## Tools

Astram comes with the following built-in tools:

| Tool | Description |
|------|-------------|
| `read_file` | Read the contents of a file |
| `write_file` | Write content to a file |
| `list_files` | List files in a directory |
| `run_command` | Execute a system command |

## Configuration

Astram uses the following configuration:

- **Ollama Base URL**: `http://localhost:11434`
- **Coding Model Name**: `deepseek-coder:6.7b`
- **General Model Name**: `llama3`
- **Memory File**: `memory.json`
