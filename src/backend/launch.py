import os
import subprocess
import sys

def main():
    # Pfad zur Streamlit-Datei
    app_path = os.path.join("src", "frontend", "st", "main.py")

    # Streamlit-Kommando
    cmd = [
        "streamlit", "run", app_path,
        "--server.address=0.0.0.0",
        "--server.port=8501"
    ]

    # Environment (wichtig, damit Backend importierbar ist)
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath("src")

    subprocess.run(cmd, env=env)

if __name__ == "__main__":
    sys.exit(main())