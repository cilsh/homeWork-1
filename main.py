class Cat:
    def __init__(self, kg, color, age, growth, pot):
        self.kg = kg
        self.color = color
        self.age = age
        self.growth = growth
        self.pot = pot

    def eat(self):
        self.kg += 1
        self.age += 1
        print(f'Кіт поїв і тепер важить {self.kg} кг')

    def sleep(self):
        self.age += 1
        print(f'Кіт поспав тепер йому {self.age}')

    def pryg(self):
        self.age += 1
        print(f'Кіт прагнув тепер йому {self.age}')

    def go(self):
        self.age += 1
        print(f'Кіт ходив тепер йому {self.age}')


if __name__ == '__main__':
    cat = Cat(kg=5, color='green', age=10, growth=1.5, pot='guy')
    cat.eat()
    cat.sleep()
    cat.pryg()
    cat.go()
