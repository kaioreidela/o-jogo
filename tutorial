import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

# inicializando o pygame
pygame.init()
pygame.mixer.init()


#criando diretorios
diretorio_principal=os.path.dirname(__file__)
diretorio_imagens=os.path.join(diretorio_principal,'imagens')
diretorio_sons=os.path.join(diretorio_principal,'sons')

#musica de tutorial
som_tutorial=pygame.mixer.Sound(os.path.join(diretorio_sons,'tutorial.mpeg'))

#criando e definindo variaveis
Largura=853
Altura=599
pontos = 0
Branco=(255,255,255)
Preto=(0,0,0)


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
        if self.rect.y <= 260:
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
    if pontos <= 500:
      self.rect.x -=10
    else:
      self.rect.x -=20


todas_as_sprites=pygame.sprite.Group()
vaqueiro=Vaqueiro()
todas_as_sprites.add(vaqueiro)

for i in range(Largura*2//64):
  chao=Chao(i)
  todas_as_sprites.add(chao)
som=som_tutorial.play()
relogio=pygame.time.Clock()
while True:
  #iniciando som
  som

  relogio.tick(30)
  #trocando do dia pra noite
  if pontos <= 500:
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



  todas_as_sprites.update()

  textos_pontos = exibe_mensagem("para pular aperte a tecla 'SPACE' ", 40, (50, 10, 25))

  tela.blit(textos_pontos, (30, 30))
  todas_as_sprites.draw(tela)


  pygame.display.flip()
