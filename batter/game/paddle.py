from game.actor import Actor
from game import constants
from game.point import Point
class Paddle(Actor):

    def __init__(self):
        super().__init__()
        self.set_width(constants.PADDLE_WIDTH)
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_image(constants.IMAGE_PADDLE)
        self.set_position(Point(constants.MAX_X/2 - constants.PADDLE_WIDTH/2, constants.MAX_Y - constants.PADDLE_HEIGHT))