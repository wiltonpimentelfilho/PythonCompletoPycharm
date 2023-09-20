# While - Excelente para loops dependentes de uma condição.

valor_produto = float(100.00)
dia = 0

while valor_produto > 20.00:
  dia += 1
  print(f'No dia {dia}, o valor do produto é igual a R${valor_produto}. ')
  valor_produto -= 5