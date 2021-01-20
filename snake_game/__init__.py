""" snake game module """
import random

import pygame

X_WINDOW = 800
Y_WINDOW = 600

MOVEMENT_BLOCK = 20
SNAKE_BLOCK = 20
CLOCK_TICK = 10

BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (120, 200, 122)


class Snake(pygame.sprite.Sprite):  # pylint: disable=R0902
    """ Implement the snake class """
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.left_movement = None
        self.right_movement = None
        self.up_movement = None
        self.down_movement = None

    @property
    def left_movement(self):
        """ getter function for left_movement """
        return self._left_movement

    @property
    def right_movement(self):
        """ getter function for right_movement """
        return self._right_movement

    @property
    def up_movement(self):
        """ getter function for up_movement """
        return self._up_movement

    @property
    def down_movement(self):
        """ getter function for down_movement """
        return self._down_movement

    @left_movement.setter
    def left_movement(self, value):
        """ setter function for left_movement """
        self._left_movement = value
        self._right_movement = False
        self._up_movement = False
        self._down_movement = False

    @right_movement.setter
    def right_movement(self, value):
        """ setter function for right_movement """
        self._right_movement = value
        self._left_movement = False
        self._up_movement = False
        self._down_movement = False

    @up_movement.setter
    def up_movement(self, value):
        """ setter function for up_movement """
        self._up_movement = value
        self._left_movement = False
        self._right_movement = False
        self._down_movement = False

    @down_movement.setter
    def down_movement(self, value):
        """ setter function for down_movement """
        self._down_movement = value
        self._left_movement = False
        self._right_movement = False
        self._up_movement = False

    def reset_position(self):
        """ Reset the position of the snake to a random position """
        x_position = random.randrange(X_WINDOW - SNAKE_BLOCK)
        y_position = random.randrange(Y_WINDOW - SNAKE_BLOCK)
        movement_choice = random.randrange(0, 4)
        if movement_choice == 0:
            self.down_movement = True
        elif movement_choice == 1:
            self.up_movement = True
        elif movement_choice == 2:
            self.right_movement = True
        else:
            self.left_movement = True
        self.rect.x = 0
        self.rect.y = 0
        self.move(x_position, y_position)

    def move(self, x_position, y_position):
        """ Move the snake block """
        self.rect = self.rect.move(x_position, y_position)

    def movement(self):
        """ Movement of the snake """
        if self._right_movement:
            x_pos = MOVEMENT_BLOCK
            y_pos = 0
        elif self.left_movement:
            x_pos = -MOVEMENT_BLOCK
            y_pos = 0
        elif self.up_movement:
            x_pos = 0
            y_pos = -MOVEMENT_BLOCK
        elif self.down_movement:
            x_pos = 0
            y_pos = MOVEMENT_BLOCK
        else:
            print('There is no movement')

        self.move(x_pos, y_pos)

    def update(self):
        """ update the movement """
        self.movement()


def main():
    """ main loop of the game """
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((X_WINDOW, Y_WINDOW))
    snake = Snake(GREEN_COLOR, SNAKE_BLOCK, SNAKE_BLOCK)
    snake_body = pygame.sprite.Group()
    snake_body.add(snake)
    snake.reset_position()

    exit_flag = False
    while not exit_flag:
        clock.tick(CLOCK_TICK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True
            elif event.type == pygame.KEYDOWN:  # when the key is released
                if event.key == pygame.K_q:
                    exit_flag = True
                elif event.key == pygame.K_SPACE:
                    snake.reset_position()
                elif event.key == pygame.K_DOWN:
                    snake.down_movement = True
                elif event.key == pygame.K_UP:
                    snake.up_movement = True
                elif event.key == pygame.K_RIGHT:
                    snake.right_movement = True
                elif event.key == pygame.K_LEFT:
                    snake.left_movement = True

        snake_body.update()
        canvas.fill(BLACK_COLOR)
        canvas.blit(snake.image, snake.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
