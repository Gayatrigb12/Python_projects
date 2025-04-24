import pygame
import time
import random

pygame.font.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load assets
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
PLAYER_IMG = pygame.transform.scale(pygame.image.load("player.png"), (40, 60))
STAR_IMG = pygame.transform.scale(pygame.image.load("star.jpg"), (10, 20))

# Game constants
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
STAR_WIDTH, STAR_HEIGHT = 20, 20
BULLET_WIDTH, BULLET_HEIGHT = 5, 10

PLAYER_VEL = 5
BULLET_VEL = 7
STAR_FALL_SPEED = 5
FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, stars, bullets, elapsed_time, score, level):
    WIN.blit(BG, (0, 0))

    # HUD
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    score_text = FONT.render(f"Score: {score}", 1, "white")
    level_text = FONT.render(f"Level: {level}", 1, "white")

    WIN.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))
    WIN.blit(score_text, (10, 10))
    WIN.blit(level_text, (WIDTH//2 - level_text.get_width()//2, 10))

    # Player
    WIN.blit(PLAYER_IMG, (player.x, player.y))

    # Stars
    for star in stars:
        WIN.blit(STAR_IMG, (star.x, star.y))

    # Bullets
    for bullet in bullets:
        pygame.draw.rect(WIN, "cyan", bullet)

    pygame.display.update()

def draw_message(message):
    msg = FONT.render(message, 1, "white")
    WIN.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
    pygame.display.update()
    pygame.time.delay(2000)

def wait_for_restart():
    msg = FONT.render("Press R to Restart or Q to Quit", 1, "white")
    WIN.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 + 40))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    return

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    FPS = 60
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_timer = 0
    stars = []
    bullets = []
    score = 0
    level = 1

    global STAR_FALL_SPEED
    STAR_FALL_SPEED = 5

    hit = False

    while run:
        star_timer += clock.tick(FPS)
        elapsed_time = time.time() - start_time

        if star_timer >= star_add_increment:
            for _ in range(5):
                x = random.randint(0, WIDTH - STAR_WIDTH)
                stars.append(pygame.Rect(x, 0, STAR_WIDTH, STAR_HEIGHT))
            star_add_increment = max(200, star_add_increment - 50)
            star_timer = 0

        # Increase difficulty
        if int(elapsed_time) % 15 == 0 and level < int(elapsed_time // 15) + 1:
            level += 1
            STAR_FALL_SPEED += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL < WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullet = pygame.Rect(player.x + player.width//2 - BULLET_WIDTH//2, player.y, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(bullet)

        for star in stars[:]:
            star.y += STAR_FALL_SPEED
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        for bullet in bullets[:]:
            bullet.y -= BULLET_VEL
            if bullet.y < 0:
                bullets.remove(bullet)
            else:
                for star in stars[:]:
                    if bullet.colliderect(star):
                        try:
                            stars.remove(star)
                            bullets.remove(bullet)
                        except:
                            pass
                        score += 1
                        break

        draw(player, stars, bullets, elapsed_time, score, level)

        if hit:
            draw_message("You Lost!")
            wait_for_restart()
            break

        if elapsed_time >= 60:
            draw_message("You Won!")
            wait_for_restart()
            break

    pygame.quit()

if __name__ == "__main__":
    main()
