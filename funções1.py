# Funções: Ou elas realizam uma tarefa (tipo, imprimir algo na tela) ou retornam um valor para a função.
# def nome_funcao(parâmetro1, parâmetro2, ...): "Definindo a função, aqui eu coloco os PARÂMETROS"
#     Código...
#
# nome_funcao('argumento1','arqumento2', ... )  "Chamada da função, aqui eu coloco os ARGUMENTOS"

nome = input('Entre com o nome do cliente: ')
x = int(input('Entre com a quantidade de produtos em estoque: '))

def boas_vindas(nome):
    print(f'Olá {nome}!')
    print(f'Temos {str(produto(x))} produtos em estoque.')


def produto(x):
    return x

boas_vindas(nome)