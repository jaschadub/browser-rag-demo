# In-Browser RAG Demo

A browser-based Retrieval-Augmented Generation (RAG) demo that processes PDF and Excel files locally and queries them using Ollama.

## Features

- **Local File Processing**: Upload PDF or Excel files for text extraction
- **In-Browser Embeddings**: Uses Xenova/transformers for client-side text embeddings
- **Semantic Search**: Finds relevant document chunks using cosine similarity
- **Ollama Integration**: Sends context to local Ollama instance for question answering

## Prerequisites

1. **Python 3** (for local HTTP server)
2. **Ollama** installed and running
3. **Gemma3:12b model** (or modify the model name in the code)

## Setup Instructions

### 1. Install and Start Ollama

```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the required model
ollama pull gemma3:12b

# Start Ollama with CORS enabled
OLLAMA_ORIGINS=* ollama serve
```

### 2. Start the Local Server

```bash
# In the project directory
python3 serve.py
```

This starts a local HTTP server on port 8000 with CORS headers enabled.

### 3. Open the Demo

Navigate to: `http://localhost:8000/` (opens automatically)

## Usage

1. **Wait for Model Loading**: The embedding model (~23MB) downloads on first use
2. **Upload a File**: Choose a PDF or Excel file
3. **Ask Questions**: Type your question and click "Ask" or press Enter
4. **View Results**: The system finds relevant content and generates an answer

## Troubleshooting

### CORS Errors
- **Problem**: Browser blocks requests due to CORS policy
- **Solution**: Start Ollama with `OLLAMA_ORIGINS=* ollama serve`

### Model Loading Issues
- **Problem**: Transformers model fails to load
- **Solution**: Ensure you're accessing via HTTP (not file://) and have internet connection

### Ollama Connection Failed
- **Problem**: Cannot connect to Ollama API
- **Solutions**:
  - Check Ollama is running: `ollama list`
  - Verify model availability: `ollama pull gemma3:12b`
  - Ensure CORS is enabled: `OLLAMA_ORIGINS=* ollama serve`

### File Processing Errors
- **Problem**: PDF or Excel files fail to process
- **Solutions**:
  - Ensure file is not corrupted
  - Try smaller files first
  - Check browser console for detailed errors

## Technical Details

- **Frontend**: Vanilla JavaScript with ES6 modules
- **Embeddings**: Xenova/all-MiniLM-L6-v2 (runs in browser)
- **File Processing**: PDF.js for PDFs, SheetJS for Excel
- **LLM**: Ollama API (local)
- **Styling**: Tailwind CSS (CDN)

## File Structure

```
├── index.html          # Main demo page
├── serve.py            # Local HTTP server with CORS
└── README.md           # This file
```

## Security Notes

- This demo uses CDN resources for simplicity
- For production use, download and serve assets locally
- The demo processes files entirely in the browser (no server upload)
- Ollama runs locally, so your data stays on your machine