import pygame
import random
from settings import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, ITEM_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

class Grid:
    def __init__(self):
        self.item_position = self.spawn_item()
    
    def spawn_item(self):
        # Generate a random position for a new item
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    def draw(self, surface):
        # Draw the grid lines (optional, for visual aid)
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(surface, (200, 200, 200), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(surface, (200, 200, 200), (0, y), (SCREEN_WIDTH, y))
        
        # Draw the item
        item_rect = pygame.Rect(self.item_position[0] * GRID_SIZE, self.item_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, ITEM_COLOR, item_rect)
    
    def reset_item(self, snake_segments):
        # Ensure the new item does not spawn on the snake
        new_position = self.spawn_item()
        while new_position in snake_segments:
            new_position = self.spawn_item()
        self.item_position = new_position