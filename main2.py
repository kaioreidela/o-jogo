# importando bibliotecas necessarias

import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

# inicializando o pygame
pygame.init()

#criando diretorios
diretorio_principal=os.path.dirname(__file__)
diretorio_imagens=os.path.join(diretorio_principal,'imagens')

#criando e definindo variaveis
Largura=640
Altura=480
pontos = 0
Branco=(255,255,255)
Preto=(0,0,0)

escolha_obstaculo = choice([0, 1])

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comincsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado
#criacao de tela
tela=pygame.display.set_mode((Largura,Altura))

#criacao do nome do jogo
pygame.display.set_caption("jogo")

#organizando e definindo imagens da spritesheet
sprite_sheet=pygame.image.load(os.path.join(diretorio_imagens,'spritesjogo111.png')).convert_alpha()
imgfundo_dia=pygame.image.load('imagens/fundopixel_dia.jpg')
imgfundo_noite=pygame.image.load('imagens/fundopixel_noite.jpg')

class Urubu(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.imagens_player=[]
    for i in range(4,8):
      img = sprite_sheet.subsurface((i*32,0),(32,32))
      img=pygame.transform.scale(img,(32*4,32*4))
      self.imagens_player.append(img)

    self.index_lista=0
    self.image=self.imagens_player[0]
    self.mask=pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.escolha = escolha_obstaculo
    self.rect.center=(50,50)


  def update(self):
    if self.escolha == 1:
     if self.rect.topright[0] < 0:
       self.rect.x = Largura
       self.rect.x -= 10

    if self.index_lista > 3:
       self.index_lista = 0
    self.index_lista += 0.25
    self.image = self.imagens_player[int(self.index_lista)]

#criacao da classe vaqueiro
class Vaqueiro(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.imagens_player=[]

    #definindo imagens quais imagens sao a do vaqueiro na spritesheet
    for i in range(4):
      img = sprite_sheet.subsurface((i*32,0),(32,32))
      img=pygame.transform.scale(img,(32*4,32*4))
      self.imagens_player.append(img)

    #posicao inicial do vaqueiro e definicao de mascara pra colisao
    self.index_lista=0
    self.image=self.imagens_player[0]
    self.rect=self.image.get_rect()
    self.mask=pygame.mask.from_surface(self.image)
    self.pos_y_inicial = Altura - 96 - 96//2
    self.rect.center=(100,Altura-96)
    self.pulo = False
  def pular(self):
    self.pulo = True

  #sistema de atualizacao do personagem vaqueiro com definicao de altura de pulo e velocidade da animacao
  def update(self):
    #pulo e altura do pulo
    if self.pulo == True:
        if self.rect.y <= 170:
          self.pulo = False
        self.rect.y -= 18
    # para quando o vaqueiro nao estiver pulando
    else:

      if self.rect.y < self.pos_y_inicial:
        self.rect.y += 18
      else:
        self.rect.y = self.pos_y_inicial
    #velocidade de animacao
    if self.index_lista > 3 :
      self.index_lista=0
    self.index_lista +=0.25
    self.image=self.imagens_player[int(self.index_lista)]

class Chao(pygame.sprite.Sprite):
  def __init__(self,pos_x):
    pygame.sprite.Sprite.__init__(self)
    self.image=sprite_sheet.subsurface((9*32,0),(32,32))
    self.image=pygame.transform.scale(self.image,(32*4,32*4))
    self.rect=self.image.get_rect()
    self.rect.y=Altura-128
    self.rect.x=pos_x *128

  def update(self):
    if self.rect.topright[0] < 0:
      self.rect.x=Largura
    if pontos <= 50:
      self.rect.x -=10
    else:
      self.rect.x -=20


class Cacto(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = sprite_sheet.subsurface((8* 32, 0), (32, 32))
    self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))
    self.rect=self.image.get_rect()
    self.mask = pygame.mask.from_surface(self.image)
    self.rect.center=(Largura,Altura -45)

  def update(self):
    if self.rect.topright[0] < 0:
      self.rect.x = Largura
    if pontos <= 50:
      self.rect.x -=10
    else:
      self.rect.x -=20

todas_as_sprites=pygame.sprite.Group()
vaqueiro=Vaqueiro()
todas_as_sprites.add(vaqueiro)

urubu = Urubu()
todas_as_sprites.add(urubu)

for i in range(Largura*2//64):
  chao=Chao(i)
  todas_as_sprites.add(chao)

cacto=Cacto()
todas_as_sprites.add(cacto)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)
grupo_obstaculos.add(urubu)

relogio=pygame.time.Clock()
while True:
  relogio.tick(30)
  #trocando do dia pra noite
  if pontos <= 50:
    #tela.fill(Branco)
    tela.blit(imgfundo_dia,(0,0))
  else:
    #tela.fill(Preto)
    tela.blit(imgfundo_noite, (0, 0))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        if vaqueiro.rect.y != vaqueiro.pos_y_inicial:
          pass
        else:
          vaqueiro.pular()

  colisoes=pygame.sprite.spritecollide(vaqueiro,grupo_obstaculos,False,pygame.sprite.collide_mask)

  todas_as_sprites.draw(tela)
  if cacto.rect.topright[0] <= 0 or urubu.rect.topright[0] <= 0:
    escolha_osbtaculo = choice([0,1])
    cacto.rect.x = Largura
    urubu.rect.x = Largura
    cacto.escolha = escolha_obstaculo
    urubu.escolha = escolha_obstaculo

  if colisoes:
    pass
  else:
    pontos += 1
    todas_as_sprites.update()

  textos_pontos = exibe_mensagem(pontos, 40, (50,10,25))

  tela.blit(textos_pontos, (520, 30))


  pygame.display.flip()


