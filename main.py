# import os
# import eel

# eel.init("www")

# # Open Chrome in app mode on macOS
# os.system('open -a "Google Chrome" --args --app="http://localhost:8000/index.html"')

# eel.start('index.html', mode=None, host='localhost', block=True)
import subprocess
import eel

eel.init("www")

# Launch Chrome in app mode (macOS)
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
url = "http://localhost:8000/index.html"

try:
    subprocess.Popen([chrome_path, f'--app={url}'])
except FileNotFoundError:
    print("Chrome not found at expected path. Please check the path or install Chrome.")

eel.start('index.html', mode=None, host='localhost', block=True)

