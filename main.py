# main.py

import pygame
from menu import show_menu
from game import game_loop


def main():
    # Initialize Pygame
    pygame.init()
 
    # Define screen dimensions
    screen_width = 1440
    screen_height = 750

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Combat')

    # Display the menu
    start_game_option = show_menu(screen)

    # If the player chooses to start the game, execute the game loop
    if start_game_option == 0:
        game_loop(0)
    elif start_game_option == 1:
        game_loop(1)
    elif start_game_option == 2:
        game_loop(2)

    # Quit Pygame
    pygame.quit()


main()
