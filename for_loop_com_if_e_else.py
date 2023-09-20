
#Compra online com 3 tentativas
compra_confirmada = True
valor = input('Quanto você está disposto a pagar nesta compra?')
dados_compra = f'Compra confirmada no valor de R${valor}.'

for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    
  else:
    print('Falha na compra!')