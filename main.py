import pygame
import sys
from map import Map
from baseEnemy import BaseEnemy

pygame.init()

SCREEN = pygame.display.set_mode((500,500))
pygame.display.set_caption("TODDLERS VS PITBULLS!!!")

fps = pygame.time.Clock()

map = Map.load_map('playground')
SCREEN.blit(map[0],map[0].get_rect())

e = BaseEnemy(map[1], 10, 5, 'sprites/pitbull.jpg', SCREEN)
e.travel()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    fps.tick(30)      
    pygame.display.flip()