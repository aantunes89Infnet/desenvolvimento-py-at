import os

file = input("Digite o nomedo arquivo: ")
# windows
# abrindo teste.txt
# openFile = f"notepad.exe {file}.txt"
# os.system(openFile)

# mac
# abrindo teste.txt
import subprocess
subprocess.call(['open', '-a', 'TextEdit', f"{file}.txt"])