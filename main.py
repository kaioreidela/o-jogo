
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange , choice
import variaveis


# inicializando o pygame
pygame.init()
pygame.mixer.init()

while True:
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
      #botao secreto
      if event.key == K_a:
        variaveis.pontos += 500
      if event.key == K_SPACE and variaveis.colidiu == False:
        if variaveis.vaqueiro.rect.y != variaveis.vaqueiro.pos_y_inicial:
          pass
        else:
          variaveis.vaqueiro.pular()
      if event.key == K_f and variaveis.colidiu == True:
        variaveis.reinicia_jogo()


  colisoes=pygame.sprite.spritecollide(variaveis.vaqueiro,variaveis.grupo_obstaculos,False,pygame.sprite.collide_mask)

  variaveis.todas_as_sprites.draw(variaveis.tela)

  if variaveis.cacto.rect.topright[0] <= 0 or variaveis.urubu.rect.topright[0] <= 0:
    escolha_osbtaculo = choice([0,1])
    variaveis.cacto.rect.x = variaveis.Largura
    variaveis.urubu.rect.x = variaveis.Largura
    variaveis.cacto.escolha = variaveis.escolha_obstaculo
    variaveis.urubu.escolha = variaveis.escolha_obstaculo

  if colisoes and variaveis.colidiu == False:
    variaveis.som_morte.play()
    variaveis.colidiu = True

  if variaveis.colidiu:
    if variaveis.pontos % 100 ==0:
      variaveis.pontos+=1
    variaveis.tela.blit(variaveis.img_morte, (0, 0))

    restart=variaveis.exibe_mensagem('press f to restart',50, variaveis.Branco)
    variaveis.tela.blit(restart,(variaveis.Largura//2,variaveis.Altura//2 +60))


  else:
    variaveis.pontos += 1
    variaveis.todas_as_sprites.update()
    textos_pontos = variaveis.exibe_mensagem(variaveis.pontos, 40, (50, 10, 25))

  if variaveis.pontos % 100 == 0 :
    if variaveis.velocidade_jogo == 11:
      variaveis.velocidade_jogo +=0
    else:
     variaveis.velocidade_jogo += 10



  variaveis.tela.blit(textos_pontos, (780, 30))


  pygame.display.flip()
