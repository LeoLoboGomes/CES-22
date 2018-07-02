import abc

class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buy(self, color):
        pass

class Audi(Car):
    def buy(self, color):
        print("Comprando Audi com cor " + color)

class Mercedes(Car):
    def buy(self, color):
        print("Comprando Mercedes com cor " + color)

class Buying(Car):
    def __init__(self):
        self.car = []

    def buy(self, color):
        for sh in self.car:
            sh.buy(color)

    def add(self, sh):
        self.car.append(sh)

    def remove(self, sh):
        self.car.remove(sh)

    def clear(self):
        print("Clearing all the shapes from drawing")
        self.car = []

if __name__ == '__main__':
    Au1 = Audi()
    Au2 = Audi()
    Mer = Mercedes()

    buying = Buying()
    buying.add(Au1)
    buying.add(Au2)
    buying.add(Mer)

    buying.buy("Red")

    buying.clear()

    buying.add(Au1)
    buying.add(Mer)
    buying.buy("Green")