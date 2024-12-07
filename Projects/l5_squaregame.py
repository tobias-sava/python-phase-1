import pygame 
import random
import sys

pygame.init()                               # initializes pygame

WIDTH, HEIGHT = 800, 600                    # screen dimensions

WHITE = (255, 255, 255)                     # colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the enemies!")

clock = pygame.time.Clock()

player_size = 50 
player_pos = [WIDTH // 2, HEIGHT -2 * player_size]
player_speed = 5

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos
    if (ex < px < ex + enemy_size or ex < px + player_size < ex + enemy_size) and (
        ey < py < ey + enemy_size or ey < py + player_size < ey + enemy_size
    ):
        return True
    return False

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        print("Game Over!")
        
    # drawing everything 

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, RED, (*enemy_pos, enemy_size, enemy_size))
    
    pygame.display.flip()
    
    clock.tick(60)

