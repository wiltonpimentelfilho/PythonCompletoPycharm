# Função que recebe vários parâmetros e vários argumentos

def revenda(**carros):
  return carros

a = revenda(fabrica='Volks', marca='gol', cor='branco', ano='1999')
b = revenda(fabrica='Chevrolet', marca='Chevett', cor='preto', ano='2001')
c = revenda(fabrica='Ford', marca='Corcel', cor='Azul', ano='1976')

print(a)
print(b)
print(c)