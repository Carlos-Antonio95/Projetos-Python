print('''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta, pinta uma área de 2m²\n''')
largura = float(input('Larura da parede: '))
altura = float(input('Altura da parede'))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f} m2')
tinta = area / 2
print(f'Voce precisa de {tinta:.2f} para pintar uma area de {area:.2f}')