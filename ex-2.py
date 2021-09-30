import os

file = input("Digite o nomedo arquivo")
openFile = f"notepad.exe {file}.txt"
os.system(openFile)


# import subprocess
# subprocess.call(['open', '-a', 'TextEdit', file])