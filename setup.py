# Import the required modules
from PyInstaller import __main__ as pyi

# Specify the script and options
script = "main.py"
options = [
    "--name=2D Runner",
    "--onefile",  # For a single executable file
    "--hidden-import=pygame",  # To handle 'pygame' as an external import
    "--add-data=images;images",  # Include image files
    "--add-data=sounds;sounds",  # Include sound files
    "--add-data=scores.txt;.",  # Include scores.txt in the root of the executable
]

# Build the executable using PyInstaller
pyi.run([script, *options])
