# main.py

import pygame
from menu import show_menu
from game import game_loop

def main():
    # Inicializa o Pygame
    pygame.init()

    # Define as dimensões da tela
    largura_tela = 1440
    altura_tela = 750

    # Cria a tela
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Jogo de Tanque')

    # Exibe o menu
    iniciar_jogo = show_menu(tela)

    # Se o jogador escolher iniciar o jogo, executa o loop do jogo
    if iniciar_jogo:
        game_loop()

    # Finaliza o Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
