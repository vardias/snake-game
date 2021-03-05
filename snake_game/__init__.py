""" snake game module """
import random

import pygame

X_WINDOW = 800
Y_WINDOW = 600

MOVEMENT_BLOCK = 20
SNAKE_BLOCK = 20
FRUIT_BLOCK = 20

BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (120, 200, 122)
RED_COLOR = (122, 3, 20)
BLUE_COLOR = (30, 3, 170)


class Fruit(pygame.sprite.Sprite):
    """ Implement the fruit obect """
    def __init__(self, color, width, height, group, speed):
        # pylint: disable=too-many-arguments
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.group = group
        self.speed = speed

    def random_position(self):
        """ setting a random position of the fruit """
        x_position = random.randrange(X_WINDOW - FRUIT_BLOCK - 5)
        y_position = random.randrange(Y_WINDOW - FRUIT_BLOCK - 5)
        self.rect.x = 0
        self.rect.y = 0
        self.rect = self.rect.move(x_position, y_position)

    def update(self):
        """ update the fruit """
        if pygame.sprite.spritecollide(self, self.group, False):
            self.random_position()
            self.speed.increase_game_speed()


class Wall(pygame.sprite.Sprite):  # pylint: disable=too-few-public-methods
    """ Implement the wall borders of the game """
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_position(self, x_position, y_position):
        """ setting the position of the wall """
        self.rect = self.rect.move(x_position, y_position)


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
        """ reset the position of the snake to a random position """
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
        """ move the snake block """
        self.rect = self.rect.move(x_position, y_position)

    def movement(self):
        """ movement of the snake """
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

    def check_snake_movement(self):
        """ check if the snake get outside the canvas """
        if self.rect.y >= Y_WINDOW:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = Y_WINDOW

    def update(self):
        """ update the movement """
        self.check_snake_movement()
        self.movement()


class GameSpeed():
    """ class for game speed """
    def __init__(self):
        self.game_speed = 5

    def get_game_speed(self):
        """ return the game speed value """
        return self.game_speed

    def increase_game_speed(self):
        """ increase game speed by one """
        self.game_speed += 1


def main():
    """ main loop of the game """
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((X_WINDOW, Y_WINDOW))

    speed = GameSpeed()

    wall_right = Wall(RED_COLOR, 5, Y_WINDOW)
    wall_right.set_position(0, 0)
    wall_left = Wall(RED_COLOR, 5, Y_WINDOW)
    wall_left.set_position(X_WINDOW-5, 0)
    walls = pygame.sprite.Group()
    walls.add(wall_right)
    walls.add(wall_left)

    snake = Snake(GREEN_COLOR, SNAKE_BLOCK, SNAKE_BLOCK)
    snake_body = pygame.sprite.Group()
    snake_body.add(snake)
    snake.reset_position()

    fruit = Fruit(BLUE_COLOR, FRUIT_BLOCK, FRUIT_BLOCK, snake_body, speed)
    fruit.random_position()
    fruit_block = pygame.sprite.Group()
    fruit_block.add(fruit)

    exit_flag = False
    while not exit_flag:
        clock.tick(speed.get_game_speed())
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
        fruit.update()

        # check collision
        pygame.sprite.groupcollide(snake_body, walls, True, False)

        canvas.fill(BLACK_COLOR)
        canvas.blit(snake.image, snake.rect)
        canvas.blit(wall_right.image, wall_right.rect)
        canvas.blit(wall_left.image, wall_left.rect)
        canvas.blit(fruit.image, fruit.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
