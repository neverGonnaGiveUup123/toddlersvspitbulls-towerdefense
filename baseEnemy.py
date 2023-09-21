
class BaseEnemy:
    def __init__(self, checkpoints, health, speed, img) -> None:
        self.checkpoints = checkpoints
        self.health = health
        self.speed = speed
        self.sprite = img
    
    def travel(self):
        print([i for i in self.checkpoints.values()])

import json
with open('maps/playground/playgroundCheckpoints.json', 'r') as file:
    ee = json.load(file)

e = BaseEnemy(checkpoints=ee,health=10,speed=10,img=0)
e.travel()