import pygame
import sys
import random

# Initialisez Pygame
pygame.init()

# Définissez les couleurs
BLUE = (0, 0, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Définissez les paramètres du jeu
width, height = 600, 400
cell_size = 20
snake_size = 20

# Initialisez l'écran
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Définissez la classe Snake
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([0, 1, 2, 3])  # 0: up, 1: down, 2: left, 3: right
        self.color = GREEN  # Modification de la couleur à vert

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.get_head_position()
        if self.direction == 0:
            y -= cell_size
        elif self.direction == 1:
            y += cell_size
        elif self.direction == 2:
            x -= cell_size
        elif self.direction == 3:
            x += cell_size

        # Ajustez la position si le serpent atteint les bords de la fenêtre
        x = x % width
        y = y % height

        self.positions = [((x, y))] + self.positions[:self.length - 1]

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], snake_size, snake_size))

# Définissez la classe Apple
class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
                         random.randint(0, (height - cell_size) // cell_size) * cell_size)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], snake_size, snake_size))

# Fonction principale du jeu
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    score = 0

    # Créez un objet police pour afficher le score
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 1:
                    snake.direction = 0
                elif event.key == pygame.K_DOWN and snake.direction != 0:
                    snake.direction = 1
                elif event.key == pygame.K_LEFT and snake.direction != 3:
                    snake.direction = 2
                elif event.key == pygame.K_RIGHT and snake.direction != 2:
                    snake.direction = 3

        snake.update()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
            score += 1  # Incrémente le score quand le serpent mange une pomme

        screen.fill(BLUE)
        snake.render(screen)
        apple.render(screen)

        # Affichez le score à l'écran
        score_text = font.render(f"Score: {score}", True, RED)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(10)

# Exécutez la fonction principale
if __name__ == "__main__":
    main()
