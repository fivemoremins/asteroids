import pygame
import random
from constants import *  # type: ignore
from circleshape import CircleShape # type: ignore

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),(self.position),self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: # type: ignore
            return
        random_angle = random.uniform(20, 50)
        v1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        v2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS # type: ignore
        asteroid_v1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_v2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_v1.velocity = v1 * 1.2
        asteroid_v2.velocity = v2 * 1.2  
        new_asteroids = [asteroid_v1, asteroid_v2]    
        return new_asteroids