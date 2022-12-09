import pytest
import pygame
import variaveis


def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comincsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado


def test_exibe_mensagem_pontos():
    textos_pontos = exibe_mensagem(variaveis.pontos, 40, (50, 10, 25))
    assert textos_pontos == textos_pontos


def test_exibe_mensagem_restart():
    restart = variaveis.exibe_mensagem('press f to restart', 50, variaveis.Branco)
    assert restart == restart

def test_exibe_mensagem_tutorial():
    textos_tutorial= variaveis.exibe_mensagem("para pular aperte a tecla 'SPACE' ", 40, (50, 10, 25))
    assert textos_tutorial == textos_tutorial

def test_exibe_mensagem_creditos():
    textos_creditos= variaveis.exibe_mensagem("creditos para todos que ajudaram no projeto", 40, variaveis.Preto)
    assert textos_creditos == textos_creditos

def test_exibe_mensagem_dialogos():
    textos_dialogos= variaveis.exibe_mensagem("olá vamos ajudar raimundo a enfrentar os obstaculos que aparece em sua vida", 40, variaveis.Preto)
    assert textos_dialogos == textos_dialogos




def test_reiniciajogo():
    if variaveis.reinicia_jogo() == True:
       assert variaveis.pontos == 0
       assert variaveis.velocidade_jogo == 10
       assert  variaveis.colidiu == False
       assert  variaveis.vaqueiro.rect.y == Altura - 96 - 96 // 2
       assert variaveis.vaqueiro.pulo == False
       assert variaveis.urubu.rect.x == Largura
       assert variaveis.cacto.rect.x == Largura
       assert v.escolha_obstaculo == choice([0, 1])
