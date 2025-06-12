#!/usr/bin/env python3
"""
Simple HTTP server with CORS headers for the RAG demo.
Run with: python3 serve.py [port]
"""

import http.server
import socketserver
from http.server import SimpleHTTPRequestHandler
import sys
import os
import webbrowser
from urllib.parse import urlparse

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        # Suppress default logging for cleaner output
        return

def find_available_port(start_port=8000):
    """Find an available port starting from start_port"""
    import socket
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return None

def main():
    # Parse command line arguments
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print("Error: Port must be a number")
            sys.exit(1)
    else:
        PORT = find_available_port(8000)
        if PORT is None:
            print("Error: No available ports found in range 8000-8099")
            sys.exit(1)

    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("Error: index.html not found in current directory")
        print("Make sure you're running this script from the project directory")
        sys.exit(1)

    try:
        with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
            url = f"http://localhost:{PORT}/"
            print(f"🚀 Server running at {url}")
            print(f"📄 Demo available at {url}")
            print("🔧 Make sure Ollama is running with: OLLAMA_ORIGINS=* ollama serve")
            print("⏹️  Press Ctrl+C to stop the server")
            
            # Try to open browser automatically
            try:
                webbrowser.open(url)
                print("🌐 Opening browser...")
            except:
                pass
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✅ Server stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"❌ Port {PORT} is already in use.")
            print(f"Try: python3 serve.py {PORT + 1}")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()