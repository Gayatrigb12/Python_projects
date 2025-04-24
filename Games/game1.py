import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
STAR_WIDTH, STAR_HEIGHT = 10, 20
PLAYER_VEL = 5
FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, stars, elapsed_time):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "yellow", star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    FPS = 60
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000  # milliseconds
    star_count = 0
    stars = []

    hit = False

    while run:
        star_count += clock.tick(FPS)
        elapsed_time = time.time() - start_time

        if star_count >= star_add_increment:
            for _ in range(5):
                x = random.randint(0, WIDTH - STAR_WIDTH)
                y = 0  # Start from the top
                stars.append(pygame.Rect(x, y, STAR_WIDTH, STAR_HEIGHT))
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL < WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += 5
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.colliderect(player):
                stars.remove(star)
                hit = True
                print("Hit!")
                break
        if hit:
            lost_text = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH // 2 - lost_text.get_width() // 2, HEIGHT // 2 - lost_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(4000)
            run = False
        if elapsed_time >= 60:  # End the game after 60 seconds
            win_text = FONT.render("You won!", 1, "white")
            WIN.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(4000)
            run = False
        draw(player, stars, elapsed_time)

    pygame.quit()

if __name__ == "__main__":
    main()
