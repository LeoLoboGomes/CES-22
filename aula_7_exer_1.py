import threading
import time
import random


class Fila:
    lock = threading.RLock()
    def __init__(self):
        self.total_itams = 0
    def add(self):
        Fila.lock.acquire()
        self.total_itams += 1
        Fila.lock.release()
    def remove(self):
        Fila.lock.acquire()
        self.total_itams -= 1
        Fila.lock.release()


def producer(fila):
    for i in range(10):
        print("Um item adicionado pelo Produtor.")
        fila.add()
        time.sleep(2)


def consumer(fila):
    while True:
        print("Um item retirado pelo consumidor")
        fila.remove()
        time.sleep(2)

if __name__ == "__main__":
    fila = Fila()
    t1 = threading.Thread(target=producer, args=100)
    t2 = threading.Thread(target=consumer, args=100)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
