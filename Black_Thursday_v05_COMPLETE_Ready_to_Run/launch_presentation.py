"""Start Black Thursday's local HTTP presentation + Python simulation.

This launcher must live next to Project-Black-Thursday-deliverable/.
The course package's *selective update* is not a standalone project.
"""
from pathlib import Path
import runpy
import socket
import sys
import threading
import time
import webbrowser

BASE = Path(__file__).resolve().parent
REPO_DIR = BASE / "Project-Black-Thursday-deliverable"
SERVER = REPO_DIR / "python" / "app.py"
ADDRESS = ("127.0.0.1", 8000)
URL = "http://127.0.0.1:8000/"


def main():
    if not SERVER.is_file():
        print("\nERROR: The Python server file is missing:", file=sys.stderr)
        print(f"  {SERVER}", file=sys.stderr)
        print("\nThis usually means you extracted ONLY the selective-update ZIP.", file=sys.stderr)
        print("Use the COMPLETE Ready-to-Run ZIP instead, or merge the", file=sys.stderr)
        print("selective update into your existing complete project repository.", file=sys.stderr)
        return 2

    try:
        with socket.create_connection(ADDRESS, timeout=0.5):
            print("\nPort 8000 is already in use.", file=sys.stderr)
            print("If Black Thursday is already running, open:", URL, file=sys.stderr)
            print("Otherwise close the program using port 8000 and try again.", file=sys.stderr)
            return 3
    except OSError:
        pass

    print("Black Thursday | group polsci01 | Interactive mode", flush=True)
    print(f"Source: {REPO_DIR}", flush=True)
    print(f"Browser: {URL}", flush=True)
    print("Leave this window open; press Ctrl+C to stop the server.\n", flush=True)

    def open_later():
        time.sleep(1.7)
        webbrowser.open(URL)

    threading.Thread(target=open_later, daemon=True).start()
    try:
        runpy.run_path(str(SERVER), run_name="__main__")
    except OSError as ex:
        print(f"Failed to start Python server: {ex}", file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
