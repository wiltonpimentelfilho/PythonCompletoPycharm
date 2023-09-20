#Loop dentro de loop

#Outer Loop
  #Inner Loop

for numero1 in range(5):
  print(f'Produto {numero1} loop de fora, Outer')
  for numero2 in range(5):
    print(f'{numero1, numero2} loop de dentro, Inner loop')

