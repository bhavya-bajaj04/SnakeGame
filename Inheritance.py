class Car:

    def __init__(self):
        self.color = "Red"
        self.body = "Metal"

    def engine(self):
        print("250cc")


class Sport(Car):
    def __init__(self):
        super().__init__()

    def boost(self):
        print("Has Booster")

    def engine(self):
        super().engine()
        print("maximum power")


sport = Sport()
sport.boost()
sport.engine()
print(sport.color)
print(sport.body)
