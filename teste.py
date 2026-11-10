import pygame
import random
pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Meu primeiro jogo")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 28)

x = 280
y = 180
moeda_x = 100
moeda_y = 100
pontos = 0
vidas = 3                                               # NOVO
inimigo_x = 100
inimigo_y = 300
velocidade = 3

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x = x - 5
    if teclas[pygame.K_RIGHT]:
        x = x + 5
    if teclas[pygame.K_UP]:
        y = y - 5
    if teclas[pygame.K_DOWN]:
        y = y + 5

    if x < 0:
        x = 0
    if x > 560:
        x = 560
    if y < 0:
        y = 0
    if y > 360:
        y = 360

    inimigo_x = inimigo_x + velocidade
    if inimigo_x < 0 or inimigo_x > 560:
        velocidade = -velocidade

    jogador = pygame.Rect(x, y, 40, 40)
    moeda = pygame.Rect(moeda_x, moeda_y, 20, 20)
    inimigo = pygame.Rect(inimigo_x, inimigo_y, 40, 40)
    if jogador.colliderect(moeda):
        moeda_x = random.randint(0, 580)
        moeda_y = random.randint(0, 380)
        pontos = pontos + 1
    if jogador.colliderect(inimigo):
        x = 280
        y = 180
        vidas = vidas - 1                               # MUDOU (antes era pontos = 0)
        if vidas == 0:                                  # NOVO
            pontos = 0                                  # NOVO
            vidas = 3                                   # NOVO

    tela.fill((30, 30, 30))
    pygame.draw.rect(tela, (0, 200, 0), (x, y, 40, 40))
    pygame.draw.rect(tela, (255, 220, 0), (moeda_x, moeda_y, 20, 20))
    pygame.draw.rect(tela, (220, 0, 0), (inimigo_x, inimigo_y, 40, 40))
    texto = fonte.render("Pontos: " + str(pontos), True, (255, 255, 255))
    tela.blit(texto, (10, 10))
    texto_vidas = fonte.render("Vidas: " + str(vidas), True, (255, 255, 255))   # NOVO
    tela.blit(texto_vidas, (10, 40))                                            # NOVO
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()