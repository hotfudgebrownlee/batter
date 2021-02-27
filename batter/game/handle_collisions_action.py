import random
from game import constants
from game.action import Action
from game.point import Point

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
        bvx = ball.get_velocity().get_x()
        bvy = ball.get_velocity().get_y()
        bpx = ball.get_position().get_x()
        bpy = ball.get_position().get_y()
        ppx = paddle.get_position().get_x()
        ppy = paddle.get_position().get_y()
        for brick in bricks:
            if brick.get_text() == "*":
                if ball.get_position().equals(brick.get_position()):
                    brick.set_text(" ")
                    ball.set_velocity(Point((bvx),(bvy * -1)))
        if bpx in range(ppx,ppx + 10) and bpy == ppy:
            ball.set_velocity(Point(bvx,(bvy * -1)))
        elif bpx == 0 or bpx == constants.MAX_X:
            ball.set_velocity(Point((bvx * -1),bvy))
        elif bpy == 0:
            ball.set_velocity(Point(bvx,(bvy * -1)))
        elif bpy == constants.MAX_Y:
            del ball