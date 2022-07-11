###### SNAKE GAME by Gustavo Laurindo (lawrindovsk)
#Aqui em baixo os imports.
import pygame, random
from pygame.locals import *
pygame.init()
pygame.font.init()

#Método Grid Random
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

#Método de colisão.
def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, False)

#Tela do jogo e nome.
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake Game by lawrindovsk')
####################################################
#Criando a snake/minhoca/cobra
cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((0,255,0))
###################################################
#Maça e fazendo ela aparecer na tela puxando o grid random.
maca_pos = on_grid_random()
maca = pygame.Surface((10,10))
maca.fill((255,0,0))
######################################
my_direction = LEFT

relogio = pygame.time.Clock()
############################
#Aqui fica as BINDS(a forma que o jogador vai controlar) , eventos que acontecem com a snake e o update.
while True:
    relogio.tick(10)
    menssagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(menssagem, False, (255,255,255))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
        #Comandos de movimento = caso ele aperte o botão bindado , ele executa a ação.
        if evento.type == KEYDOWN:
            if evento.key == K_UP:
                my_direction = UP
            if evento.key == K_DOWN:
                my_direction = DOWN
            if evento.key == K_LEFT:
                my_direction = LEFT
            if evento.key == K_RIGHT:
                my_direction = RIGHT

    if colisao(cobra[0], maca_pos):
        maca_pos = on_grid_random()
        cobra.append((0,0))
        pontos = pontos + 1

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if my_direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if my_direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if my_direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if my_direction == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    tela.fill((0, 0, 0))
    tela.blit(maca, maca_pos)
    for pos in cobra:
        tela.blit(cobra_skin, pos)

        tela.blit(texto_formatado, (390,20))
    pygame.display.update()