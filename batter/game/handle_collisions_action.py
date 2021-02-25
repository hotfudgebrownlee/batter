import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this
    class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]
        x = ball.get_velocity().get_x()
        y = ball.get_velocity().get_y()
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                del brick
                ball.set_velocity((x * -1),(y * -1))
        if ball.get_position().equals(paddle.get_position()):
            ball.set_velocity(x,(y * -1))
        elif ball.get_position().get_x() == (0 or constants.MAX_X):
            ball.set_velocity((x * -1),y)
        elif ball.get_position().get_y() == 0:
            ball.set_velocity(x,(y * -1))
        elif ball.get_position().get_y() == constants.MAX_Y:
            del ball