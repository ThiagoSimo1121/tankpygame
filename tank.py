import pygame


class Tank:
    def __init__(self, tank_image, x, y, scale, health, color):
        self.health = health
        self.color = color
        self.original_image = pygame.image.load(tank_image).convert_alpha()
        # Resize the image according to the provided scale
        width = int(self.original_image.get_width() * scale)
        height = int(self.original_image.get_height() * scale)
        self.original_image = pygame.transform.scale(self.original_image, (width, height))
        # Change the color of the image
        self.original_image.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)
        self.image = self.original_image
        # Set the initial position of the tank
        self.x = x
        self.y = y
        # Set the initial angle of the tank
        self.angle = 0
        # Set the initial rectangle of the tank
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def rotate(self, delta_angle):
        # Increment the angle of the tank
        self.angle += delta_angle
        # Rotate the tank's image
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        # Update the position of the bottom center of the rectangle

    def draw(self, screen):
        # Draw the tank's image on the screen at coordinates (x, y)
        screen.blit(self.image, self.rect.topleft)

    def invert(self):
        self.original_image = pygame.transform.flip(self.original_image, True, False)
        self.image = self.original_image

    def get_health(self):
        return self.health

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.health = 3
