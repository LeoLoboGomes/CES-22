import abc


class BaseCar():

    default_acessories = ["Aparelho de Som", "Ar condicionado"]

    @abc.abstractmethod
    def get_acessories(self):
        return self.default_acessories

    """Esse metodo estatico apenas fornece a informacao dos possiveis preco dos carros"""
    @staticmethod
    def prices(car):
        if car == "Full Car":
            return 750.00
        elif car == "Basic Car":
            return 500.00


class FullCar(BaseCar):
    """O metodo seguinte "overrides" o metodo abstrato feito anteriormente"""
    def get_acessories(self):
        return self.default_acessories + ["Vidro Blindado", "Step de alta qualidade"]


class OverpricedFullCar(BaseCar):
    @classmethod
    def prices(cls):
        return 1000.00


car = FullCar()
print(car.get_acessories())
print(BaseCar.prices("Full Car"))
print(BaseCar.prices("Basic Car"))
print(OverpricedFullCar.prices())
