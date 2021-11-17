from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        bricks = cast["bricks"]
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                brick.set_hp(brick.get_hp() - 1)
                if not brick.is_alive():
                    bricks.remove(brick)
                x = ball.get_position().get_x() + constants.BALL_WIDTH/2
                y = ball.get_position().get_y() + constants.BALL_HEIGHT/2
                x2 = brick.get_position().get_x() + constants.BRICK_WIDTH/2
                y2 = brick.get_position().get_y() + constants.BRICK_HEIGHT/2
                n = x - x2
                n2 = y - y2
                if n >= 15:
                    n = 10
                elif n > 0:
                    n = 5
                elif n <= -15:
                    n = -10
                elif n < 0:
                    n = -5
                else:
                    n = 0
                if n2 >= 15:
                    n2 = 10
                elif n2 > 0:
                    n2 = 5
                elif n2 <= -15:
                    n2 = -10
                elif n2 < 0:
                    n2 = -5
                else:
                    n2 = 0
                ball.set_velocity(Point(n, n2))
        if self._physics_service.is_collision(ball, paddle):
            x = ball.get_position().get_x() + constants.BALL_WIDTH/2
            y = ball.get_position().get_y() + constants.BALL_HEIGHT/2
            x2 = paddle.get_position().get_x() + constants.PADDLE_WIDTH/2
            y2 = paddle.get_position().get_y() + constants.PADDLE_HEIGHT/2
            n = x - x2
            n2 = y - y2
            if n >= 15:
                n = 10
            elif n > 0:
                n = 5
            elif n <= -15:
                n = -10
            elif n < 0:
                n = -5
            else:
                n = 0
            if n2 >= 15:
                n2 = 10
            elif n2 > 0:
                n2 = 5
            elif n2 <= -15:
                n2 = -10
            elif n2 < 0:
                n2 = -5
            else:
                n2 = 0
            ball.set_velocity(Point(n, n2))
            