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

clock = pygame.time.Clock()

# créer la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")



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

    # Remplir l'écran en noir
    screen.fill(BLACK)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôle du temps (FPS)
    clock.tick(FPS)

# Fermer proprement
pygame.quit()
sys.exit()
