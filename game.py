import pygame
from tank import Tank
from movement import Movement
from bullet import Bullet
from map import World, world_matrix1 


# Inicializa o Pygame
pygame.init()


def draw_text(texto, pos_x, pos_y):
    font = pygame.font.Font(None, 40)
    text = font.render(f"{texto}", True, (255, 255, 255))
    tela.blit(text, (pos_x - text.get_width() // 2, pos_y- text.get_height() // 2))

# Define as dimensões da tela
largura_tela = 1441
altura_tela = 751

#criando linhas imagianrias
tamanho_linha = 30
def desenhar_linhas():
    for linha in range (49):
        pygame.draw.line(tela, (255,255,255), (0, linha * tamanho_linha), (largura_tela, linha * tamanho_linha))
        pygame.draw.line(tela, (255,255,255), (linha * tamanho_linha, 0), (linha * tamanho_linha, altura_tela))

#world data (transformar em .txt depois)


world = World(world_matrix1)

# Cria a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Criar um tank
meu_tanque = Tank('Tank (2).png',100,375,0.5, 3)
benio_tanque = Tank('Tank (2).png',1340,375,0.5, 3)
benio_tanque.inverter()

tank1vivo = True
tank2vivo = True

# Lista para armazenar todas as balas
balas = []

# Define o título da janela
pygame.display.set_caption('Jogo de Tanque')

# Colocando movimentação no tank
movimento_tanque1 = Movement(meu_tanque,2, {'esquerda': pygame.K_a, 'direita': pygame.K_d,
                                               'cima': pygame.K_w, 'baixo': pygame.K_s})
movimento_tanque2 = Movement(benio_tanque, 0.2, {'esquerda': pygame.K_LEFT, 'direita': pygame.K_RIGHT,
                                                 'cima': pygame.K_UP, 'baixo': pygame.K_DOWN})


# Loop principal do jogo

rodando = True
while rodando:
    # Preenche a tela com a cor verde
    tela.fill((140, 238, 144))

    # Processa os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and tank1vivo:  # Pressionar a tecla espaço cria uma nova bala
                balas.append(Bullet('meu_tanque', meu_tanque.x, meu_tanque.y, meu_tanque.angulo, 1,1))
            if evento.key == pygame.K_f and tank2vivo:  # Pressionar a tecla espaço cria uma nova bala
                balas.append(Bullet('benio_tanque', benio_tanque.x, benio_tanque.y, benio_tanque.angulo, 1,-1))

    for bala in balas:
        bala.mover()
        bala.draw(tela)
        bala.collision_screen()
        bala.collision_walls(world)
        

        if bala.get_num_of_collisions() >= 3:
            balas.remove(bala)

        # Verifica se a bala colidiu com o tanque inimigo
        if bala.dono == 'meu_tanque' and tank2vivo and bala.rect.colliderect(benio_tanque.rect):
            balas.remove(bala)  # Remove a bala
            bala.hit_tank(benio_tanque) 
            if benio_tanque.get_vida() == 0:
                tank2vivo = False
                balas.clear()

        elif bala.dono == 'benio_tanque' and tank1vivo and bala.rect.colliderect(meu_tanque.rect):
            balas.remove(bala)  # Remove a bala
            bala.hit_tank(meu_tanque)
            if meu_tanque.get_vida() == 0:
                tank1vivo = False
                balas.clear()
               
    
    # Move os tanques
    if tank1vivo:  # Só move o tanque inimigo se ele ainda existir
        movimento_tanque1.mover(1)
        movimento_tanque1.collide_with_walls(world)
    if tank2vivo:  # Só move o tanque inimigo se ele ainda existir
        movimento_tanque2.mover(-1)
        movimento_tanque2.collide_with_walls(world)

    # Desenha o tanque
    if tank1vivo:  # Só desenha o tanque inimigo se ele ainda existir
        meu_tanque.desenhar(tela)
    if tank2vivo == True:  # Só desenha o tanque inimigo se ele ainda existir
        benio_tanque.desenhar(tela)

    
    world.draw(tela)
    if meu_tanque.get_vida() != 0 and benio_tanque.get_vida() != 0:
        draw_text(f"PLAYER 1 LIFE: {meu_tanque.get_vida()}", 150,40)
        draw_text(f"PLAYER 2 LIFE: {benio_tanque.get_vida()}", 1300,40)
    else:
        if meu_tanque.get_vida() == 0:
            draw_text(f"PLAYER 2 WINS!!", 650,40)
        if benio_tanque.get_vida() == 0:
            draw_text(f"PLAYER 1 WINS!!", 650,40)
        

       
    
    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
