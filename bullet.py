import pygame
import math


class Bullet:
    def __init__(self, tank, owner, x, y, angle, speed, ball_direction):
        self.owner = owner
        self.ball_direction = ball_direction
        self.angle = angle
        self.speed = speed
        self.size = 5
        self.color = tank.color
        self.num_of_collision = 0
        self.collided = False  # Add this line
        tank_length = 45
        self.x = x + tank_length * math.cos(math.radians(self.angle)) * self.ball_direction
        self.y = y - tank_length * math.sin(math.radians(self.angle)) * self.ball_direction
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle)) * self.ball_direction
        self.y -= self.speed * math.sin(math.radians(self.angle)) * self.ball_direction
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def collision_walls(self, world):
        bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect) and not self.collided:
                self.collided = True
                bounce_sound_effect.play()
                if self.x + 5 >= tile[1].right or self.x <= tile[1].left:
                    self.angle = 180 - self.angle
                    self.num_of_collision += 1
                    self.x += self.speed * math.cos(math.radians(self.angle)) * self.ball_direction
                elif self.y >= tile[1].top or self.y <= tile[1].bottom:
                    self.angle = -self.angle
                    self.num_of_collision += 1
                    self.y -= self.speed * math.sin(math.radians(self.angle)) * self.ball_direction
                self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
            elif not tile[1].colliderect(self.rect):
                self.collided = False

    def get_num_of_collisions(self):
        return self.num_of_collision

    def hit_tank(self, tank):
        tank.health -= 1
