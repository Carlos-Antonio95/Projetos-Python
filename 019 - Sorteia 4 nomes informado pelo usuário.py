from random import choice #importa biblioteca randon
print('''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o 
nome do escolhido.\n''')
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))
lista = [aluno1,aluno2,aluno3,aluno4] #coloca todos os nomes dentro de uma lista
escolhido = choice(lista)# variavel escolhido vai receber o nome do aluno sorteado
print(f'O aluno escolhido foi {escolhido}')#imprime o nome do aluno sorteado
