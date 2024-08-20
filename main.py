import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 128, 255)
BULLET_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
ENEMY_COLOR = (0, 255, 0)
ENEMY_SIZE = 50
BULLET_SPEED = 7
PLAYER_SPEED = 5
ENEMY_SPEED = 3
FPS = 60

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple FPS Shooter")

# Setup player
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)

# Setup bullets and enemies
bullets = []
enemies = [pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), 
                       random.randint(-100, -ENEMY_SIZE), ENEMY_SIZE, ENEMY_SIZE) for _ in range(5)]

# Clock
clock = pygame.time.Clock()

def draw_objects():
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)
    pygame.display.flip()

def handle_movement(keys):
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.x += PLAYER_SPEED

def handle_bullets():
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

def handle_enemies():
    global enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)
            enemies.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), 
                                       random.randint(-100, -ENEMY_SIZE), ENEMY_SIZE, ENEMY_SIZE))

def check_collisions():
    global bullets, enemies
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), 
                                           random.randint(-100, -ENEMY_SIZE), ENEMY_SIZE, ENEMY_SIZE))

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - 5, player.top - 10, 10, 20)
                bullets.append(bullet)
    
    handle_movement(keys)
    handle_bullets()
    handle_enemies()
    check_collisions()
    draw_objects()
    
    clock.tick(FPS)
