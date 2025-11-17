import os
import subprocess
import sys
from pathlib import Path

# def main():
#     # Pfad zur Streamlit-Datei
#     app_path = os.path.join("src", "frontend", "st", "Start.py")

#     # Streamlit-Kommando
#     cmd = [
#         "streamlit", "run", app_path,
#         "--server.address=0.0.0.0",
#         "--server.port=8501"
#     ]

#     # Environment (wichtig, damit Backend importierbar ist)
#     env = os.environ.copy()
#     env["PYTHONPATH"] = os.path.abspath("src")

#     subprocess.run(cmd, env=env)

# if __name__ == "__main__":
#     sys.exit(main())



def main():
    # Basis: Ordnerstruktur ausgehend von dieser Datei
    # launch.py liegt in: src/backend/launch.py
    backend_dir = Path(__file__).resolve().parent        # .../src/backend
    src_dir = backend_dir.parent                         # .../src

    # Pfad zur Streamlit-Datei (Start.py)
    app_path = src_dir / "frontend" / "st" / "Start.py"

    # Streamlit-Kommando
    cmd = [
        "streamlit", "run", str(app_path),
        "--server.address=0.0.0.0",
        "--server.port=8501",
    ]

    # Environment (wichtig, damit backend importierbar ist)
    env = os.environ.copy()
    # src in PYTHONPATH hängen
    env["PYTHONPATH"] = str(src_dir) + os.pathsep + env.get("PYTHONPATH", "")

    # optional: auch im aktuellen Prozess sichtbar machen
    sys.path.append(str(src_dir))

    subprocess.run(cmd, env=env)

if __name__ == "__main__":
    sys.exit(main())