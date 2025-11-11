import constants

class Walls:

    def __init__(self):
        self.up_border = None
        self.down_border = None
        self.left_border = None
        self.right_border = None
        self.create_border()

    def create_border(self):
        self.up_border = constants.SCREEN_LENGTH / 2
        self.down_border = constants.SCREEN_LENGTH / -2
        self.left_border = constants.SCREEN_WIDTH / -2
        self.right_border = constants.SCREEN_WIDTH / 2

    def show_border(self):
        return

    def check_wall_collision(self, snake):
        if (
            self.left_border < snake.get_head_coords()[0] < self.right_border or
            self.up_border < snake.get_head_coords()[1] < self.down_border
        ):
            return True
        return False