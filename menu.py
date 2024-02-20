import pygame


def show_menu(screen):
    screen.fill((0, 0, 0))  # Fills the screen with black color
    font_path = "assets/bridgeofficer.ttf"
    maps_png = pygame.image.load("assets/background_maps.png")
    screen.blit(maps_png, (0, 100))
    font = pygame.font.Font(font_path, 35)
    title = font.render("Combat", True, (99, 79, 88))
    title_rect = title.get_rect(center=(screen.get_width() // 2, 100))

    text = font.render("Select the map number to start the game!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, 300))

    while True:
        screen.blit(title, title_rect)
        screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 0
                if event.key == pygame.K_2:
                    return 1
                if event.key == pygame.K_3:
                    return 2
