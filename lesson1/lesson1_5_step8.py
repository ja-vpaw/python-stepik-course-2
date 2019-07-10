class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return True if self.capacity >= self.money + v else False

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.money += v
