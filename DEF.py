# def imprimir(a, b, c): <- parametros
#     print(a, b, c) 


# imprimir(1, 2, 3) <- argumentos
# imprimir(4, 5, 6) <- argumentos

def separacao():
    print('-' * 35)

def aula(numero_aula=0):
    print(f'Aula {numero_aula}')


# aula(1)
# separacao()

# def saudacao(nome='Sem Nome'):
#     print(f'Olá, {nome}!')


# saudacao('Segredo')
# saudacao('Guilherme')
# saudacao()

# separacao()
# aula(2)    
# separacao()    

# def soma(x, y, z):
#     print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

# soma(1, 2, 3)
# soma(1, y=2, z=5) #  <- a partir de um argumento nomeado, os próximos deverão ser nomeaods

# separacao()
# aula(3)
# separacao()

# def soma2(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)
#     else:
#         print(f'{x=} {y=}', '|', 'x + y = ', x + y)

# soma2(1, 2)        
# soma2(3, 7, 5)        
# soma2(3, 7, 0)        

# separacao()
# aula(4)
# separacao()


# x = 1

# def escopo():
#     global x
#     x = 10

#     def outra_funcao():
#         global x
#         x = 11
#         y = 2
#         print(x, y)

#     outra_funcao()    
#     print(x)

# print(x)
# escopo()
# print(x)

# separacao()
# aula(5)
# separacao()

# def soma_teste(x, y):
#     return x + y

# result1 = soma_teste(5, 5)
# result2 = soma_teste(2, 2)
# print(result1 + result2)

# separacao()
# aula(6)
# separacao()

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# soma_1_2_3 = soma(1, 2, 3)        
# print(soma_1_2_3)

# soma_4_5_6 = soma(4, 5, 6)        
# print(soma_1_2_3)

# numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# outra_soma = soma(*numeros)        
# print(outra_soma)

# print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
# print(*numeros)

# separacao()
# aula(7)
# separacao()

# def multiplicar_arg(*args):
#     total = args
#     for numero in args:
#         total = numero
#         return total
    

# mult = multiplicar_arg(1 * 2 * 3 * 4 * 5)
# print(mult)

# def par_impar(x):
#     if x % 2 == 0:
#         return 'par'
#     else:
#         return 'ímpar'
    
# numero = par_impar(33)
# numero2 = par_impar(34)
# print(numero)
# print(numero2)

separacao()
aula(8)
separacao()

# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'nome': 'Guilherme Silva',
    'sobrenome': 'Plácido',
    'endereco': [
        {'rua': 'Antonio', 'numero': 77}
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa['endereco']:
    print({chave["rua"]})