
cidade1 = 'Floripa'
cidade2 = 'Rio de Janeiro'
cidade3 = 'São Paulo'

cidades = ['Floripa', 'Rio de janeiro', 'São Paulo']
print(cidades)

cidades[2] = 'Fortaleza'
print(cidades)

cidades[-1] = 'Salvador' # A posição [-1] sempre será a última posição do vetor.
print(cidades)

cidades.append('Natal')
print(cidades)

cidades.append('Vitória')
print(cidades)

cidades.remove('Rio de janeiro')
print(cidades)

cidades.pop(0) # Remove o iten da posição específica
print(cidades)

cidades.clear() #Remove tudo
print(cidades)

cidades.insert(0, 'Floripa')
print(cidades)

cidades.insert(1, 'Rio de janeiro')
print(cidades)

cidades.insert(1, 'São Paulo')
print(cidades)

cidades.sort() # Organiza em ordem alfabética
print(cidades)

print('Concatenando listas:')

numeros = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd', 'e']

concatena = numeros + letras
print(concatena)

numeros.extend(letras) 
print(numeros)