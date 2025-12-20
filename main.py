from src.minesweeper import MineSweeper

import pygame
import time
from pyDatalog import pyDatalog

# 1. Define Terms
# 2. Define Rules

def prolog_solver(game):

    # 3. Define Facts

    running = True
    while running:
        # Check Pygame events (keep window responsive)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.render()
        if game.game_over:
            print("Game Over!")
            time.sleep(2)
            break

        # 4. Query to Reveal/Flag
        # 5. Take Actions

if __name__ == "__main__":
    ms = MineSweeper(rows=10, cols=10, mines=10, seed=42)
    prolog_solver(ms)