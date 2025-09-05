import pygame
import random
import time

pygame.init()

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)

#Tamanho da tela
largura_tela = 700
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

clock = pygame.time.Clock()
tamanho_cobra = 10
velocidade_cobra = 15

fonte_mensagem = pygame.font.SysFont(None, 50)
fonte_placar = pygame.font.SysFont(None, 35)

def placar(pontos):
    valor = fonte_placar.render("Pontuação: " + str(pontos), True, verde)
    tela.blit(valor, [0, 0])

def cobra(tamanho_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, preto, [x[0], x[1], tamanho_cobra, tamanho_cobra])

def mensagem(msg, cor):
    mesg = fonte_mensagem.render(msg, True, cor)
    tela.blit(mesg, [largura_tela / 6, altura_tela / 3])

def jogo():
    game_over = False
    game_close = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0

    while not game_over:

        while game_close:
            tela.fill(branco)
            mensagem("Você perdeu! Pressione C para jogar novamente ou Q para sair", vermelho)
            placar(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_cobra
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_cobra
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_cobra
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_cobra
                    x1_mudanca = 0

        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            game_close = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(branco)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        cobra_cabeca = []
        cobra_cabeca.append(x1)
        cobra_cabeca.append(y1)
        lista_cobra.append(cobra_cabeca)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == cobra_cabeca:
                game_close = True

        cobra(tamanho_cobra, lista_cobra)
        placar(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade_cobra)

    pygame.quit()
    quit()

jogo()

