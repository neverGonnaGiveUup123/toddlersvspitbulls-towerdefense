import json
import pygame

class Map:
    @staticmethod
    def load_map(map_name):
        with open(f'maps/{map_name}/{map_name}Checkpoints.json', 'r') as file:
            checkpoints = json.load(file)
        mapImg = pygame.image.load(f'maps/{map_name}/{map_name}Map.jpg')

        mapImg
        return mapImg, checkpoints