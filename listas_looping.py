
valores = [10, 20, 30, 40, 50]
print(f'O valor final do produto na lista é de: ')

for x in valores:
  print(f'R${x}.')

cores = ['branco', 'azul', 'verde', 'preto', 'vermelho']
print(f'As cores disponíveis em estoque são: ')
for cor in cores:
  print(f': {cor}')

cor_cliente = input('Digite a cor desejada: ')

if cor_cliente.lower() in cores:
  print('Tinta consta em estoque.')
else:
  print('Não temos esta cor em estoque.')