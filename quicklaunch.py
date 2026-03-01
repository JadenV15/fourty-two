import webbrowser
import subprocess
import platform
from pathlib import Path

basedir = str(Path(__file__).resolve().parent)

sinfo = None
if platform.system().lower() == 'windows':
    sinfo = subprocess.STARTUPINFO()
    sinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
CREATE_NO_WINDOW = 0x08000000

subprocess.Popen(['flask', 'run', '--debug'], startupinfo=sinfo, creationflags=CREATE_NO_WINDOW, cwd=basedir)
webbrowser.open(r'http://127.0.0.1:5000/')