import os
import shutil

subpastas = os.listdir('D:\\repertorio\\popInternacional\\')

for subpasta in subpastas:
    arquivos = os.listdir('D:\\repertorio\\popInternacional\\'+subpasta)
    for arquivo in arquivos:
        shutil.copy('D:\\repertorio\\popInternacional\\'+subpasta+'\\' +arquivo, 'D:\\repertorio\\popInternacional\\zarquivos_copiados\\')

print("Arquivos copiados com sucesso!")