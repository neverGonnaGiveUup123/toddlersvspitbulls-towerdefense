import pygame

class BaseEnemy:
    def __init__(self, checkpoints, health, speed, img, screen):
        self.checkpoints = checkpoints
        self.health = health
        self.speed = speed
        self.sprite = pygame.image.load(img)
        self.screen = screen
    
    def travel(self):
        print([i for i in self.checkpoints.values()])
        self.screen.blit(self.sprite, (50,50))