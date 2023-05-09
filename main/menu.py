import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Atributos da tela

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Xadrez")


while True:

    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()