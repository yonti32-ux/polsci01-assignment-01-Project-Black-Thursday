"""Launch full Black Thursday presentation with Python simulation, one command.

Usage: python launch_presentation.py
No pip installation is necessary: python/app.py has a stdlib server fallback.
"""
from pathlib import Path
import runpy
import threading
import time
import webbrowser

ROOT = Path(__file__).resolve().parent
APP = ROOT / 'Project-Black-Thursday-deliverable' / 'python' / 'app.py'


def open_browser():
    # Give either Flask or the Python stdlib server a moment to bind.
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:8000/')


if __name__ == '__main__':
    if not APP.is_file():
        raise SystemExit(f'Cannot locate presentation Python server: {APP}')
    print('Black Thursday | group polsci01 | Interactive mode')
    print('Browser: http://127.0.0.1:8000/ | Press Ctrl+C to stop.')
    threading.Thread(target=open_browser, daemon=True).start()
    runpy.run_path(str(APP), run_name='__main__')
