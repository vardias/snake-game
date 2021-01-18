""" snake game module """
import random

import pygame

X_WINDOW = 800
Y_WINDOW = 600

BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (120, 200, 122)


class Snake(pygame.sprite.Sprite):
    """ Implement the snake """
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def reset_position(self):
        """ Reset the position of the snake to a random position """
        x_position = random.randrange(X_WINDOW - 30)
        y_position = random.randrange(Y_WINDOW - 30)
        self.rect.x = 0
        self.rect.y = 0
        self.move(x_position, y_position)

    def move(self, x_position, y_position):
        """ Move the snake """
        self.rect = self.rect.move(x_position, y_position)


def main():
    """ main loop of the game """
    pygame.init()
    canvas = pygame.display.set_mode((X_WINDOW, Y_WINDOW))
    snake = Snake(GREEN_COLOR, 20, 20)
    snake_body = pygame.sprite.Group()
    snake_body.add(snake)
    snake.reset_position()

    exit_flag = False
    while not exit_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True
            elif event.type == pygame.KEYDOWN:  # when the key is released
                if event.key == pygame.K_q:
                    exit_flag = True
                elif event.key == pygame.K_SPACE:
                    snake.reset_position()
                elif event.key == pygame.K_DOWN:
                    snake.move(0, 20)
                elif event.key == pygame.K_UP:
                    snake.move(0, -20)
                elif event.key == pygame.K_RIGHT:
                    snake.move(20, 0)
                elif event.key == pygame.K_LEFT:
                    snake.move(-20, 0)

        canvas.fill(BLACK_COLOR)
        canvas.blit(snake.image, snake.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
