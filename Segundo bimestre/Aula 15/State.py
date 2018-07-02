import abc

class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def motion(self):
        pass


class MovingState(State):
    def motion(self):
        return "Esta em movimento"


class StationaryState(State):
    def motion(self):
        return "Esta parado"


class Car(State):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def motion(self):
        return self.state.motion()


if __name__ == '__main__':
    car = Car(MovingState())
    print(car.motion())

    car.set_state(StationaryState())
    print(car.motion())
