import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
gamefont = pygame.font.SysFont('comicsans', 15)
endfont = pygame.font.SysFont('comicsans', 25)

background = pygame.transform.scale(pygame.image.load(os.path.join('background.png')), (WIDTH, HEIGHT))
pygame.display.set_caption('Pathfinder')
FPS = 60    #  frames per second
vel = 4     #   how qickly the ball is moving
move = 0   # where ball starts off then you add velocity to move forward
padsize = 100
padimage = pygame.image.load(os.path.join('pad.png'))
pad = pygame.transform.scale(padimage, (10, padsize))
continuing = True
left_border = pygame.Rect(0, 0, 1, HEIGHT)
score = 0

def check_contact(the_ball, the_pad):
    global continuing
    if the_ball.colliderect(the_pad):
        continuing = True
    else:
        continuing = False

def loss():
    global continuing
    global score
    global vel
    if not continuing:
        gameovertext = endfont.render("Game Over", True, (0,0,0))
        WIN.blit(gameovertext, (WIDTH/2 - gameovertext.get_width()/2, HEIGHT/2 - gameovertext.get_height()/2))
        score = 0
        vel = 4
        ballrect = pygame.Rect(10, 300, 10, 10)
        padrect = pygame.Rect(WIDTH - 18, get_pos()[1], 10, padsize)
        pygame.display.update()
        pygame.time.delay(4000)

def get_pos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawing_window(ballrect, padrect, score, vel):
    pos = get_pos()
    #WIN.fill((255, 255, 255))  if you wanted white screen
    WIN.blit(background, (0,0))
    scoretext = gamefont.render(f"Score: {str(score)}", True, (0, 0, 0))
    WIN.blit(scoretext, (WIDTH - scoretext.get_width() - 10, 10))
    veltext = gamefont.render(f"Level: {str(vel -3)}", True, (0, 0, 0))
    WIN.blit(veltext, (10, 10))

    pygame.draw.rect(WIN, (0,0,0), left_border)
    WIN.blit(pad, (padrect.x, pos[1]))
    pygame.draw.circle(WIN, (0, 0, 255), (ballrect.x, ballrect.y), 10)
    pygame.display.update()


def game():
    #   allow ball to move
    ballrect = pygame.Rect(10, 300, 10, 10)
    padrect = pygame.Rect(WIDTH - 18, get_pos()[1], 10, padsize)
    reupdate = pygame.time.Clock()
    text = ''
    run = True
    global move
    global score
    global vel
    while run:
        reupdate.tick(FPS)  # go through this loop no more than 60 times per second
        #  check if someone cancelled out of game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #if event.type == pygame.MOUSEBUTTONDOWN:

            if event.type == pygame.MOUSEMOTION:
                ballrect = pygame.Rect(ballrect.x, ballrect.y, 10, 10)
                padrect = pygame.Rect(WIDTH - 18, get_pos()[1], 10, padsize)

        if 0 <= move < (WIDTH * 2)-60:
            if move == 0:
                ballrect.x = 10
            if move < WIDTH-30:
                ballrect.x += vel
            if ballrect.x == padrect.x:
                check_contact(ballrect, padrect)
                ballrect.x = WIDTH - 30
                if continuing:
                    score += 1
                    vel = score//3 + 4
                    clip = padrect.clip(ballrect)
                    print(padrect.y, padrect.top,padrect.bottom , ballrect.y, ballrect.top, ballrect.bottom)

                if not continuing:
                    loss()
            if WIDTH - 30 <= move < (WIDTH * 2)-60:
                ballrect.x -= vel

        move += vel
        if move >= (WIDTH * 2)-60:
            move = 0

        #   re-add things to window including color and balls
        drawing_window(ballrect, padrect, score, vel)

    pygame.quit()

game()
