prod = float(input('Entre com o valor do produto em R$: '))

while prod > 0:
  prod = (prod * 0.20) + prod
  print(f'O valor final do seu produto sera de R${prod}.')
  break