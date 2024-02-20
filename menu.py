import pygame
from game import game_loop

def show_menu(tela):
    tela.fill((0, 0, 0))  # Preenche a tela com a cor preta
    font_path = "bridgeofficer.ttf"
    font = pygame.font.Font(font_path, 60)
    titulo = font.render("Combat", True, (255, 255, 255))
    titulo_rect = titulo.get_rect(center=(tela.get_width() // 2, tela.get_height() // 3))

    texto = font.render("Pressione Enter para Iniciar", True, (255, 255, 255))
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
                if evento.key == pygame.K_RETURN:
                    return True  # Retorna True indicando que o jogo deve ser iniciado

if __name__ == "__main__":
    # Define as dimensões da tela
    largura_tela = 1440
    altura_tela = 750

    # Cria a tela
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.init()
    iniciar_jogo = show_menu(tela)
    if iniciar_jogo:
        game_loop()
