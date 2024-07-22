import pygame
from sys import exit

pygame.display.set_caption('mr runner')


width = 800
height  = 400

clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((width,height))


sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

test_font = pygame.font.Font('font/Pixeltype.ttf',50)
score_surface = test_font.render('My Game', False, 'Black')
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_rect.bottom -= 100
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("key up")
        
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'Grey',score_rect)
    pygame.draw.rect(screen,'Grey',score_rect,6,30)
    screen.blit(score_surface,score_rect)

    snail_rect.left -= 4
    if snail_rect.left < -100:
        snail_rect.left = width
    screen.blit(snail_surface,snail_rect)

    player_rect.left += 2
    #gravity start
    if player_rect.bottom > 300:
        player_rect.bottom = 300
    else:
        player_rect.bottom += 2
    #gravity end



    if player_rect.left > 900:
        player_rect.left = 0
    screen.blit(player_surface,player_rect)

    #update screen
    pygame.display.update()
    clock.tick(60)