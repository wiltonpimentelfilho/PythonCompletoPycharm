
itens = [[1,2,3,4,5], [6,7,8,9,0]]
print(itens)

print(itens[0])
print(itens[1])

print(itens[0][0])
print(itens[0][1])
print(itens[1][0])

produtos = ['arroz', 'feijão', 'carne', 'frango']

item1, item2, item3, item4 = produtos
print(item1)

item1, item2, *outros = produtos
print(outros)
