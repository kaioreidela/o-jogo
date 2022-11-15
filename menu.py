import pygame
import random
from pygame import font
from sys import exit
from random import randint
import os

pygame.mixer.init()



#dimenções da janela
largura = 853
altura = 599
Preto=(0,0,0)
Branco=(255,255,255)
#posição da seta
posicao = 1

janela = pygame.display.set_mode((largura, altura))

#criando diretorios
diretorio_principal=os.path.dirname(__file__)
diretorio_imagens=os.path.join(diretorio_principal,'imagens')
diretorio_sons=os.path.join(diretorio_principal,'sons')

#chmando imagens e sons
sprite_sheet=pygame.image.load(os.path.join(diretorio_imagens,'spritesjogo111.png')).convert_alpha()
imgfundo=pygame.image.load('imagens/imgfundo2.png')
som_menu=pygame.mixer.Sound(os.path.join(diretorio_sons,'menu.mpeg'))

class Vaqueiro(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.imagens_player=[]

    #definindo imagens quais imagens sao a do vaqueiro na spritesheet
    for i in range(4):
      img = sprite_sheet.subsurface((i*32,0),(32,32))
      img=pygame.transform.scale(img,(32*4,32*4))
      self.imagens_player.append(img)

    #posicao inicial do vaqueiro
    self.index_lista=0
    self.image=self.imagens_player[0]
    self.rect=self.image.get_rect()
    self.rect.center=(100, 120)

  def update(self):
    if self.index_lista > 3 :
       self.index_lista=0
    self.index_lista +=0.25
    self.image=self.imagens_player[int(self.index_lista)]

class Urubu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_player = []
        for i in range(4, 8):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 4, 32 * 4))
            self.imagens_player.append(img)

        self.index_lista = 0
        self.image = self.imagens_player[0]
        self.rect = self.image.get_rect()
        self.rect.center = (800, 120)

    def update(self):
        if self.index_lista > 3:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_player[int(self.index_lista)]


som=som_menu.play()
som=0
while True:
    #iniciando som
    som=1

    janela.fill([0]*3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit ()




    #menu
    pygame.draw.rect(janela, (0, 0, 200), (10, 10, 60, 40))
    menu = ' As Aventuras de Raimundo'
    jogar = 'jogar'
    opcoes = 'tutorial'
    pygame.font.init()
    fonte = pygame.font.get_default_font()
    #titulo
    fontesys = pygame.font.SysFont(fonte, 70)
    titulo = fontesys.render(menu, 1, Preto)
    #opções
    fontesys = pygame.font.SysFont(fonte, 50)
    opcao1 = fontesys.render(jogar, 1, Preto)
    opcao2 = fontesys.render(opcoes, 1, Preto)
    #iprimindo o titulo e as opções
    janela.blit(imgfundo, (0, 0))
    janela.blit(titulo, (150, 150))
    janela.blit(opcao1, (600, 220))
    janela.blit(opcao2, (600, 270))
    #roda pé
    fontesys = pygame.font.SysFont(fonte, 30)
    sair = '[ESC] - sair'
    enter = '[ENTER] - selecionar'
    direito = '2022 ALL RIGHTS RESERVED DEVELOPMENT BY KAIOREIDELA & NNADSON12'
    esc = fontesys.render(sair, 1, Branco)
    selecionar = fontesys.render(enter, 1,Branco)
    direito = fontesys.render(direito, 1, Branco)
    janela.blit(esc,(220, 380))
    janela.blit(selecionar, (590, 380))
    janela.blit(direito, (60,560))


    #seta
    comandos = pygame.key.get_pressed()
    if comandos [pygame.K_UP]:
        posicao = 1
    elif comandos [pygame.K_DOWN]:
        posicao = 2

    if posicao == 1:
        #posicao = 1;
        seta = pygame.draw.polygon(janela, (0, 0, 0),  ((430, 223), (430, 237), (442, 230)))
    elif posicao == 2:
        #posicao = 2;
        seta = pygame.draw.polygon(janela, (0, 0, 0), ((430, 273), (430, 287), (442, 270)))
    #decta se o usuario clicou na tecla enter
    if comandos [pygame.K_RETURN]:
     #verifica em que posição a seta estava quando o usuario teclou enter
        if posicao == 1:
           #chamada de arquivo.py do jogo
           som_menu.set_volume(0)
           import main
        elif posicao == 2:
           som_menu.set_volume(0)
           import tutorial
    #decta se o usuario clicou na tecla esc
    if comandos [pygame.K_ESCAPE]:
        print("sair")
        pygame.draw.rect(janela, (255, 0, 0), (305, 150, 400, 300))
        pygame.quit()

    todas_as_sprites = pygame.sprite.Group()
    vaqueiro = Vaqueiro()
    todas_as_sprites.add(vaqueiro)
    urubu = Urubu()
    todas_as_sprites.add(urubu)


    #atualização da tela
    todas_as_sprites.draw(janela)
    pygame.display.update()

#sair do programa
pygame.display.flip()