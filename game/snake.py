import sys # ici import pour avoir un contrôle sur notre environnement
import pygame

# initialiasation de pygame
pygame.init()

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

# créer la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


# Boucle principale du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0

    # Déplacement du serpent (ajoute une nouvelle tête et enlève la queue)
    new_head = [snake[0][0] + dx, snake[0][1] + dy]
    snake.insert(0, new_head)
    snake.pop()


    # Remplir l'écran en noir
    screen.fill(BLACK)
    for segment in snake:
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôle du temps (FPS)
    clock.tick(FPS)

# Fermer proprement
pygame.quit()
sys.exit()
