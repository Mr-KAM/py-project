import os
import sys
import shutil

os.chdir(os.getcwd())
sources = ["py-project.py", "py-project.bat"]
destination = os.path.dirname(sys.executable)  # Executable de python
print(f"Destination python {destination}")
to_add=f"python {destination}/py-project.py"
file=open("py-project.bat","w")
file.write(to_add)
file.close()
print(to_add)
for source in sources:
    shutil.copy(source, destination)
