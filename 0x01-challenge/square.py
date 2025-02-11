#!/usr/bin/python3
""" Contains the square class """


class square():
    """ the square class which defines a square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Called by default for initialization """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.height

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return self.height * 4

    def __str__(self):
        """ magic method that returns a peek of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
