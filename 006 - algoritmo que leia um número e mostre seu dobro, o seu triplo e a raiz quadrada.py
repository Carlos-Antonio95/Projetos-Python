#crie um algoritmo que leia um n�mero e mostre seu dobro, o seu triplo e a raiz quadrada
n = int(input('Digite um n�mero: '))
d = n * 2
t = n * 3
r = pow(n,(1/2))
print(f'O dobro de {n} vale {d} , o triplo vale {t} e sua raiz quadrada é {r:.2f}')