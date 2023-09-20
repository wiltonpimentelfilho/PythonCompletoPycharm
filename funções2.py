# Função com vários argumentos (xargs)

# Somando vários números (sem definição de qtidade de nºs que serão somados)

def soma(*numeros): # O '*' indica que pode conter n parâmetros
  resultado = 0
  for num in numeros:
    resultado += num # Pega o resultado e soma com o 'num'
  return resultado

x = soma(1, 2, 3, 4, 5, 6, 7)
print(x)
  
