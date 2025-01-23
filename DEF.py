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

separacao()
aula(6)
separacao()

