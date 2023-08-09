from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake:
    def __init__(self, block_size, bounds):
        # Initialize snake attributes
        self.length = 1
        self.direction = None
        self.body = []  # Initialize body as an empty list
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()
        self.score = 0
        self.high_score = 0

    def respawn(self):
        # Reset snake attributes when respawning
        self.body = [(20, 20)]  # Start with just the head
        self.direction = Direction.DOWN

    def draw(self, game, window):
        # Draw the snake's body segments on the window
        for segment in self.body:
            game.draw.rect(window, (0, 0, 255), (segment[0], segment[1], self.block_size, self.block_size))

    def move(self):
        # Move the snake's body segments based on the current direction
        curr_head = self.body[-1]
        if self.direction == Direction.DOWN:
            next_head = (curr_head[0], curr_head[1] + self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.UP:
            next_head = (curr_head[0], curr_head[1] - self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.RIGHT:
            next_head = (curr_head[0] + self.block_size, curr_head[1])
            self.body.append(next_head)
        elif self.direction == Direction.LEFT:
            next_head = (curr_head[0] - self.block_size, curr_head[1])
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, direction):
        # Change snake's direction while preventing opposite direction steering
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction

    def check_bounds(self):
        # Check if the snake hits the boundaries
        head = self.body[-1]
        if head[0] >= self.bounds[0] or head[1] >= self.bounds[1] or head[0] < 0 or head[1] < 0:
            return True
        return False

    def check_tail_collision(self):
        # Check if the snake collides with its own tail
        head = self.body[-1]
        has_eaten_tail = False

        for i in range(len(self.body) - 1):
            segment = self.body[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                has_eaten_tail = True

        return has_eaten_tail

    def check_for_food(self, food):
        # Check if the snake eats the food and update score and high score
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.length += 1
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
            food.respawn()

    def reset(self):
        # Reset the snake's attributes when restarting the game
        self.length = 1
        self.body = [(20, 20)]
        self.direction = Direction.DOWN
        self.score = 0
