print('''Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salario com 15% de aumento.\n''')
salario = float(input('Digite seu salário: R$'))
aumento = float(input('Digite a % de aumento: '))
novo_salario = (salario * aumento /100) + salario
print(f'O seu antigo salário de R${salario:.2f} + o aumento de {aumento:.2f}%, rsendo assim seu novo salario é R${novo_salario}')