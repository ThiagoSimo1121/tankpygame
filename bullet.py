import pygame
import math

class Bullet:
    def __init__(self, dono ,x, y, angulo, velocidade, direção_bola):
        self.dono = dono
        self.direção_bola = direção_bola
        self.angulo = angulo
        self.velocidade = velocidade
        self.size = 5
        self.color = (255, 255, 255)  # Cor branca
        # Ajusta a posição inicial da bala
        comprimento_tank = 45  # Substitua pelo comprimento real do seu tanque
        self.x = x + comprimento_tank * math.cos(math.radians(self.angulo)) * self.direção_bola
        self.y = y - comprimento_tank * math.sin(math.radians(self.angulo)) * self.direção_bola
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def mover(self):
        self.x += self.velocidade * math.cos(math.radians(self.angulo)) * self.direção_bola
        self.y -= self.velocidade * math.sin(math.radians(self.angulo)) * self.direção_bola
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, tela):
        pygame.draw.rect(tela, self.color, self.rect)

    def collision(self):
        if self.x >= 1440 or self.x <= 0:
            self.angulo = 180 - self.angulo  # Reflete o ângulo na direção x
        if self.y >= 750 or self.y <= 0:
            self.angulo = -self.angulo  # Reflete o ângulo na direção y

