import os
from pydub import AudioSegment

AudioSegment.converter = r'C:\\ffmpeg\\bin\\ffmpeg.exe'
mp3_files = os.listdir("D:\\repertorio\\popNacional\\zzarquivos_copiados\\")


# Duração desejada para cada arquivo (em milissegundos)
duration = 20 * 1000

for file in mp3_files:

    audio = AudioSegment.from_mp3(file)
    audio = audio[:duration]
    audio.export(file, format="mp3")
    print(f"Arquivo {file} editado com sucesso.")