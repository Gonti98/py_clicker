import time

class Grind:
    def __init__(self, cooldown: float, income: int):
        self.cooldown = cooldown
        self.income = income
        self.last_press = 0.0

    @property
    def available(self) -> bool:
        return time.time() - self.last_press >= self.cooldown

    def click(self, coins: int) -> int:
        if not self.available:
            return coins
        self.last_press = time.time()
        return coins + self.income
