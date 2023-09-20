'''
Criar um retângulo
'''
linhas = 6
colunas = 6
simbolo = '#'

for l in range(linhas):
  for c in range(colunas):
    print(simbolo, end='') # O end='', (end=' ') indica que o caractere final deve ser identificado por um espaço em branco e não por uma nova linha.
  print() #Equivale ao 'ENTER'