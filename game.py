import pygame
from snake import Snake
from grid import Grid
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, SCORE_COLOR, SCORE_FONT_SIZE

class Game:
    def __init__(self):
        self.snake = Snake()
        self.grid = Grid()
        self.score = 0
        self.font = pygame.font.Font(None, SCORE_FONT_SIZE)
    
    def update(self):
        self.snake.move()
        # Check for snake collision with the item
        if self.snake.segments[0] == self.grid.item_position:
            self.snake.grow = True
            self.grid.reset_item(self.snake.segments)
            self.score += 1
        # Check for game over conditions
        if not (0 <= self.snake.segments[0][0] < SCREEN_WIDTH // GRID_SIZE and 
                0 <= self.snake.segments[0][1] < SCREEN_HEIGHT // GRID_SIZE) or            self.snake.check_collision_with_self():
            self.reset()
    
    def draw(self, surface):
        surface.fill(BACKGROUND_COLOR)
        self.snake.draw(surface)
        self.grid.draw(surface)
        self.draw_score(surface)
    
    def draw_score(self, surface):
        score_surface = self.font.render(f'Score: {self.score}', True, SCORE_COLOR)
        surface.blit(score_surface, (10, 10))
    
    def handle_key(self, key):
        self.snake.change_direction(key)
    
    def reset(self):
        self.snake = Snake()
        self.grid = Grid()
        self.score = 0