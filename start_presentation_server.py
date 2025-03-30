import http.server
import socketserver
import webbrowser
import os
import threading
import time

# Configuration
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PRESENTATION_FILE = "Accountants_Big_Data_AI_Solution_Presentation.html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        # Customize logging to be more user-friendly
        if "200" in args[0]:  # Only log successful requests
            print(f"Serving: {self.path}")

def open_browser():
    # Wait a moment for the server to start
    time.sleep(1)
    # Open the presentation in the default browser
    url = f"http://localhost:{PORT}/{PRESENTATION_FILE}"
    print(f"\nOpening presentation in browser: {url}")
    webbrowser.open(url)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n{'='*60}")
        print(f"Presentation server running at http://localhost:{PORT}")
        print(f"To view the presentation, open a browser and go to:")
        print(f"http://localhost:{PORT}/{PRESENTATION_FILE}")
        print(f"\nTo access from other devices on your network, use your IP address:")
        print(f"http://YOUR_IP_ADDRESS:{PORT}/{PRESENTATION_FILE}")
        print(f"\nPress Ctrl+C to stop the server")
        print(f"{'='*60}\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server...")
            httpd.shutdown()

if __name__ == "__main__":
    # Start browser in a separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Start the server
    start_server()
