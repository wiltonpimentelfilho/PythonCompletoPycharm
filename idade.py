
def sub(x, y):
  return x - y

ano_nasc = int(input('Entre com o ano do seu nascimento: '))
# print(type(ano_nasc))
ano_atual = int(input('Entre com o ano atual: '))
# print(type(ano_atual))

print("Você já tem ou fará  " + str(sub(ano_atual,ano_nasc)) + " anos em " + str(ano_atual)+'.')