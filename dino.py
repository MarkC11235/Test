import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dino Run: Score - 0")

run = True

backgroundColor = (255, 255, 255)

player = [100,450]
playerVelocity = 0
playerRect = pygame.Rect(player[0], player[1], 50, 50)
grounded = True

cactus = [500,400]
cactusRect = pygame.Rect(cactus[0], cactus[1], 50, 100)

score = 0

while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and grounded:
        playerVelocity = -.75
        grounded = False
    if not grounded:
        playerVelocity += .001
    
    player[1] += playerVelocity

    if player[1] >= 450:
        grounded = True
        playerVelocity = 0

    if cactus[0] <= 0:
        cactus[0] = 500
        score+=1
    
    cactus[0] -= .2

    if player[0] <= cactus[0] + 50 and player[0] + 50 >= cactus[0] and player[1] + 50 >= cactus[1]:
        run = False

    playerRect = pygame.Rect(player[0], player[1], 50, 50)
    catusRect = pygame.Rect(cactus[0], cactus[1], 50, 100)
    win.fill(backgroundColor)
    pygame.draw.rect(win, (255,0,0), playerRect)
    pygame.draw.rect(win, (0,255,0), catusRect)
    pygame.display.set_caption("Dino Run: Score - "+str(score))
    pygame.display.update()

        

pygame.quit()