""" Exercicio 38 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. """

# Exercicio 38
valor_saque = int(input('Digite o valor do saque: '))

if (valor_saque >= 10) and (valor_saque <= 600):
    nota_100 = valor_saque//100
    valor_saque = valor_saque - 100*nota_100

    nota_50 = valor_saque//50
    valor_saque = valor_saque - 50*nota_50

    nota_10 = valor_saque//10
    valor_saque = valor_saque - 10*nota_10

    nota_5 = valor_saque//5
    valor_saque = valor_saque - 5*nota_5

    nota_1 = valor_saque//1
else:
    print('Por favor, digite um valor entre 10 e 600.')

print('Notas de 100: ', nota_100)
print('Notas de 50: ', nota_50)
print('Notas de 10: ', nota_10)
print('Notas de 5: ', nota_5)
print('Notas de 1: ', nota_1)
