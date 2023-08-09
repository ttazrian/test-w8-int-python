import random

class Food:
    def __init__(self, block_size, bounds):
        # Initialize food attributes
        self.block_size = block_size
        self.bounds = bounds
        self.x = 0
        self.y = 0
        self.respawn()

    def draw(self, game, window):
        # Draw the food on the window
        game.draw.rect(window, (0, 255, 0), (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        # Randomly respawn the food within the bounds
        blocks_in_x = self.bounds[0] // self.block_size
        blocks_in_y = self.bounds[1] // self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size
