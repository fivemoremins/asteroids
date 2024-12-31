import pygame
from circleshape import CircleShape # type: ignore
from constants import * # type: ignore
from shot import Shot # type: ignore

## Player Object
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) # type: ignore
        self.rotation = 0
        self.timer = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # type: ignore
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt # type: ignore

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) # type: ignore
            new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED # type: ignore
            self.timer = PLAYER_SHOOT_COOLDOWN # type: ignore

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            left_turn = dt - (2 * dt)
            self.rotate(left_turn)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            backwards = dt - (2 * dt)
            self.move(backwards)
        if keys[pygame.K_SPACE]:
            self.shoot()