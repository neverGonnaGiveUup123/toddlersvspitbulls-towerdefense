import pygame
import sys
from map import Map

SCREEN = pygame.display.set_mode((500,500))
pygame.display.set_caption("TODDLERS VS PITBULLS!!!")

fps = pygame.time.Clock()

map = Map.load_map('playground')
SCREEN.blit(map[0],map[0].get_rect())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    fps.tick(30)      
    pygame.display.flip()  