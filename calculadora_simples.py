
#Calculadora simples

#Esta função adiciona dois números
def add(x, y):
  return x + y

#Esta função subtrai dois números
def sub(x, y):
  return x - y 

#Esta função multiplica dois números
def mult(x, y):
  return x * y 

#Esta função divide dois números
def div(x, y):
  return x / y 

print("Selecione a operação desejada:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
  #Recebe a entrada do usuário:
  choice = input("Digite o número da operação: ")

  if choice in ('1', '2', '3', '4'):
    num1 = float(input("Entre com o primeiro número: "))
    num2 = float(input("Entre com o segundo número: "))

    if choice == '1':
      print('O resultado é: ', add(num1,num2))

    elif choice == '2':
      print('O resultado é: ', sub(num1,num2))

    elif choice == '3':
      print('O resultado é: ', mult(num1,num2))

    elif choice == '4':
      print('O resultado é: ', div(num1,num2))
    
    break
    
  else:
    print("Opção inválida")