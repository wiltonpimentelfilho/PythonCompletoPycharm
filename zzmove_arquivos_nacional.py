# -*- coding: utf-8 -*-
import os
import shutil

#subpastas = os.listdir('D:\\repertorio\\popnacional\\')
subpastas = os.listdir(os.path.abspath('D:\\repertorio\\popnacional\\'))

for subpasta in subpastas:
    arquivos = os.listdir('D:\\repertorio\\popnacional\\'+subpasta)
    for arquivo in arquivos:
        if arquivo.endswith(".mp3"):
            if not os.path.exists('D:\\repertorio\\popnacional\\zzarquivos_copiados'):
                os.mkdir('D:\\repertorio\\popnacional\\zzarquivos_copiados')
            if os.path.exists('D:\\repertorio\\popnacional\\zzarquivos_copiados\\'+arquivo):
                pass
            else:
                shutil.copy('D:\\repertorio\\popnacional\\'+subpasta+'\\'+arquivo, 'D:\\repertorio\\popnacional\\zzarquivos_copiados\\')
                print("Arquivos copiados com sucesso!")