import pygame
from tank import Tank
from movement import Movement
from bullet import Bullet
from map import Map, world_matrix1, world_matrix2, world_matrix3


def show_victory_screen(screen, winner):
    screen.fill((0, 0, 0))  # Fill the screen with black color
    font_path = "assets/bridgeofficer.ttf"
    font = pygame.font.Font(font_path, 35)
    title = font.render(f"Player {winner} Wins! ", True, (99, 79, 88))
    title_rect = title.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))

    text = font.render("Press R to Restart", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    credits_text = font.render("Davi Guilherme / Benicio Mozan / Thiago Simões", True, (255, 255, 255))
    credits_text_rect = credits_text.get_rect(center=(screen.get_width() // 2, 600))

    while True:
        screen.blit(title, title_rect)
        screen.blit(text, text_rect)
        screen.blit(credits_text, credits_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Returns True indicating game restart


def draw_text(text, pos_x, pos_y, screen):
    font_path = "assets/bridgeofficer.ttf"
    font = pygame.font.Font(font_path, 20)
    text_surface = font.render(f"{text}", True, (0, 0, 0))
    screen.blit(text_surface, (pos_x - text_surface.get_width() // 2, pos_y - text_surface.get_height() // 2))


def game_loop(map_choice):
    # Initialize Pygame
    pygame.init()

    # Define screen dimensions
    screen_width = 1440
    screen_height = 750

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Time between shots
    cooldown_time = 1500
    last_shot_time_my_tank = 0
    last_shot_time_enemy_tank = 0

    # Sound effects
    shot_sound_effect = pygame.mixer.Sound('assets/tankshot_effect.wav')
    hit_sound_effect = pygame.mixer.Sound('assets/tankhit_effect.wav')
    music = pygame.mixer.Sound('assets/background_effect.mp3')
    shot_sound_effect.set_volume(0.4)
    music.set_volume(0.3)
    music.play()

    # Create tanks
    my_tank = Tank('assets/tank.png', 100, 375, 0.3, 3, (255, 50, 0))
    enemy_tank = Tank('assets/tank.png', 1340, 375, 0.3, 3, (0, 0, 240))
    enemy_tank.invert()

    tank1_alive = True
    tank2_alive = True

    maps = [world_matrix1, world_matrix2, world_matrix3]
    world = Map(maps[map_choice])

    # List to store all bullets
    bullets = []

    # Set the title of the window
    pygame.display.set_caption('Combat')

    # Set up tank movements
    movement_tank1 = Movement(my_tank, 0.5, {'left': pygame.K_a, 'right': pygame.K_d,
                                             'up': pygame.K_w, 'down': pygame.K_s})
    movement_tank2 = Movement(enemy_tank, 0.5, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT,
                                                'up': pygame.K_UP, 'down': pygame.K_DOWN})

    # Game loop
    running = True
    while running:
        # Fill the screen with a background color
        screen.fill((99, 79, 88))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                current_time = pygame.time.get_ticks()

                # Cooldown for tank 1
                if event.key == pygame.K_SPACE and tank1_alive and (
                        current_time - last_shot_time_my_tank) > cooldown_time:
                    bullets.append(Bullet(my_tank, 'my_tank', my_tank.x, my_tank.y, my_tank.angle, 1, 1))
                    last_shot_time_my_tank = current_time
                    shot_sound_effect.play()

                # Cooldown for tank 2
                if event.key == pygame.K_RSHIFT and tank2_alive and (
                        current_time - last_shot_time_enemy_tank) > cooldown_time:
                    bullets.append(
                        Bullet(enemy_tank, 'enemy_tank', enemy_tank.x, enemy_tank.y, enemy_tank.angle, 1, -1))
                    last_shot_time_enemy_tank = current_time
                    shot_sound_effect.play()

        # Update bullets
        for bullet in bullets:
            bullet.move()
            bullet.draw(screen)
            bullet.collision_walls(world)

            if bullet.get_num_of_collisions() >= 4:
                bullets.remove(bullet)

            if bullet.owner == 'my_tank' and tank2_alive and bullet.rect.colliderect(enemy_tank.rect):
                bullets.remove(bullet)
                bullet.hit_tank(enemy_tank)
                hit_sound_effect.play()

                if enemy_tank.get_health() == 0:
                    tank2_alive = False
                    bullets.clear()

            elif bullet.owner == 'enemy_tank' and tank1_alive and bullet.rect.colliderect(my_tank.rect):
                bullets.remove(bullet)
                bullet.hit_tank(my_tank)
                hit_sound_effect.play()

                if my_tank.get_health() == 0:
                    tank1_alive = False
                    bullets.clear()

        # Move tanks
        if tank1_alive:
            movement_tank1.move(1)
            movement_tank1.collide_with_walls(world)
        if tank2_alive:
            movement_tank2.move(-1)
            movement_tank2.collide_with_walls(world)

        # Draw tanks
        if tank1_alive:
            my_tank.draw(screen)
        if tank2_alive:
            enemy_tank.draw(screen)

        world.draw(screen)
        if my_tank.get_health() != 0 and enemy_tank.get_health() != 0:
            draw_text(f"PLAYER 1 HEALTH: {my_tank.get_health()}", 170, 40, screen)
            draw_text(f"PLAYER 2 HEALTH: {enemy_tank.get_health()}", 1260, 40, screen)
        else:
            if my_tank.get_health() == 0 or enemy_tank.get_health() == 0:
                # Check victory condition
                if not tank1_alive or not tank2_alive:
                    winner = 2 if tank2_alive else 1
                    restart_game = show_victory_screen(screen, winner)
                    if restart_game:
                        # Restart the game
                        bullets.clear()
                        tank1_alive = True
                        tank2_alive = True
                        my_tank.reset(100, 375)
                        enemy_tank.reset(1340, 375)
                        bullets.clear()

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
