
import pygame
from tank import Tank
from movement import Movement
from bullet import Bullet
from map import World, world_matrix1

def show_victory_screen(tela, vencedor):
    tela.fill((0, 0, 0))  # Preenche a tela com a cor preta
    font_path = "bridgeofficer.ttf"
    font = pygame.font.Font(font_path, 40)
    titulo = font.render(f"Player {vencedor} Wins! ", True, (255, 255, 255))
    titulo_rect = titulo.get_rect(center=(tela.get_width() // 2, tela.get_height() // 3))

    texto = font.render("Pressione R para Reiniciar", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(tela.get_width() // 2, tela.get_height() // 2))

    while True:
        tela.blit(titulo, titulo_rect)
        tela.blit(texto, texto_rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True  # Retorna True indicando reinício do jogo


def draw_text(texto, pos_x, pos_y,tela):
    font_path = "bridgeofficer.ttf"
    font = pygame.font.Font(font_path, 20)
    text = font.render(f"{texto}", True, (255, 0, 0))
    tela.blit(text, (pos_x - text.get_width() // 2, pos_y - text.get_height() // 2))

def game_loop():
    # Initialize Pygame
    pygame.init()

    # Define screen dimensions
    largura_tela = 1440
    altura_tela = 750

    # Create the screen
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # time between shots
    cooldown_time = 1500
    last_shot_time_meu_tanque = 0
    last_shot_time_benio_tanque = 0


    # Create a tank
    meu_tanque = Tank('negro.png', 100, 375, 0.3, 3, (255,255,255))
    benio_tanque = Tank('negro.png', 1340, 375, 0.3, 3, (255,3,255))
    benio_tanque.inverter()

    tank1vivo = True
    tank2vivo = True

    world = World(world_matrix1)

    # List to store all bullets
    balas = []

    # Set the title of the window
    pygame.display.set_caption('Jogo de Tanque')

    # Set up tank movements
    movimento_tanque1 = Movement(meu_tanque, 0.5, {'esquerda': pygame.K_a, 'direita': pygame.K_d,
                                                   'cima': pygame.K_w, 'baixo': pygame.K_s})
    movimento_tanque2 = Movement(benio_tanque, 0.5, {'esquerda': pygame.K_LEFT, 'direita': pygame.K_RIGHT,
                                                     'cima': pygame.K_UP, 'baixo': pygame.K_DOWN})

    # Game loop
    rodando = True
    while rodando:
        # Fill the screen with green color
        tela.fill((8,51,8))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                current_time = pygame.time.get_ticks()

                # Cooldown para o tanque 1
                if evento.key == pygame.K_SPACE and tank1vivo and (
                        current_time - last_shot_time_meu_tanque) > cooldown_time:
                    balas.append(Bullet('meu_tanque', meu_tanque.x, meu_tanque.y, meu_tanque.angulo
                                        , 1, 1))
                    last_shot_time_meu_tanque = current_time

                # Cooldown para o tanque 2
                if evento.key == pygame.K_f and tank2vivo and (
                        current_time - last_shot_time_benio_tanque) > cooldown_time:
                    balas.append(Bullet('benio_tanque', benio_tanque.x, benio_tanque.y, benio_tanque.angulo
                                        , 1, -1))
                    last_shot_time_benio_tanque = current_time

        # Update bullets
        for bala in balas:
            bala.mover()
            bala.draw(tela)
            bala.collision_screen()
            bala.collision_walls(world)

            if bala.get_num_of_collisions() >= 4:
                balas.remove(bala)

            if bala.dono == 'meu_tanque' and tank2vivo and bala.rect.colliderect(benio_tanque.rect):
                balas.remove(bala)
                bala.hit_tank(benio_tanque)


                if benio_tanque.get_vida() == 0:
                    tank2vivo = False
                    balas.clear()

            elif bala.dono == 'benio_tanque' and tank1vivo and bala.rect.colliderect(meu_tanque.rect):
                balas.remove(bala)
                bala.hit_tank(meu_tanque)


                if meu_tanque.get_vida() == 0:
                    tank1vivo = False
                    balas.clear()

        # Move tanks
        if tank1vivo:
            movimento_tanque1.mover(1)
            movimento_tanque1.collide_with_walls(world)
        if tank2vivo:
            movimento_tanque2.mover(-1)
            movimento_tanque2.collide_with_walls(world)

        # Draw tanks
        if tank1vivo:
            meu_tanque.desenhar(tela)
        if tank2vivo:
            benio_tanque.desenhar(tela)

        world.draw(tela)
        if meu_tanque.get_vida() != 0 and benio_tanque.get_vida() != 0:
            draw_text(f"PLAYER 1 LIFE: {meu_tanque.get_vida()}", 150, 40,tela)
            draw_text(f"PLAYER 2 LIFE: {benio_tanque.get_vida()}", 1280, 40,tela)
        else:
            if meu_tanque.get_vida() == 0 or benio_tanque.get_vida() == 0:
                # Verificar condição de vitória
                if not tank1vivo or not tank2vivo:
                    vencedor = 2 if tank2vivo else 1
                    iniciar_jogo = show_victory_screen(tela, vencedor)
                    if iniciar_jogo:
                        # Reiniciar o jogo
                        balas.clear()
                        tank1vivo = True
                        tank2vivo = True
                        meu_tanque.reset( 100, 375)
                        benio_tanque.reset(1340, 375)
                        balas.clear()
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()