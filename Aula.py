"""
1 Etapa
Calculo do primeiro dígito do CPF
CPF: 727.739.590-51
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  727.739.590-51 (727739590)
   10  9  8  7  6  5  4  3  2
*  7   2  7  7  3  9  5  9  0
   70  18 56 49 18 45 20 27 0

Somar todos os resultados: 
70+18+56+49+18+45+20+27+0 = 303
Multiplicar o resultado anterior por 10
303 * 10 = 3030
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '72773959051'
dez_digitos = cpf[:9]
contador_regressivo2 = 10
resultado = 0

for resultado_digito2 in dez_digitos:
    resultado += int(resultado_digito2) * contador_regressivo2
    contador_regressivo2 -= 1
resultado_digito2 = (resultado * 10) % 11
resultado_digito2 = resultado_digito2 if resultado_digito2 <= 9 else 0
print(resultado_digito2)

"""
2 Etapa
Calculo do segundo dígito do CPF
CPF: 727.739.590-51
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  727.739.590-51 (727739590)
   11 10  9  8  7  6  5  4  3  2
*  7   2  7  7  3  9  5  9  0  5 <-- PRIMEIRO DIGITO
   77 20 63 56 21 54 25 36  0 10

Somar todos os resultados:
77+20+63+56+21+54+25+36+0+10 = 362
Multiplicar o resultado anterior por 10
362 * 10 = 3620
Obter o resto da divisão da conta anterior por 11
3620 % 11 = 
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 
"""

cpf = '72773959051'
dez_digitos = cpf[:10]
contador_regressivo2 = 11
resultado = 0

for resultado_digito2 in dez_digitos:
    resultado += int(resultado_digito2) * contador_regressivo2
    contador_regressivo2 -= 1
resultado_digito2 = (resultado * 10) % 11
resultado_digito2 = resultado_digito2 if resultado_digito2 <= 9 else 0
print(resultado_digito2)