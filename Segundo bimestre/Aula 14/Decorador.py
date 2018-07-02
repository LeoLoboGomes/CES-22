import abc

class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def assemble(self):
        pass


class BasicCar(Car):
    def assemble(self):
        print("Carro Basico.")


class CarDecorator(Car):
    def __init__(self, car):
        self.car = car

    def assemble(self):
        self.car.assemble()


class SportsCar(CarDecorator):
    def __init__(self, car):
        super(SportsCar, self).__init__(car)

    def assemble(self):
        super(SportsCar, self).assemble()
        print("Adicionando acessorios de carro esportivo.")


class LuxuryCar(CarDecorator):
    def __init__(self, car):
        super(LuxuryCar, self).__init__(car)

    def assemble(self):
        super(LuxuryCar, self).assemble()
        print("Adicionando acessorios de carro de luxo.")


if __name__ == '__main__':
    sports_car = SportsCar(BasicCar())
    sports_car.assemble()
    print("-----")

    sports_luxury_car = SportsCar(LuxuryCar(BasicCar()))
    sports_luxury_car.assemble()