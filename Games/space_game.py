import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
PLAYER_IMG = pygame.transform.scale(pygame.image.load("player.png"), (40, 60))
STAR_IMG = pygame.transform.scale(pygame.image.load("star.jpg"), (20, 20))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
STAR_WIDTH, STAR_HEIGHT = 20, 20
PLAYER_VEL = 7
STAR_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)
BIG_FONT = pygame.font.SysFont("comicsans", 60)

def draw(player, stars, elapsed_time, score):
    WIN.blit(BG, (0, 0))
    
    # Draw UI
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    score_text = FONT.render(f"Score: {score}", 1, "white")
    WIN.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))
    WIN.blit(score_text, (10, 10))
    
    # Draw player
    WIN.blit(PLAYER_IMG, (player.x, player.y))
    
    # Draw stars
    for star in stars:
        WIN.blit(STAR_IMG, (star.x, star.y))
    
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    FPS = 60

    start_time = time.time()
    elapsed_time = 0
    score = 0

    star_timer = 0
    star_add_interval = 2000
    stars = []

    hit = False

    while run:
        dt = clock.tick(FPS)
        elapsed_time = time.time() - start_time
        star_timer += dt

        if star_timer >= star_add_interval:
            for _ in range(5):
                x = random.randint(0, WIDTH - STAR_WIDTH)
                stars.append(pygame.Rect(x, 0, STAR_WIDTH, STAR_HEIGHT))
            star_add_interval = max(300, star_add_interval - 50)  # Increase difficulty
            star_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL < WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VEL

        # Star movement & collision
        for star in stars[:]:
            star.y += STAR_VEL
            if star.colliderect(player):
                hit = True
                break
            if star.y > HEIGHT:
                stars.remove(star)
                score += 1  # Score increases when dodged

        if hit:
            lost_text = BIG_FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH // 2 - lost_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        if elapsed_time >= 60:
            win_text = BIG_FONT.render("You Won!", 1, "white")
            WIN.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, stars, elapsed_time, score)

    pygame.quit()

if __name__ == "__main__":
    main()
