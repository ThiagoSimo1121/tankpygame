# menu.py

import pygame
from game import game_loop

def show_menu(tela):
    font = pygame.font.Font(None, 60)
    texto = font.render("Pressione Enter para Iniciar", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(tela.get_width() // 2, tela.get_height() // 2))

    while True:
        tela.fill((0, 0, 0))  # Preenche a tela com a cor preta
        tela.blit(texto, texto_rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return True  # Retorna True indicando que o jogo deve ser iniciado

if __name__ == "__main__":
    # Para testar o menu
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    iniciar_jogo = show_menu(tela)
    if iniciar_jogo:
        game_loop()





