print('''Faça um programa que leia o preço de um produto e mostre seu novo 
preço, com 5% de desconto.\n''')
produto = float(input('Digite o valor do produto:R$ '))
desconto =produto - (produto * 5 /100)
print(f'O novo valor do produto com desconto é R${desconto:.2f}')