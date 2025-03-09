import pygame
from circleshape import CircleShape
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        aster1 = Asteroid(self.position.x, self.position.y, new_radius)
        aster1.velocity = v1 * 1.2
        aster2 = Asteroid(self.position.x, self.position.y, new_radius)
        aster2.velocity = v2
