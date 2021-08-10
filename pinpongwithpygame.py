import pygame, emoji
import unicodedata
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
gamefont = pygame.font.SysFont('comicsans', 15)
endfont = pygame.font.SysFont('comicsans', 25)

background = pygame.transform.scale(pygame.image.load(os.path.join('background.png')), (WIDTH, HEIGHT))
pygame.display.set_caption('Pingpong')
FPS = 60    #  frames per second
vel = 4     #   how qickly the ball is moving
move = 0   # where ball starts off then you add velocity to move forward
padsize = 100
padimage = pygame.image.load(os.path.join('pad.png'))
pad = pygame.transform.scale(padimage, (10, padsize))
continuing = True
borderwidth = 1.0
left_border = pygame.Rect(0, 0, borderwidth, HEIGHT)
top_border = pygame.Rect(0, 0, WIDTH, borderwidth)
bottom_border = pygame.Rect(0, HEIGHT-borderwidth, WIDTH, borderwidth)
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

def moveyaxis(angle, ballrect):
    pass

def drawing_window(ballrect, padrect, score, vel, paused, lost):

    pos = get_pos()

    #WIN.fill((255, 255, 255))  if you wanted white screen
    WIN.blit(background, (0,0))
    scoretext = gamefont.render(f"Score: {str(score)}", True, (0, 0, 0))
    WIN.blit(scoretext, (WIDTH - scoretext.get_width() - 10, 10))
    veltext = gamefont.render(f"Level: {str(vel -3)}", True, (0, 0, 0))
    WIN.blit(veltext, (10, 10))
    pygame.draw.rect(WIN, (0, 0, 0), left_border)
    pygame.draw.rect(WIN, (0, 0, 0), top_border)
    pygame.draw.rect(WIN, (0, 0, 0), bottom_border)
    WIN.blit(pad, (padrect.x, pos[1]))
    pygame.draw.circle(WIN, (0, 0, 255), (ballrect.x, ballrect.y), 10)
    if paused:
        pause_text = endfont.render('PAUSED', True, (255, 0, 0))
        WIN.blit(pause_text, ((WIDTH - pause_text.get_width())/2, (HEIGHT - pause_text.get_height()) / 2))
    if lost:
        pause_text = endfont.render('X  GAME OVER  X', True, (255, 0, 0))
        WIN.blit(pause_text, ((WIDTH - pause_text.get_width()) / 2, (HEIGHT - pause_text.get_height()) / 2))
    pygame.display.update()


def game():
    #   allow ball to move
    ballrect = pygame.Rect(10, 300, 10, 10)
    padrect = pygame.Rect(WIDTH - 18, get_pos()[1], 10, padsize)
    reupdate = pygame.time.Clock()
    text = ''
    angle = 0
    paused = False
    lost = False

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_SPACE :  # Pausing/Unpausing
                    paused = not paused
            if event.type == pygame.MOUSEMOTION and not paused :
                ballrect = pygame.Rect(ballrect.x, ballrect.y, 10, 10)
                padrect = pygame.Rect(WIDTH - 18, get_pos()[1], 10, padsize)
        if not paused and not lost:
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
                        print("\npad:", padrect.top,padrect.bottom ,"\tball:", ballrect.top, ballrect.bottom)

                    if not continuing:
                        lost = True
                if WIDTH - 30 <= move < (WIDTH * 2)-60:
                    ballrect.x -= vel

            move += vel
            if move >= (WIDTH * 2)-60:
                move = 0

            #   re-add things to window including color and balls
        drawing_window(ballrect, padrect, score, vel, paused, lost)




    pygame.quit()

game()
