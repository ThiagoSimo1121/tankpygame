import pygame
from tank import Tank
from movement import Movement
from bullet import Bullet

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura_tela = 1440
altura_tela = 750

# Cria a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Criar um tank
meu_tanque = Tank('Tank (2).png',100,375,0.5)
benio_tanque = Tank('Tank (2).png',1340,375,0.5)
benio_tanque.inverter()

# Lista para armazenar todas as balas
balas = []

# Define o título da janela
pygame.display.set_caption('Jogo de Tanque')

# Colocando movimentação no tank
movimento_tanque1 = Movement(meu_tanque, 0.2, {'esquerda': pygame.K_a, 'direita': pygame.K_d,
                                               'cima': pygame.K_w, 'baixo': pygame.K_s})
movimento_tanque2 = Movement(benio_tanque, 0.2, {'esquerda': pygame.K_LEFT, 'direita': pygame.K_RIGHT,
                                                 'cima': pygame.K_UP, 'baixo': pygame.K_DOWN})



# Loop principal do jogo
rodando = True
while rodando:
    # Preenche a tela com a cor preta
    tela.fill((0, 0, 0))

    # Processa os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Pressionar a tecla espaço cria uma nova bala
                balas.append(Bullet('meu_tanque', meu_tanque.x, meu_tanque.y, meu_tanque.angulo, 0.2,1))
            if evento.key == pygame.K_f:  # Pressionar a tecla espaço cria uma nova bala
                balas.append(Bullet('benio_tanque', benio_tanque.x, benio_tanque.y, benio_tanque.angulo, 0.2,-1))

    for bala in balas:
        bala.mover()
        bala.draw(tela)
        bala.collision()

        # Verifica se a bala colidiu com o tanque inimigo
        if bala.dono == 'meu_tanque' and benio_tanque is not None and bala.rect.colliderect(benio_tanque.rect):
            balas.remove(bala)  # Remove a bala
            benio_tanque = None  # Remove o tanque inimigo
        elif bala.dono == 'benio_tanque' and meu_tanque is not None and bala.rect.colliderect(meu_tanque.rect):
            balas.remove(bala)  # Remove a bala
            meu_tanque = None  # Remove o seu tanque

    # Move os tanques
    if meu_tanque is not None:  # Só move o tanque inimigo se ele ainda existir
        movimento_tanque1.mover(1)
    if benio_tanque is not None:  # Só move o tanque inimigo se ele ainda existir
        movimento_tanque2.mover(-1)

    # Desenha o tanque
    if meu_tanque is not None:  # Só desenha o tanque inimigo se ele ainda existir
        meu_tanque.desenhar(tela)
    if benio_tanque is not None:  # Só desenha o tanque inimigo se ele ainda existir
        benio_tanque.desenhar(tela)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
