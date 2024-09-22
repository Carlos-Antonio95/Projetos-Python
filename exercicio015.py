print('''Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado e a quantidade de dias pelas quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por km rodado.\n''')
alugel_dias = int(input('Quantos dias o carro ficou alugado: '))
km_rodado = float(input('Quantos km rodou com  o carro: '))
valor_dias = alugel_dias * 60
valor_km = km_rodado * 0.15
valor_total = valor_dias + valor_km
print('Calculando...')
print(f'''O carro foi alugado por {alugel_dias} dias e rodou {km_rodado:.2f}km, sendo assim somando o valor
de R${valor_dias} + R$ {valor_km:.2f} fica o saldo devedor de: R$ {valor_total:.2f}''')
print('Obrigado pela preferencia!')
