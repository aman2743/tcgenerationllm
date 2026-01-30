# Ollama Test Generator

A local LLM-powered test case generator using Ollama (Llama 3.2) with a premium web interface.

## Features

- 🤖 **Local LLM**: Uses Ollama (Llama 3.2) for test case generation
- 🎨 **Premium UI**: Glassmorphism design with dark mode
- ⚡ **Real-time Streaming**: See test cases generated in real-time
- 📋 **Structured Output**: Test cases with ID, Description, Steps, and Expected Results

## Tech Stack

- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Backend**: Python FastAPI
- **AI**: Ollama (Llama 3.2)

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- Llama 3.2 model pulled (`ollama pull llama3.2`)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd AITesterBlueprintNew
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Ollama is running:
```bash
ollama serve
```

4. Verify Ollama connection:
```bash
python tools/check_ollama.py
```

## Usage

1. Start the application:
```bash
python run_app.py
```

2. Open your browser to: `http://localhost:3000`

3. Paste your code or requirements and click "Generate"

## Project Structure

```
AITesterBlueprintNew/
├── app/
│   └── main.py              # FastAPI backend
├── frontend/
│   ├── index.html           # Main UI
│   ├── css/
│   │   └── style.css        # Glassmorphism styling
│   └── js/
│       └── app.js           # Frontend logic
├── architecture/
│   └── generation_sop.md    # Technical SOP
├── tools/
│   └── check_ollama.py      # Ollama health check
├── requirements.txt         # Python dependencies
└── run_app.py              # Launcher script
```

## Architecture

Built using the **B.L.A.S.T.** protocol:
- **Blueprint**: Defined requirements and data schema
- **Link**: Verified Ollama connectivity
- **Architect**: 3-layer architecture (Frontend → API → LLM)
- **Stylize**: Premium UI/UX design
- **Trigger**: Ready for deployment

## License

MIT
