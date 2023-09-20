renda_para_aprovacao = input('Entre com a renda mínima para aprovação: ')

renda_do_cliente = (input('Entre com o a renda do cliente: '))

if renda_do_cliente >= renda_para_aprovacao:
  print('Financiamento aprovado!')
else:
  print('Financiamento reprovado')

