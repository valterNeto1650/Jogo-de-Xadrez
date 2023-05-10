import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Atributos da tela

largura = 800
altura = 600

larguraBotao = 250
alturaBotao = 50

larguraPeca = 50
alturaPeca = 50

posicaoXBotao = 280
posicaoYBotao = 420

tamanho = largura , altura
tamanhoBotao = larguraBotao, alturaBotao
#tamanhoPeca = larguraPeca, alturaPeca

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Xadrez")

fundo = pygame.image.load("assets/fundo/telaMenu.png").convert()
fundo = pygame.transform.scale(fundo, tamanho)

fundoJogo = pygame.image.load("assets/fundo/telaGame2.png").convert()
fundoJogo = pygame.transform.scale(fundoJogo, tamanho)

botaoJogar = pygame.image.load("assets/fundo/botaoJogar.png").convert()
botaoJogar = pygame.transform.scale(botaoJogar, tamanhoBotao)
retangulo = botaoJogar.get_rect()

"""
bispoPreto = pygame.image.load("assets/peças/black_bishop.png").convert()
bispoPreto = pygame.transform.scale(bispoPreto, tamanhoPeca)

reiPreto = pygame.image.load("assets/peças/black_king.png").convert()
reiPreto = pygame.transform.scale(reiPreto, tamanhoPeca)

cavaloPreto = pygame.image.load("assets/peças/black_knight.png").convert()
cavaloPreto = pygame.transform.scale(cavaloPreto, tamanhoPeca)

peaoPreto = pygame.image.load("assets/peças/black_pawn.png").convert()
peaoPreto = pygame.transform.scale(peaoPreto, tamanhoPeca)

rainhaPreto = pygame.image.load("assets/peças/black_queen.png").convert()
rainhaPreto = pygame.transform.scale(rainhaPreto, tamanhoPeca)

torrePreto = pygame.image.load("assets/peças/black_rook.png").convert()
torrePreto = pygame.transform.scale(torrePreto, tamanhoPeca)
"""

retangulo.x = posicaoXBotao
retangulo.y = posicaoYBotao

click = False

while True:
   
    
    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Verifique se o botão esquerdo do mouse foi clicado dentro do retângulo
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if retangulo.collidepoint(event.pos):
                click = True 
                print("Imagem clicada!")
        

    if click:
            tela.blit(fundoJogo, (0, 0))
            
    else:
        tela.blit(fundo, (0, 0))
        tela.blit(botaoJogar, (posicaoXBotao, posicaoYBotao))
    #Desenha a tela
    
    
    pygame.display.update()