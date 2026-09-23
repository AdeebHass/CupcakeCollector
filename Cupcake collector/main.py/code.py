import pygame
import random

pygame.init()
pygame.mixer.init()
Screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("badaba")
clock = pygame.time.Clock()

player = pygame.image.load('player.png').convert_alpha()
Cupcake = pygame.image.load('Cupcake.png').convert_alpha()

Cup = []


for m in range(10):
    mx = random.randint(50, 900)
    my = random.randint(50, 100)
    Cup.append(pygame.Rect(mx, my, 16, 16))


CupVelocity = [0 for m in range(10)]

plect = player.get_rect()

Pseed = 2
Pjump = 100
velocity_y = 0
gravity = 1

plect.x = 150
plect.y = 100


pygame.mixer.music.load('game music.mp3')

running = True

platforms = [
    pygame.Rect(0, 450, 1000, 50),   
    pygame.Rect(100, 400, 250, 20),  
    pygame.Rect(450, 300, 250, 20)   
]

cool = 1000
Jumpbefore = 0


score = 0
font = pygame.font.Font(None, 36)

color = (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
)
pygame.mixer.music.play(-1)

while running:
    Screen.fill((20, 24, 40))

    for rect in platforms:
        pygame.draw.rect(Screen, color, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ct = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()


    velocity_y += gravity
    plect.y += velocity_y

    if keys[pygame.K_LEFT]:
        plect.x -= Pseed

    if keys[pygame.K_RIGHT]:
        plect.x += Pseed

    if keys[pygame.K_UP]:
        if ct - Jumpbefore >= cool:
            plect.y -= Pjump
            Jumpbefore = ct

    if keys[pygame.K_DOWN]:
        plect.y += Pseed

    if plect.top < 0:
        plect.top = 0

    if plect.right > 1000:
        plect.right = 1000

    if plect.left < 0:
        plect.left = 0

    for platform in platforms:

        if plect.colliderect(platform):

            if velocity_y > 0:
                plect.bottom = platform.top
                velocity_y = 0


    for i in range(len(Cup)):

        cup = Cup[i]

        CupVelocity[i] += gravity
        cup.y += CupVelocity[i]

        for platform in platforms:

            if cup.colliderect(platform) and CupVelocity[i] > 0:
                cup.bottom = platform.top
                CupVelocity[i] = 0

        if plect.colliderect(cup):

            score += 1

            cup.y = -100

  
            CupVelocity[i] = 0
    if score == 20:
        win_text = font.render("YOU WIN", True, (255, 255, 255))
        Screen.blit(win_text, (100, 100))
        pygame.display.flip()
        pygame.time.delay(3000) 
        running = Falsealse
  
    Screen.blit(player, (plect.x, plect.y))

  
    for cup in Cup:
        Screen.blit(Cupcake, cup.topleft)

    
    score_text = font.render(
        "Score: " + str(score),
        True,
        (255, 255, 255)
    )

    Screen.blit(score_text, (20, 20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

