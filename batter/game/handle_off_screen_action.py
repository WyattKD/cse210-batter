from game import constants
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):

    def __init__(self):
        super().__init__()

    def execute(self, cast):
        self._handle_ball(cast)
        self._handle_paddle(cast)

    def _handle_ball(self, cast):
        ball = cast["balls"][0]
        current_position = cast["balls"][0].get_position()
        x = current_position.get_x()
        y = current_position.get_y()
        current_velocity = cast["balls"][0].get_velocity()
        dx = current_velocity.get_x()
        dy = current_velocity.get_y()
        if x >= constants.MAX_X - constants.BALL_WIDTH or x <= 0:
            dx *= -1
        if y <= 0:
            dy *= -1
        if y >= constants.MAX_Y - constants.BALL_HEIGHT/2:
            cast["balls"].remove(ball)
        else:
            new_velocity = Point(dx, dy)
            cast["balls"][0].set_velocity(new_velocity)

    def _handle_paddle(self, cast):
        current_position = cast["paddle"][0].get_position()
        current_x = current_position.get_x()
        if current_x >= constants.MAX_X - constants.PADDLE_WIDTH:
            cast["paddle"][0].set_position(Point(constants.MAX_X - (constants.PADDLE_WIDTH + 15), constants.MAX_Y - constants.PADDLE_HEIGHT))
        if current_x <= 15:
            cast["paddle"][0].set_position(Point(15, constants.MAX_Y - constants.PADDLE_HEIGHT))