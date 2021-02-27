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
        if bpx in range(ppx,ppx + 11) and bpy == ppy:
            ball.set_velocity(Point(bvx,(bvy * -1)))
        elif bpx == 1 or bpx == int(constants.MAX_X-1):
            ball.set_velocity(Point((bvx * -1),bvy))
            ball.get_position().set_y(bpy + 1)
        elif bpy == 0:
            ball.set_velocity(Point(bvx,(bvy * -1)))
            ball.get_position().set_y(bpy + 1)
        elif bpy == int(constants.MAX_Y):
            ball.set_velocity(Point(0,0))
            x = int(constants.MAX_X / 2)-5
            y = int(constants.MAX_Y / 2)
            ball.set_position(Point(x,y))
            ball.set_text("Game Over")
