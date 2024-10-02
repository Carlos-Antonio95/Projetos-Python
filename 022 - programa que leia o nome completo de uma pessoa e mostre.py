print('''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.\n''')
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome maiúsculo é: {nome.upper()}')
print(f'Seu nome minusculo é: {nome.lower()}')
print(f'Seu noem tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')#procura o primeiro espaço e diz em qual caractere achou