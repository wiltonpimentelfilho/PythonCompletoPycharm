import os
import subprocess

path = "D:/repertorio/popNacional/14 Bis/"

arquivos = os.listdir(path)

file: str
for file in arquivos:
    subprocess.call(['ffmpeg', '-i', {path + file}, '-t', '00:00:20', '-c', 'copy', {path + file}])
    print(arquivos)
