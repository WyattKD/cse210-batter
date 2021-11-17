from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
class Brick(Actor):
    
    def __init__(self, x, y):
        super().__init__()
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
        self.set_position(Point(x, y))
        self._spawn(y)
        

    def set_hp(self, hp):
        self._hp = hp


    def get_hp(self):
        return self._hp

    def is_alive(self):
        if self._hp != 0:
            self.set_image(constants.IMAGE_BRICK[self._hp-1])
            return True
        else:
            return False

    def _spawn(self, y):
        y /= 35
        self._hp = randint(6 - y, 7 - y)
        if self._hp < 0:
            self._hp = 0