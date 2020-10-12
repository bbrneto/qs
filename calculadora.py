operacao = input('''
1 para adicao
2 para subtracao
3 para multiplicacao
4 para divisao
''')

numero_1 = int(input('Primeiro numero: '))

numero_2 = int(input('Segundo numero: '))

if operacao == '1':
    print('{} + {} = '.format(numero_1, numero_2))
    print(numero_1 + numero_2)

elif operacao == '2':
    print('{} - {} = '.format(numero_1, numero_2))
    print(numero_1 - numero_2)

elif operacao == '3':
    print('{} * {} = '.format(numero_1, numero_2))
    print(numero_1 * numero_2)

elif operacao == '4':
    print('{} / {} = '.format(numero_1, numero_2))
    print(numero_1 / numero_2)

else:
    print('Opcao invalida')
