from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        # paddle = cast["paddle"][0]
        # balls = cast["balls"]
        # bricks = cast["bricks"]
        # balls_to_remove = []
            
        # for ball in balls:
        #     self._handle_ball_wall_collision(ball)
        #     self._handle_ball_paddle_collision(ball, paddle)
        #     self._handle_ball_brick_collision(ball, bricks)
        #     self._handle_ball_base_collision(ball, balls_to_remove)
        #     self._handle_paddle_limit_collision(paddle)
            
        # for ball in balls_to_remove:
        #     balls.remove(ball)
        pass

    def _handle_ball_wall_collision(self, ball):
        ball_x = ball.center_x
        ball_y = ball.center_y

        # Check for bounce on walls
        if ball_x <= 0 or ball_x >= constants.MAX_X:
            ball.bounce_vertical()

        if ball_y >= constants.MAX_Y:
            ball.bounce_horizontal()
        
        if not constants.BALLS_CAN_DIE and ball_y <= 0:
            ball.bounce_horizontal()
    
    def _handle_ball_paddle_collision(self, ball, paddle):
        # This makes use of the `Sprite` functionality
        if paddle.collides_with_sprite(ball):
            # Ball and paddle collide!
            ball.bounce_horizontal()

    def _handle_ball_brick_collision(self, ball, bricks):
        brick_to_remove = None
        for brick in bricks:
            # This makes use of the `Sprite` functionality
            if ball.collides_with_sprite(brick):
                ball.bounce_horizontal()
                brick_to_remove = brick
        if brick_to_remove != None:
            bricks.remove(brick_to_remove)

    def _handle_ball_base_collision(self, ball, balls_to_remove):
        if constants.BALLS_CAN_DIE and ball.center_y < 0:
            balls_to_remove.append(ball)
    
    def _handle_paddle_limit_collision(self, paddle):
        if paddle.bottom < 10:
            paddle.bottom = 10
        elif paddle.top > 200:
            paddle.top = 200
        
        if paddle.left < 0:
            paddle.left = 0
        elif paddle.right > constants.MAX_X:
            paddle.right = constants.MAX_X 
    