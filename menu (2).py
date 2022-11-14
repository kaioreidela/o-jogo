import pygame
import random
from pygame import font
from sys import exit
from random import randint
import os

diretorio_principal=os.path.dirname(__file__)
diretorio_imagens=os.path.join(diretorio_principal,'imagens')

#dimenções da janela
largura = 1000
altura = 600
#posição da seta
posicao = 1

janela = pygame.display.set_mode((largura, altura));

#chamandos imagens
sprite_sheet=pygame.image.load(os.path.join(diretorio_imagens,'spritesjogo111.png')).convert_alpha()
imgfundo_dia=pygame.image.load('imagens/fundopixel_noite.jpg')



while True:
    janela.fill([0]*3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit ();

#menu
    pygame.draw.rect(janela, (0, 0, 200), (205, 100, 600, 400));
    menu = ' Raimundinho';
    jogar = 'jogar';
    opcoes = 'opções';
    pygame.font.init();
    fonte = pygame.font.get_default_font();
    #titulo
    fontesys = pygame.font.SysFont('comicsansms', 80);
    titulo = fontesys.render(menu, 1, (225,225,0));
    #opções
    fontesys = pygame.font.SysFont('comicsansms', 40);
    opcao1 = fontesys.render(jogar, 1, (225,225,0));
    opcao2 = fontesys.render(opcoes, 1, (225,225,0));
    #iprimindo o titulo e as opções
    janela.blit(imgfundo_dia, (0, 0))
    janela.blit(titulo, (310, 120));
    janela.blit(opcao1, (452, 200));
    janela.blit(opcao2, (452, 246));
    #roda pé
    fontesys = pygame.font.SysFont(fonte, 30);
    sair = '[ESC] - sair';
    enter = '[ENTER] - selecionar';
    esc = fontesys.render(sair, 1, (225,225,0));
    selecionar = fontesys.render(enter, 1, (225,225,0));
    janela.blit(esc, (220, 464));
    janela.blit(selecionar, (590, 464));

    #seta
    comandos = pygame.key.get_pressed();
    if comandos [pygame.K_UP]:
        posicao = 1;
    elif comandos [pygame.K_DOWN]:
        posicao = 2;

    if posicao == 1:
        #posicao = 1;
        seta = pygame.draw.polygon(janela, (0, 0, 0),  ((430, 223), (430, 237), (442, 230)));
    elif posicao == 2:
        #posicao = 2;
        seta = pygame.draw.polygon(janela, (0, 0, 0), ((430, 273), (430, 287), (442, 270)));
    #decta se o usuario clicou na tecla enter
    if comandos [pygame.K_RETURN]:
     #verifica em que posição a seta estava quando o usuario teclou enter
        if posicao == 1:
            import jogo
        elif posicao == 2:
            print("opções de jogo");
    #decta se o usuario clicou na tecla esc
    if comandos [pygame.K_ESCAPE]:
        print("sair");
        pygame.draw.rect(janela, (255, 0, 0), (305, 150, 400, 300));
        pygame.quit();

    #atualização da tela
    pygame.display.update();

#sair do programa
pygame.quit ();
