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
from typing import List
import time

@functools.total_ordering
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
    if low > high:
        raise ValueError('low cannot be higher than high')
    if low <= x <= high:
        return x
    if x < low:
        return low
    if x > high:
        return high
    return None
    # You can use doctest to test for exceptions. You can see an example above.
    # You might see it again later. Note that you need to also write
    # "doctest: +IGNORE_EXCEPTION_DETAIL".


class Color:
    """ This is the Color class used to color slimes. """

    def __init__(self, r: int = 0, g: int = 0, b: int = 0) -> None:
        """ Creates a color coordinate based on RGB values. """
        self.__r = clamp(r, 0, 255)
        self.__g = clamp(g, 0, 255)
        self.__b = clamp(b, 0, 255)

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
        self.__r = clamp(new_r, 0, 255)

    @property
    def g(self):
        """ Sets the red component of the color. Don't forget to clamp!

                >>> color = Color(0, 0, 0)
                >>> color.g = 20
                >>> color.g
                20
                >>> color.g = -1
                >>> color.g
                0
                >>> color.g = 999
                >>> color.g
                255
        """
        return self.__g

    @g.setter
    def g(self, new_g):
        self.__g = clamp(new_g, 0, 255)

    @property
    def b(self):
        """ Sets the red component of the color. Don't forget to clamp!
            >>> color = Color(0, 0, 0)
            >>> color.b = 20
            >>> color.b
            20
            >>> color.b = -1
            >>> color.b
            0
            >>> color.b = 999
            >>> color.b
            255
        """
        return self.__b

    @b.setter
    def b(self, new_b):
        self.__b = clamp(new_b, 0, 255)

    def __str__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def __eq__(self: 'Color', other: 'Color'):
        """ A color is equal iff all three components match.

        >>> col_1 = Color(100,100,100)
        >>> col_2 = Color(100,100,100)
        >>> col_1 == col_2
        True
        """
        return self.__r == other.r and self.__g == other.g and self.__b == other.b

    # When a class wants to type-hint itself, you must add quotes around the
    # class name (turning it into a string). Don't worry, as there is actually
    # no type enforcement (from Python's perspective) anyway.


def mix_colors(color1, color2, weight1=1, weight2=1):
    """ Mix colors, with given weights. """
    total_mass = weight1 + weight2
    r = int(((color1.r * weight1) + (color2.r * weight2)) / total_mass)
    g = int(((color1.g * weight1) + (color2.g * weight2)) / total_mass)
    b = int(((color1.b * weight1) + (color2.b * weight2)) / total_mass)
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
        return self.__color

    @color.setter
    def color(self, new_color):
        if 0 <= new_color.r <= 255 and 0 <= new_color.g <= 255 and 0 <= new_color.b <= 255:
            self.__color = new_color

    @property
    def mass(self):
        """ Mass defines how heavy a slime is, and who will become the primary
            parent (P1) in case of breeding. Must be >= 0.
        """
        return self.__mass

    @mass.setter
    def mass(self, new_mass):
        if new_mass >= 0:
            self.__mass += int(new_mass * 0.9)

    @property
    def volume(self):
        """ Volume defines how big a slime is, and whether it will fit in a box.
            Must be >= 0.
        """
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        if new_volume >= 0:
            self.__volume = new_volume

    def eat(self, food_mass: int = 0, food_type="L"):
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
            self.__mass += int(food_mass * 0.9)
            self.__volume += int(food_mass * 0.9)
        elif food_type == "S":
            self.__mass += int(food_mass * 0.4)
        else:
            raise ValueError("food type must be L or S")

    def split(self, copies: int) -> List['Slime']:
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
        if copies == 1:
            return [self]
        if copies > 1:
            mass = copy.copy(self.__mass)
            volume = copy.copy(self.__volume)
            return [Slime(mass // copies, volume // copies, self.__color) for _ in range(copies)]
        if copies < 1:
            raise ValueError("Copies must be larger than 0.")
        return None

    def __eq__(self, other):
        return self.__mass == other.mass and self.__volume == other.volume

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
        return Slime(self.__mass + other.mass, self.volume + other.volume,
                     mix_colors(self.__color, other.color, self.__mass, other.mass))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Use the following line INSTEAD if you want to print all tests anyway.
    doctest.testmod(verbose=True)
