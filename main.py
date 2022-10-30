#inicializando pygame
import os
import pygame
from pygame.locals import *
from random import randint
from sys import exit

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
pygame.init()
#criando tela

largura=640
altura=480
x=largura/2
y=altura/2
x_azul=randint(40,600)
y_azul=randint(50,430)

tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('lampião')

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'spritesjogo111.png')).convert_alpha()

class Lampião(pygame.sprite.Sprite):
    def __int__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_lampião = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 32,0), (32,32))
            self.imagens_lampião.append(img)
         self.index_lista = 0
         self.image = self.imagens_lampião[0]
          self.rect = self.image.get_rect()
           self.rect.center = (100,100)
     def update(self):
         if self.index_lista > 2:
             self.index_lista = 0
         self.index_lista += 0.25
         self.image = self.imagens_lampião[int(self.index_lista)]

class Lampião(pygame.sprite.Sprite):
    def __int__(self):
        pygame.sprite.Sprite.__init__(self)
        pass

    todas_as_sprites = pygame.sprite.Group()
    lampião = Lampião()
    todas_as_sprites.add(lampião)

relogio=pygame.time.Clock()
#roda o jogo
while True:
    #velocidade di objeto
    relogio.tick(30)
    tela.fill((0,0,0))
    #saida do jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()



            pygame.display.flip()
    #movimentaçao
    if pygame.key.get_pressed()[K_a]:
        x= x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y= y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    ret_vermelho =  pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    ret_azul =  pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)

    pygame.display.update()