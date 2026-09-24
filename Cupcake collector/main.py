import pygame
import random
import asyncio 

pygame.init()
pygame.mixer.init()
Screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("cupcake Collector")
clock = pygame.time.Clock()
async def main():

    player = pygame.image.load('assets/player.png').convert_alpha()
    Cupcake = pygame.image.load('assets/Cupcake.png').convert_alpha()

    Cup = []


    for m in range(10):
        mx = random.randint(50, 900)
        my = random.randint(50, 100)
        Cup.append(pygame.Rect(mx, my, 16, 16))


    CupVelocity = [0 for m in range(10)]

    plect = player.get_rect()
    plect.x = 900 
    plect.y =  400

    Pseed = 2 #movment speed
    Pjump = 30
    velocity_y = Pjump
    gravity = 2
    jumping = False
    plect.x = 150
    plect.y = 100


    pygame.mixer.music.load('assets/game music.ogg')
    pygame.mixer.music.set_volume(.5)
    running = True

    platforms = [
        pygame.Rect(0, 450, 1000, 50),   
        pygame.Rect(100, 400, 250, 20),  
        pygame.Rect(450, 300, 250, 20), 
        pygame.Rect(800, 100, 300, 50)  
    ]

    cool = 1000 # cooldown btween jumps
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


        plect.y += gravity

        if keys[pygame.K_LEFT]:
            plect.x -= Pseed

        if keys[pygame.K_RIGHT]:
            plect.x += Pseed

        if keys[pygame.K_UP]:
            jumping = True
        
        if jumping:
            plect.y -= velocity_y
            velocity_y -= gravity
            if velocity_y < -Pjump:
                jumping = False
                velocity_y = Pjump

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

                plect.bottom = platform.top


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
            running = False
  
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
        await asyncio.sleep(0)
asyncio.run(main())
pygame.quit()


