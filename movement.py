import pygame
import math
from tank import Tank

class Movement:
    def __init__(self, tank, velocidade, teclas):
        self.tank = tank
        self.velocidade = velocidade
        self.teclas = teclas

    def mover(self, direção):
        keys = pygame.key.get_pressed()
        if keys[self.teclas['esquerda']]:
            self.tank.rotacionar(0.2)  # Gira no sentido anti-horário
        if keys[self.teclas['direita']]:
            self.tank.rotacionar(-0.2)  # Gira no sentido horário
        if keys[self.teclas['cima']]:
            # Move o tanque na direção que está apontando
            self.tank.x += self.velocidade * math.cos(math.radians(self.tank.angulo)) * direção
            self.tank.y -= self.velocidade * math.sin(math.radians(self.tank.angulo)) * direção
            # Atualiza a posição da coordenada central inferior do retângulo
            self.tank.rect = self.tank.imagem.get_rect(center=(self.tank.x, self.tank.y))
            self.tank.centro_inferior = (self.tank.rect.bottom)
        if self.tank.x >= 1400:
            self.tank.x = 1400
        if self.tank.x <= 40:
            self.tank.x = 40
        if self.tank.y >= 710:
            self.tank.y = 710
        if self.tank.y <= 40:
            self.tank.y = 40

