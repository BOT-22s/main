import pygame
from settings import GRID_SIZE, SNAKE_COLOR, SNAKE_START_LENGTH

class Snake:
    def __init__(self):
        self.segments = [(GRID_SIZE // 2, GRID_SIZE // 2)] * SNAKE_START_LENGTH
        self.direction = pygame.K_RIGHT
        self.grow = False
    
    def move(self):
        head_x, head_y = self.segments[0]
        
        if self.direction == pygame.K_UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - 1, head_y)
        else: # self.direction == pygame.K_RIGHT
            new_head = (head_x + 1, head_y)
        
        if not self.grow:
            self.segments.pop()
        else:
            self.grow = False
        
        self.segments.insert(0, new_head)
    
    def change_direction(self, key):
        if key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            # Prevent the snake from moving directly opposite to its current direction
            if (key == pygame.K_UP and self.direction != pygame.K_DOWN) or                (key == pygame.K_DOWN and self.direction != pygame.K_UP) or                (key == pygame.K_LEFT and self.direction != pygame.K_RIGHT) or                (key == pygame.K_RIGHT and self.direction != pygame.K_LEFT):
                self.direction = key
    
    def draw(self, surface):
        for segment in self.segments:
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, SNAKE_COLOR, rect)
    
    def check_collision_with_self(self):
        return self.segments[0] in self.segments[1:]