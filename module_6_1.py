class Animal():
    alive = True  # (живой)- (атрибут класса)
    fed = False  # (накормленный)- (атрибут класса)

    def __init__(self, name):
        self.name = name    #(индивидуальное название каждого животного)- (атрибут экземпляра)


    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant():
    edible = False  #(съедобность)- (атрибут класса)
    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    edible = True #(индивидуальное название каждого растения)- (атрибут экземпляра)

class Flower(Plant):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
