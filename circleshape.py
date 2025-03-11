# Base class for game objects
import pygame
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass
                
    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self,other_obj):
         sum_of_radii = self.radius + other_obj.radius
         distance = self.position.distance_to(other_obj.position)
         return distance <= sum_of_radii