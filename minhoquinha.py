import pygame #Importando o Pygame para o Pycharm.

pygame.init() #Faz o código funcionar, iniciar.
tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Minhoquinha game by Gustavo Laurindo (lawrindovsk)')
pygame.display.update()

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))






red = (255, 0, 0) # red = cor vermelha;
blue = (0, 0, 255) # blue = cor azul;
black = (0, 0, 0) # black = cor preta;
white = (255, 255, 255) # white = cor branca;


game_over = False #Não permite o loop infinito , e também faz o jogo não acabar derrepente sem uma punição que tenha sentido.

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

            x1 += x1_change
            y1 += y1_change




            tela.fill((white))




    pygame.draw.rect(tela, blue, [200, 150, 10, 10]) #Aqui fica o(a) Snake/Minhoca , "rect" de retangular , e depois as cores.
    pygame.display.update() #Apenas um refresh , ou um atualizar a tela.

    pygame.display.update()

    clock.tick(30)

pygame.quit()#Finaliza o pygame.
quit() #Sair.