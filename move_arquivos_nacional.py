import os
import shutil

subpastas = os.listdir('D:\\repertorio\\popnacional\\')


for subpasta in subpastas:
    arquivos = os.listdir('D:\\repertorio\\popnacional\\'+subpasta)
    for arquivo in arquivos:
        shutil.copy('D:\\repertorio\\popnacional\\'+subpasta+'\\'+arquivo, 'D:\\repertorio\\popnacional\\zzarquivos_copiados\\')

print("Arquivos copiados com sucesso!")
