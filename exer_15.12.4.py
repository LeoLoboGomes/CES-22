class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def get_line_to(self, point):
        a = (self.y - point.y)/(self.x - point.x)
        b = self.y - a*self.x
        return (a,b)
