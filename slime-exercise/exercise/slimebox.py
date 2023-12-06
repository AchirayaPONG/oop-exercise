"""
This module is a story about you and a box of slimes.

01219114 Computer Programming
Week 9, Long Program Assignment: Slime Box (slimebox module)
(C) 2022 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

# Your instructions:
# If there's any "pass", implement it.
# If there's any "TODO", follow the instructions.
# For any logic concerns, read the main problem statement.
# Resolve any remaining doctest and program errors and you should be fine.

import functools
import copy

def clamp(x: int, low: int, high: int) -> int:
    """ Clamps value x so it is within the [low, high] range.

        Must raise ValueError as written in doctest when low > high.

        >>> clamp(10, 0, 100)
        10
        >>> clamp(999, 0, 100)
        100
        >>> clamp(-10, 0, 10)
        0
        >>> clamp(100, 90, 0) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
          ...
        ValueError: 'low cannot be higher than high'

    """

    # You can use doctest to test for exceptions. You can see an example above.
    # You might see it again later. Note that you need to also write
    # "doctest: +IGNORE_EXCEPTION_DETAIL".

    pass

class Color:
    """ This is the Color class used to color slimes. """

    def __init__(self, r: int = 0, g: int = 0, b: int = 0) -> None:
        """ Creates a color coordinate based on RGB values. """
        pass


    @property
    def r(self):
        """ Sets the red component of the color. Don't forget to clamp!

        >>> color = Color(0, 0, 0)
        >>> color.r = 20
        >>> color.r
        20
        >>> color.r = -1
        >>> color.r
        0
        >>> color.r = 999
        >>> color.r
        255
        """
        return self.__r

    @r.setter
    def r(self, new_r):
        pass

    # TODO: Implement "g" and "b" in the same way.

    def __str__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def __eq__(self: 'Color', other: 'Color'):
        """ A color is equal iff all three components match.

        >>> col_1 = Color(100,100,100)
        >>> col_2 = Color(100,100,100)
        >>> col_1 == col_2
        True
        """
        pass

    # When a class wants to type-hint itself, you must add quotes around the
    # class name (turning it into a string). Don't worry, as there is actually
    # no type enforcement (from Python's perspective) anyway.

def mix_colors(color1, color2, weight1=1, weight2=1):
    """ Mix colors, with given weights. """

    pass
    return Color(r, g, b)

class Slime:
    """ Slimes are interesting creatures and they are defined by this class. """

    def __init__(self, mass: int = 0, volume: int = 0, color: Color = Color(0, 0, 0)):
        self.__mass = mass
        self.__volume = volume
        self.__color = color

    @property
    def color(self):
        """ Color property represents the color of the slime. """
        pass

    @color.setter
    def color(self, new_color):
        pass

    @property
    def mass(self):
        """ Mass defines how heavy a slime is, and who will become the primary
            parent (P1) in case of breeding. Must be >= 0.
        """
        pass

    @mass.setter
    def mass(self, new_mass):
        pass

    @property
    def volume(self):
        """ Volume defines how big a slime is, and whether it will fit in a box.
            Must be >= 0.
        """
        pass

    @volume.setter
    def volume(self, newVolume):
        pass

    def eat(self, food_mass: int = 0, food_type = "L"):
        """ The slime eats and grows.

            If liquid food, mass is increased by 90% of food mass, and volume
            is also increased by the same amount.
            If solid food, only the mass is increased by 40% of food mass.
            Liquid food is the default.
            Raises ValueError("food type must be L or S") if food type
            is invalid.

            >>> s = Slime(100, 100)
            >>> s.eat(100)
            >>> s.mass
            190
            >>> s.volume
            190
            >>> s.eat(100, "S")
            >>> s.mass
            230
            >>> s.volume
            190
        """
        if food_type == "L":
            pass
        elif food_type == "S":
            pass
        else:
            raise ValueError("food type must be L or S")

    def split(self, copies: int) -> list['Slime']:
        """ Splits a slime into many copies.

            If copies > 1, return a list of many slimes. None of them are self.
            If copies == 1, return this slime itself in a list.
            If copies < 1, raise ValueError("Copies must be larger than 0.")

            >>> s = Slime(100, 10)
            >>> print(str(s.split(10)[0]))
            Slime(10, 1, Color(0, 0, 0))
            >>> print(str(s.split(10)[1]))
            Slime(10, 1, Color(0, 0, 0))
            >>> t = s.split(1)
            >>> t[0] is s
            True
            >>> t = s.split(0) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            ValueError: 'Copies must be larger than 0.'
        """
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        return f"Slime({self.mass}, {self.volume}, {self.color})"

    def __add__(self, other) -> 'Slime':
        """ When combining slimes, the convention is to use the + operator.

        >>> slime1 = Slime(50, 20, Color(0, 20, 0))
        >>> slime2 = Slime(50, 10, Color(10, 0, 10))
        >>> print(str(slime1 + slime2))
        Slime(100, 30, Color(5, 10, 5))
        >>> slime3 = Slime(1, 1, Color(0, 0, 0))
        >>> slime4 = Slime(9, 1, Color(100, 100, 100))
        >>> print(str(slime3 + slime4))
        Slime(10, 2, Color(90, 90, 90))
        """
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Use the following line INSTEAD if you want to print all tests anyway.
    # doctest.testmod(verbose = True)

