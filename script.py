import os
import sys
import shutil

os.chdir(os.getcwd())
sources = ["py-project.py", "py-project.bat"]
destination = os.path.dirname(sys.executable)  # Executable de python
print(destination)
for source in sources:
    shutil.copy(source, destination)
