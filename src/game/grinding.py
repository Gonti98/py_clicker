import time

class Grind:
    def __init__(self, cooldown: float, income: int):
        self.cooldown = cooldown
        self.income = income
        self.last_press = 0.0

    def grind(self, points: int) -> int:
        now = time.time()
        if now - self.last_press < self.cooldown:
            return points
        self.last_press = now
        return points + self.income
