print('''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre 
quantos Dólares ela pode comprar.\n''')
carteira = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = carteira / 3.27
print(f'Com R$ {carteira:.2f} você pode comprar US$ {dolar:.2f}')