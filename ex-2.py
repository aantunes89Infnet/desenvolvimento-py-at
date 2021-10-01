import os

file = input("Digite o nomedo arquivo: ")
# windows
# openFile = f"notepad.exe {file}.txt"
# os.system(openFile)

# mac
import subprocess
subprocess.call(['open', '-a', 'TextEdit', f"{file}.txt"])