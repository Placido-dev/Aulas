# def imprimir(a, b, c): <- parametros
#     print(a, b, c) 


# imprimir(1, 2, 3) <- argumentos
# imprimir(4, 5, 6) <- argumentos

def separacao():
    print('-' * 35)

def aula(numero_aula=0):
    print(f'Aula {numero_aula}')


aula(1)
separacao()

def saudacao(nome='Sem Nome'):
    print(f'Olá, {nome}!')


saudacao('Segredo')
saudacao('Guilherme')
saudacao()

separacao()
aula(2)    
separacao()    

def soma(x, y):
    print(x + y)
    # print(x * y)

soma(1, 2)    
soma(1, 56)

separacao()
aula(3)
separacao()