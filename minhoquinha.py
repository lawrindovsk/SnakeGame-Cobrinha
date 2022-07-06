import pygame#Importando o Pygame para o Pycharm.
import time
import random
from pygame.locals import *

snake_speed = 10

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

pygame.init() #Faz o código funcionar, iniciar.
game_window = tela = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Minhoquinha game by Gustavo Laurindo (lawrindovsk)')

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(200, 200), (210, 200), (220,200)]# Aqui fica o(a) Snake/Minhoca , e o tamanho dela.
snake_skin = pygame.Surface((10,10))# Superficie da snake.
snake_skin.fill((0, 255, 0))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

my_direction = RIGHT

relogio = pygame.time()

while True:
    relogio.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if colisao(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    tela.fill((0, 0, 0))
    tela.blit(apple, apple_pos)
    for pos in snake:
        tela.blit(snake_skin, pos)

    pygame.display.update()

pygame.display.update()

#Pontuação
score = 0
#Método para mostrar pontuação do jogador
def show_score(choice, color, font, size):

    # Definindo tamanho do score/pontuação e fone.
    score_font = pygame.font.SysFont(font, size)

    # criando display
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # criando um objeto retangular
    # objeto de texto
    score_rect = score_surface.get_rect()


   # mostrando texto
    tela.blit(score_surface, score_rect)

