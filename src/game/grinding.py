import time

class Grind:
    def __init__(self, cooldown: float, income: int):
        self.cooldown = cooldown
        self.income = income
        self.last_press = 0.0

    def grind(self, coins: int) -> int:
        now = time.time()
        if now - self.last_press < self.cooldown:
            return coins
        self.last_press = now
        return coins + self.income
