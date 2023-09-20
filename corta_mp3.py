# -*- coding: utf-8 -*-
import os
import shutil
from pydub import AudioSegment

AudioSegment.converter = r'C:\\ffmpeg\\bin\\ffmpeg.exe'

# Definir diretório atual
current_dir = os.getcwd()

# Listar todos os arquivos e subpastas
list_files = os.listdir(current_dir)

# Definir subpasta de destino
dest_dir = os.path.join(current_dir, 'arquivosOriginais')

# Criar subpasta de destino
if os.path.exists(dest_dir) == False:
    os.mkdir(dest_dir)

# Percorrer lista de arquivos
for file in list_files:
    # Verificar se é um arquivo mp3
    if file.endswith(".mp3"):
        # Abrir arquivo mp3
        song = AudioSegment.from_mp3(file)
        # Cortar arquivo mp3
        song = song[0:20000]
        # Copiar arquivo mp3 original para a subpasta
        shutil.copy2(file, dest_dir)
        # Salvar arquivo mp3 cortado
        song.export(file, format="mp3")
        print(f"Arquivo {file} editado com sucesso.")


