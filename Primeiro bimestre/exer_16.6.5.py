

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def get_information(self):
        return self.corner, self.width, self.height


def has_collision(rect1, rect2):
    (x1, y1), w1, h1 = rect1.get_information()
    (x2, y2), w2, h2 = rect2.get_information()
    if x2 - w1 < x1 < x2 + w2 and y2 - h1 < y1 < y2 + h2:
        return True
    else:
        return False


rect1 = Rectangle((1, 3), 4, 2)
rect2 = Rectangle((2, 2), 4, 2)
collision = has_collision(rect1, rect2)
print(collision)

rect1 = Rectangle((6, 0), 4, 2)
rect2 = Rectangle((2, 2), 4, 2)
collision = has_collision(rect1, rect2)
print(collision)
