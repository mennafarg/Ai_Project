import pygame
import random
import math
import sys

WIDTH, HEIGHT = 400, 400
TILE_SIZE = WIDTH // 4
FONT_SIZE = 40
BACKGROUND_COLOR = (0, 0, 255)
TILE_COLORS = {
    0: (205, 193, 180), 2: (238, 228, 218), 4: (237, 224, 200),
    8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
    64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97),
    512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)
}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 AI")
font = pygame.font.Font(None, FONT_SIZE)

def draw_grid(grid):
    screen.fill(BACKGROUND_COLOR)
    for r in range(4):
        for c in range(4):
            tile = grid[r][c]
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, TILE_COLORS.get(tile, (60, 58, 50)), rect)
            if tile != 0:
                text = font.render(str(tile), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

def initialize_game():
    grid = [[0]*4 for _ in range(4)]
    add_random_tile(grid)
    add_random_tile(grid)
    return grid

def add_random_tile(grid):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        grid[r][c] = 2 if random.random() < 0.9 else 4

def game_over(grid):
    if any(0 in row for row in grid):
        return False
    for x in range(4):
        for y in range(4):
            if x + 1 < 4 and grid[x][y] == grid[x + 1][y]:
                return False
            if y + 1 < 4 and grid[x][y] == grid[x][y + 1]:
                return False
    return True  




def draw_victory_message():
    victory_text = font.render("You Win!", True, (255, 255, 0))
    victory_rect = victory_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(victory_text, victory_rect)
    pygame.display.flip()
    pygame.time.delay(10000)  

def draw_game_over_message():
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.delay(4000)
    
def move(grid, direction):
    if direction == 'up':
        return rotate(merge_left(rotate(grid)), -1)
    elif direction == 'down':
        return rotate(merge_left(rotate(grid, -1)))
    elif direction == 'left':
        return merge_left(grid)
    elif direction == 'right':
        return reverse(merge_left(reverse(grid)))
    return grid

def merge_left(grid):
    new_grid = []
    for row in grid:
        new_row = [i for i in row if i != 0]
        i = 0
        while i < len(new_row) - 1:
            if new_row[i] == new_row[i+1]:
                new_row[i] *= 2
                new_row[i+1] = 0
            i += 1
        new_row = [i for i in new_row if i != 0]
        new_row += [0] * (4 - len(new_row))
        new_grid.append(new_row)
    return new_grid

def reverse(grid): return [row[::-1] for row in grid]
def rotate(grid, times=1):
    for _ in range(times % 4):
        grid = [list(row) for row in zip(*grid[::-1])]
    return grid


def empty_tile_heuristic(grid):
    return sum(row.count(0) for row in grid)

def smoothness_heuristic(grid):
    score = 0
    for x in range(4):
        for y in range(4):
            if grid[x][y]:
                value = math.log2(grid[x][y])
                for dx, dy in [(1,0),(0,1)]:
                    nx, ny = x+dx, y+dy
                    while 0 <= nx < 4 and 0 <= ny < 4:
                        if grid[nx][ny]:
                            target = math.log2(grid[nx][ny])
                            score -= abs(value - target)
                            break
                        nx += dx
                        ny += dy
    return score

def monotonicity_heuristic(grid):
    totals = [0, 0, 0, 0]
    for x in range(4):
        for i in range(3):
            current = math.log2(grid[x][i]) if grid[x][i] else 0
            next = math.log2(grid[x][i + 1]) if grid[x][i + 1] else 0
            if current > next:
                totals[0] += next - current
            elif next > current:
                totals[1] += current - next
    for y in range(4):
        for i in range(3):
            current = math.log2(grid[i][y]) if grid[i][y] else 0
            next = math.log2(grid[i + 1][y]) if grid[i + 1][y] else 0
            if current > next:
                totals[2] += next - current
            elif next > current:
                totals[3] += current - next
    return max(totals[0], totals[1]) + max(totals[2], totals[3])

def max_tile_heuristic(grid):
    return math.log2(max(max(row) for row in grid)) if max(max(row) for row in grid) else 0

def combined_heuristic(grid):
    return (
        2.7 * empty_tile_heuristic(grid) +
        1.0 * max_tile_heuristic(grid) +
        0.1 * smoothness_heuristic(grid) +
        1.0 * monotonicity_heuristic(grid)
    )

transposition_table = {}
def get_possible_moves(grid):
    moves = []
    for direction in ['up', 'down', 'left', 'right']:
        new_grid = move(grid, direction)
        if new_grid != grid:
            moves.append((direction, new_grid))
    return moves

def expectimax(grid, depth, player_turn, max_depth=5):
    key = (tuple(tuple(row) for row in grid), depth, player_turn)
    if key in transposition_table:
        return transposition_table[key]
    if depth == max_depth or game_over(grid):
        score = combined_heuristic(grid)
        transposition_table[key] = (score, None)
        return score, None
    if player_turn:
        max_score = -float('inf')
        best_dir = None
        for dir, new_grid in get_possible_moves(grid):
            score, _ = expectimax(new_grid, depth + 1, False, max_depth)
            if score > max_score:
                max_score, best_dir = score, dir
        transposition_table[key] = (max_score, best_dir)
        return max_score, best_dir
    else:
        empty = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]
        if not empty:
            score = combined_heuristic(grid)
            transposition_table[key] = (score, None)
            return score, None
        score = 0
        for r, c in empty:
            for val, prob in zip([2, 4], [0.9, 0.1]):
                new_grid = [row[:] for row in grid]
                new_grid[r][c] = val
                s, _ = expectimax(new_grid, depth + 1, True, max_depth)
                score += prob * s / len(empty)
        transposition_table[key] = (score, None)
        return score, None

# ========== Main Loop ==========
def main():
    grid = initialize_game()
    running = True
    while running:
        draw_grid(grid)
        pygame.time.delay(1)

        if any(2048 in row for row in grid):
            draw_grid(grid)
            draw_victory_message()
            running = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        _, best_move = expectimax(grid, 0, True)
        if best_move is None:
            running = False
        else:
            grid = move(grid, best_move)
            add_random_tile(grid)
        
        if best_move is None:
            draw_grid(grid)
            draw_game_over_message()
            running = False
   

    pygame.quit() 
    sys.exit()


if __name__ == "__main__":
    main()
