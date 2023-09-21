class BaseTower:
    def __init__(self, range, firerate, damage, cost) -> None:
        self.range = range
        self.firerate = firerate
        self.damage = damage
        self.cost = cost
    
    def basic_life_function(self):
        pass