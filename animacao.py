import pygame
from pygame.locals import *
from sys import exit
import os
import variaveis
from random import randrange, choice

# inicializando o pygame
pygame.init()
pygame.mixer.init()


while True:

  variaveis.janela.fill([0] * 3)
  #iniciando som

  variaveis.relogio.tick(30)
  #trocando do dia pra noite
  if variaveis.pontos <= 50:
    #tela.fill(Branco)
    variaveis.tela.blit(variaveis.imgfundo_dia,(0,0))

  else:
    import menu2

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_p:
        if variaveis.vaqueiro.rect.y != variaveis.vaqueiro.pos_y_inicial:
          pass
        else:
          variaveis.vaqueiro.pular()

  variaveis.pontos += 1
  variaveis.todas_as_sprites.update()

  textos_pontos = variaveis.exibe_mensagem(variaveis.pontos, 1, (50, 10, 25))
  variaveis.tela.blit(textos_pontos, (780, 30))

  #desenhando janela
  pygame.draw.rect(variaveis.janela, (0, 0, 200), (10, 10, 60, 40));
  #titulo do jogo
  titulo_jogo = ' As Aventuras de Raimundo';

  #definicao e inicializacao de fonte
  pygame.font.init();
  fonte = pygame.font.get_default_font();
  # titulo
  fontesys = pygame.font.SysFont(fonte, 70);
  titulo = fontesys.render(titulo_jogo, 1, variaveis.Preto);
  variaveis.janela.blit(titulo, (150, 150));


  variaveis.todas_as_sprites.draw(variaveis.tela)
  pygame.display.flip()
