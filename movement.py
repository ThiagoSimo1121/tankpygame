import pygame
import math

class Movement:
    def __init__(self, tank, velocidade, teclas):
        self.tank = tank
        self.velocidade = velocidade
        self.teclas = teclas
        self.old_x = self.tank.x
        self.old_y = self.tank.y

    def mover(self, direção):
        keys = pygame.key.get_pressed()
        if keys[self.teclas['esquerda']]:
            self.tank.rotacionar(0.5)  # Gira no sentido anti-horário
        if keys[self.teclas['direita']]:
            self.tank.rotacionar(-0.5)  # Gira no sentido horário
        if keys[self.teclas['cima']]:
            # Move o tanque na direção que está apontando
            self.old_x = self.tank.x
            self.old_y = self.tank.y
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

    def collide_with_walls(self, world):
        for tile in world.tile_list:
            if self.tank.rect.colliderect(tile[1]):
                # Se houver uma colisão com um bloco do mapa, move o tanque de volta para a posição anterior
                self.tank.x = self.old_x
                self.tank.y = self.old_y
                # Atualiza a posição da coordenada central inferior do retângulo
                self.tank.rect = self.tank.imagem.get_rect(center=(self.tank.x, self.tank.y))
