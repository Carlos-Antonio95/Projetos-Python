import pygame
from pygame import mixer

print('''Exercício Python 21: Faça um programa em Python que abra e 
reproduza o áudio de um arquivo MP3.\n''')
mixer.init()
mixer.music.load('leonascimentooficial-cada-minuto-741b88.mp3')
mixer.music.play()
algo = str(input('Digite algo para parar a musica: '))