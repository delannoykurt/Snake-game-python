import random


# Constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10  # Images par seconde

# Couleurs
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialisation du serpent
snake = [
    [5, 5],
    [4, 5],
    [3, 5]
]

# Direction initiale (droite)
dx, dy = 1, 0


# Générer une position aléatoire sur la grille
def random_food_position():
    while True:
        pos = [random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
               random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1)]
        if pos not in snake:
            return pos
