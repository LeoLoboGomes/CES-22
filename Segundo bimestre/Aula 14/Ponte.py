import abc

class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill_color(self):
        pass

class Brand(metaclass=abc.ABCMeta):
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def color_it(self):
        pass

class Mercedes(Brand):
    def __init__(self, color):
        super(Mercedes, self).__init__(color)

    def color_it(self):
        print("O carro da marca Mercedes tem cor ", end="")
        self.color.fill_color()

class Audi(Brand):
    def __init__(self, color):
        super(Audi, self).__init__(color)

    def color_it(self):
        print("O carro da marca Audi tem cor ", end="")
        self.color.fill_color()

class RedColor(Color):
    def fill_color(self):
        print("Vermelha")

class BlueColor(Color):
    def fill_color(self):
        print("Azul")

if __name__ == '__main__':
    s1 = Mercedes(RedColor())
    s1.color_it()

    s2 = Audi(BlueColor())
    s2.color_it()