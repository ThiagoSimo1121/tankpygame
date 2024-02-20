import pygame
import math


class Bullet:
    def __init__(self, dono, x, y, angulo, velocidade, direção_bola):
        self.dono = dono
        self.direção_bola = direção_bola
        self.angulo = angulo
        self.velocidade = velocidade
        self.size = 5
        self.color = (0, 0, 0)  # Cor branca
        self.num_of_collision = 0
        self.collided = False  # Adicione esta linha
        comprimento_tank = 45
        self.x = x + comprimento_tank * math.cos(math.radians(self.angulo)) * self.direção_bola
        self.y = y - comprimento_tank * math.sin(math.radians(self.angulo)) * self.direção_bola
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def mover(self):
        self.x += self.velocidade * math.cos(math.radians(self.angulo)) * self.direção_bola
        self.y -= self.velocidade * math.sin(math.radians(self.angulo)) * self.direção_bola
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, tela):
        pygame.draw.rect(tela, self.color, self.rect)
        pygame.draw.rect(tela, (255, 255, 255), self.rect, 1)

    def collision_screen(self):
        if self.x >= 1440 or self.x <= 0:
            self.angulo = 180 - self.angulo
        if self.y >= 750 or self.y <= 0:
            self.angulo = -self.angulo

    def collision_walls(self, world):
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect) and not self.collided:
                self.collided = True
                if self.x + 5 >= tile[1].right or self.x <= tile[1].left:
                    self.angulo = 180 - self.angulo
                    self.num_of_collision += 1
                    self.x += self.velocidade * math.cos(math.radians(self.angulo)) * self.direção_bola
                elif self.y >= tile[1].top or self.y <= tile[1].bottom:
                    self.angulo = -self.angulo
                    self.num_of_collision += 1
                    self.y -= self.velocidade * math.sin(math.radians(self.angulo)) * self.direção_bola
                self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
            elif not tile[1].colliderect(self.rect):
                self.collided = False

    def get_num_of_collisions(self):
        return self.num_of_collision

    def hit_tank(self, tank):
        tank.vida -= 1
