import pygame
import math

class Tank:
    def __init__(self, imagem_tank, x, y, escala):
        # Carrega a imagem do tanque
        self.imagem_original = pygame.image.load(imagem_tank).convert_alpha()
        # Redimensiona a imagem de acordo com a escala fornecida
        largura = int(self.imagem_original.get_width() * escala)
        altura = int(self.imagem_original.get_height() * escala)
        self.imagem_original = pygame.transform.scale(self.imagem_original, (largura, altura))
        self.imagem = self.imagem_original
        # Define a posição inicial do tanque
        self.x = x
        self.y = y
        # Define o ângulo inicial do tanque
        self.angulo = 0
        # Define o retângulo inicial do tanque
        self.rect = self.imagem.get_rect(center=(self.x, self.y))


    def rotacionar(self, delta_angulo):
        # Incrementa o ângulo do tanque
        self.angulo += delta_angulo
        # Rotaciona a imagem do tanque
        self.imagem = pygame.transform.rotate(self.imagem_original, self.angulo)
        self.rect = self.imagem.get_rect(center=(self.x, self.y))
        # Atualiza a posição da coordenada central inferior do retângulo

    def desenhar(self, tela):
        # Desenha a imagem do tanque na tela nas coordenadas (x, y)
        tela.blit(self.imagem, self.rect.topleft)

    def inverter(self):
        self.imagem_original = pygame.transform.flip(self.imagem_original, True, False)
        self.imagem = self.imagem_original
