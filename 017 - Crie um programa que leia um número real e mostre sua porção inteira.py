from math import hypot
print('''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.''')
CatetoOposto = float(input('Quanto mede o cateto oposto: '))
CatetoAdjacente = float(input('Quanto mede o cateto adjacente: '))
#hipotenusa = (CatetoOposto**2 + CatetoAdjacente**2) ** (1/2)
hi = hypot(CatetoOposto,CatetoAdjacente)
print(f'A hipotenusa vai medir {hi:.2f}')