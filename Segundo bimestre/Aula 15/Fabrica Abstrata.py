import abc


class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buy(self):
        pass


class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill(self):
        pass


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_color(self):
        pass

    @abc.abstractmethod
    def get_car(self):
        pass


class Audi(Car):
    def buy(self):
        print("Dentro do metodo Audi::buy().")


class Mercedes(Car):
    def buy(self):
        print("Dentro do metodo Mercedes::buy().")


class Red(Color):
    def fill(self):
        print("Dentro do metodo Red::fill().")


class Green(Color):
    def fill(self):
        print("Dentro do metodo Green::fill().")


class CarFactory(AbstractFactory):
    def get_car(self, car_type):
        if car_type == None:
            return None

        if car_type == "AUDI":
            return Audi()
        elif car_type == "MERCEDES":
            return Mercedes()

        return None

    def get_color(self):
        return None


class ColorFactory(AbstractFactory):
    def get_color(self, color_type):
        if color_type == None:
            return None

        if color_type == "RED":
            return Red()
        elif color_type == "GREEN":
            return Green()

        return None

    def get_car(self):
        return None


class FactoryProducer:
    @staticmethod
    def get_factory(choice):
        if choice == "CAR":
            return CarFactory()
        elif choice == "COLOR":
            return ColorFactory()
        return None


if __name__ == '__main__':
    car_factory = FactoryProducer.get_factory("CAR")

    car1 = car_factory.get_car("AUDI");
    car1.buy()

    shape2 = car_factory.get_car("MERCEDES");
    shape2.buy()

    color_factory = FactoryProducer.get_factory("COLOR");

    color1 = color_factory.get_color("RED");
    color1.fill()

    color2 = color_factory.get_color("GREEN");
    color2.fill()
