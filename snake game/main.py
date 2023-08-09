import pygame
from snake import Snake, Direction
from food import Food

# Initialize pygame and set up the game window
pygame.init()
bounds = (500, 500)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")

# Initialize snake, food, font
block_size = 20
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)
font = pygame.font.SysFont('comicsans', 30, True)

# Game loop
run = True
while run:
    pygame.time.delay(100)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Key handling for snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
        snake.steer(Direction.RIGHT)
    elif keys[pygame.K_UP]:
        snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN]:
        snake.steer(Direction.DOWN)

    # Check for food and move the snake
    snake.check_for_food(food)
    snake.move()

    # Check for collisions and display game over screen
    if snake.check_bounds() or snake.check_tail_collision():
        text = font.render('Game Over', True, (255, 255, 255))
        restart_text = font.render('Press SPACE to restart', True, (255, 255, 255))
        window.blit(text, (20, 120))
        window.blit(restart_text, (20, 180))
        pygame.display.update()
        pygame.time.delay(1000)

        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    waiting_for_restart = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        snake.reset()
                        food.respawn()
                        waiting_for_restart = False

        window.fill((0, 0, 0))
        pygame.display.update()

    else:
        # Clear the window and update the display
        window.fill((0, 0, 0))
        snake.draw(pygame, window)
        food.draw(pygame, window)

        # Display score and high score
        score_text = font.render(f'Score: {snake.score}', True, (255, 255, 255))
        window.blit(score_text, (20, 20))
        high_score_text = font.render(f'High Score: {snake.high_score}', True, (255, 255, 255))
        window.blit(high_score_text, (20, 60))

        pygame.display.update()

pygame.quit()
