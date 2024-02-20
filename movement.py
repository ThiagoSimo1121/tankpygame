import pygame
import math


class Movement:
    def __init__(self, tank, speed, keys):
        self.tank = tank
        self.speed = speed
        self.keys = keys
        self.old_x = self.tank.x
        self.old_y = self.tank.y

    def move(self, direction):
        keys = pygame.key.get_pressed()
        if keys[self.keys['left']]:
            self.tank.rotate(0.4)  # Rotate counterclockwise
        if keys[self.keys['right']]:
            self.tank.rotate(-0.4)  # Rotate clockwise
        if keys[self.keys['up']]:
            # Move the tank in the direction it is facing
            self.old_x = self.tank.x
            self.old_y = self.tank.y
            self.tank.x += self.speed * math.cos(math.radians(self.tank.angle)) * direction
            self.tank.y -= self.speed * math.sin(math.radians(self.tank.angle)) * direction
            # Update the position of the bottom center of the rectangle
            self.tank.rect = self.tank.image.get_rect(center=(self.tank.x, self.tank.y))
            self.tank.bottom_center = self.tank.rect.bottom
        if self.tank.x >= 1400:
            self.tank.x = 1400
        if self.tank.x <= 40:
            self.tank.x = 40
        if self.tank.y >= 710:
            self.tank.y = 710
        if self.tank.y <= 40:
            self.tank.y = 40

    def collide_with_walls(self, world):
        for tile in world.tile_list:
            if self.tank.rect.colliderect(tile[1]):
                # If there is a collision with a map block, move the tank back to the previous position
                self.tank.x = self.old_x
                self.tank.y = self.old_y
                # Update the position of the bottom center of the rectangle
                self.tank.rect = self.tank.image.get_rect(center=(self.tank.x, self.tank.y))
