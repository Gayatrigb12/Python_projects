import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (102, 51, 0)
LIGHT_BROWN = (255, 204, 153)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load and scale queen image
QUEEN_IMG = pygame.image.load("queen.png")

# Font
FONT = pygame.font.SysFont("comicsans", 30)

def draw_board(win, board, square_size):
    n = len(board)
    for row in range(n):
        for col in range(n):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(win, color, (col * square_size, row * square_size, square_size, square_size))
            if board[row][col] == 1:
                img = pygame.transform.scale(QUEEN_IMG, (square_size, square_size))
                win.blit(img, (col * square_size, row * square_size))
    pygame.display.update()

def is_valid_n_queens(board):
    n = len(board)
    for r1 in range(n):
        for c1 in range(n):
            if board[r1][c1] == 1:
                for r2 in range(n):
                    for c2 in range(n):
                        if (r1, c1) != (r2, c2) and board[r2][c2] == 1:
                            if c1 == c2 or r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2:
                                return False
    return True

def show_message(win, msg, color, width, height):
    text = FONT.render(msg, 1, color)
    win.blit(text, (width//2 - text.get_width()//2, height + 10))
    pygame.display.update()

def n_queen_game():
    level = 4  # Start with 4x4
    attempts = 0

    while True:
        N = level
        SQUARE_SIZE = 600 // N
        WIDTH = HEIGHT = N * SQUARE_SIZE
        WIN = pygame.display.set_mode((WIDTH, HEIGHT + 50))
        pygame.display.set_caption(f"{N}-Queens Game")

        board = [[0 for _ in range(N)] for _ in range(N)]
        moves = 0
        draw_board(WIN, board, SQUARE_SIZE)

        running = True
        result_shown = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN and not result_shown:
                    x, y = pygame.mouse.get_pos()
                    row = y // SQUARE_SIZE
                    col = x // SQUARE_SIZE
                    if row < N and col < N:
                        board[row][col] ^= 1  # Toggle queen
                        moves += 1
                        draw_board(WIN, board, SQUARE_SIZE)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    attempts += 1
                    if sum(row.count(1) for row in board) == N and is_valid_n_queens(board):
                        draw_board(WIN, board, SQUARE_SIZE)
                        show_message(WIN, f"Correct! Attempts: {attempts}, Moves: {moves}", GREEN, WIDTH, HEIGHT)
                        pygame.time.delay(3000)
                        level += 1
                        running = False
                    else:
                        draw_board(WIN, board, SQUARE_SIZE)
                        show_message(WIN, f"Incorrect. Try again!", RED, WIDTH, HEIGHT)
                        result_shown = True

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    board = [[0 for _ in range(N)] for _ in range(N)]
                    moves = 0
                    result_shown = False
                    draw_board(WIN, board, SQUARE_SIZE)

if __name__ == "__main__":
    n_queen_game()
