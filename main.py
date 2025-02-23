import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Reflorestar")

COR_FUNDO = (255,255,255)
LARGURA,ALTURA = 1000,800
FPS = 60
VelJogador = 5

janela = pygame.display.set_mode((LARGURA,ALTURA))
    
def main(janela):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()
if __name__ == "__main__":
    main(janela)