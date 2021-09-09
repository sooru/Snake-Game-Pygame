import pygame, random,os
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(os.getcwd()+'\Schizo.mp3')
pygame.mixer.music.play()

bgimg = pygame.image.load(os.getcwd()+'\snake4.png')
bgimg = pygame.transform.scale(bgimg, (700, 500))

white = [250, 250, 250]
black = [0, 0, 0]
colour1 = (20, 250, 20)
colour2 = (250, 0, 0)
snake_x = 45
snake_y = 45
snake_size = 15
exit_game = False
velx = 0
vely = 0
clock = pygame.time.Clock()
x = random.randint(2, 49)
y = random.randint(2, 29)
foody = 15* y
foodx = 15* x
score = 0
strlen = 1
gameover = False

font=pygame.font.SysFont(None,45)
def screen_score(text, colour, x, y):
    score = font.render(text, True, colour)
    gamewindow.blit(score, [x, y])


gamewindow = pygame.display.set_mode((700, 500))
gamewindow.fill(white)
pygame.display.update()

pygame.display.set_caption('GamingWithSuraj')
l = [[snake_x, snake_y]]
while not exit_game:
    if gameover:
        gamewindow.fill(colour1)
        screen_score('!!!!! GameOver !!!!!', (250, 0, 0), 300, 200)
        screen_score(f'Your Score : {score}', (250, 0, 0), 300, 230)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                # print(event.key)
                if event.key == 32:
                    velx = 0
                    vely = 0
                if event.key == 1073741906:
                    # print(event.key)
                    vely = -15
                    velx = 0
                if event.key == 1073741905:
                    vely = 15
                    velx = 0
                if event.key == 1073741903:
                    velx = 15
                    vely = 0
                if event.key == 1073741904:
                    velx = -15
                    vely = 0

        snake_x += velx
        snake_y += vely
        if (snake_x == foodx and snake_y == foody):
            x = random.randint(2, 32)
            y = random.randint(2, 19)
            foody = 15 * y
            foodx = 15 * x
            score += 10
            strlen += 1

        l.append([snake_x, snake_y])
        # print(l)
        if len(l) > strlen:
            l.pop(0)
        clock.tick(9)
        gamewindow.fill(white)
        gamewindow.blit(bgimg, (0, 0))
        screen_score('score :' + str(score), [0, 0, 250], 3, 3)
        pygame.draw.rect(gamewindow, [250, 0, 0], [foodx, foody, snake_size, snake_size])
        for x, y in l:
            # print(snake_x,'c')
            pygame.draw.rect(gamewindow, black, [x, y, snake_size, snake_size])

        pygame.display.update()
        if snake_x > 690 or snake_x < 0 or snake_y > 490 or snake_y < 0:

            pygame.mixer.music.load(os.getcwd()+'\over.mp3')
            pygame.mixer.music.play()
            gameover = True
        if [snake_x, snake_y] in l[:-1]:
            pygame.mixer.music.load(os.getcwd()+'\over.mp3')
            pygame.mixer.music.play()
            gameover = True