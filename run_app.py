import subprocess
import time
import os
import sys

def main():
    print("🚀 Starting Ollama Test Generator System...")

    # 1. Start Backend
    print("🔹 Launching Backend (FastAPI on Port 8000)...")
    backend = subprocess.Popen([sys.executable, "app/main.py"], cwd=os.getcwd())

    # 2. Start Frontend
    print("🔹 Launching Frontend (HTTP Server on Port 3000)...")
    # We need to change dir to frontend for http.server to serve from root of frontend
    frontend_cmd = [sys.executable, "-m", "http.server", "3000"]
    frontend = subprocess.Popen(frontend_cmd, cwd=os.path.join(os.getcwd(), "frontend"))

    print("\n✅ System is RUNNING!")
    print("👉 Open your browser to: http://localhost:3000")
    print("-------------------------------------------------")
    print("Press Ctrl+C to stop servers.")

    try:
        while True:
            time.sleep(1)
            # Check if processes are still alive
            if backend.poll() is not None:
                print("❌ Backend process died!")
                break
            if frontend.poll() is not None:
                print("❌ Frontend process died!")
                break
    except KeyboardInterrupt:
        print("\nStopping servers...")
        backend.terminate()
        frontend.terminate()
        print("Goodbye!")

if __name__ == "__main__":
    main()
