
# Listas
  # Armazenar mais de uma informação em variáveis
  # Manter a sequencia dos dados em uma variável

# Observe:
var = list('comprar')
print(var)

cores = ['branco', 'azul', 'amarelo', 'vermelho']
valores = [10, 20, 30, 40]

var2 = list(zip(cores, valores))
print(var2)

var3 = zip(valores, cores)
print(list(var3))