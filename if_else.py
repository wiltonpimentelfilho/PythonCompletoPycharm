
veloc_max = 110
veloc_min = 80

veloc_atual = int(input('Entre com a velocidade atual: '))


if veloc_atual > veloc_max:
  print('Você está acima da velocidade máxima permitida!')
  print('Reduza a velocidade!')

elif (veloc_atual < veloc_min):
  print('Você não pode dirigir abaixo de 80Km/H nesta via.')

else:
  print('Velocidade Ok!')
60

########################################
#valor permitido para venda deve estar entre R$20 e 39.99
valor_produto = float(input('Entre com o preço do produto: '))

if 20 <= valor_produto < 40:
  print('Produto aceito!')
else:
  print('Produto com preço não permitido.')


