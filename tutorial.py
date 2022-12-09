
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange , choice
import variaveis


# inicializando o pygame
pygame.init()
pygame.mixer.init()


som_tutorial=pygame.mixer.Sound(os.path.join(variaveis.diretorio_sons,'tutorial.mpeg'))

som=som_tutorial.play()

while True:
  #iniciando som
  som

  variaveis.relogio.tick(30)
  #trocando do dia pra noite
  if variaveis.pontos <= 500:
    #tela.fill(Branco)
    variaveis.tela.blit(variaveis.imgfundo_dia,(0,0))
  else:
    #tela.fill(Preto)
    variaveis.tela.blit(variaveis.imgfundo_noite, (0, 0))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()

    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        if variaveis.vaqueiro.rect.y != variaveis.vaqueiro.pos_y_inicial:
           pass

        else:
          variaveis.vaqueiro.pular()



  variaveis.todas_as_sprites.update()

  textos_tutorial= variaveis.exibe_mensagem("para pular aperte a tecla 'SPACE' ", 40, (50, 10, 25))

  variaveis.tela.blit(textos_tutorial, (30, 30))
  variaveis.todas_as_sprites.draw(variaveis.tela)


  pygame.display.flip()
