import pygame
import sys
from constants import * # type: ignore
from player import Player # type: ignore
from asteroid import Asteroid # type: ignore
from asteroidfield import AsteroidField # type: ignore
from shot import Shot # type: ignore

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore
	clock = pygame.time.Clock()
	dt = 0

	## Object Groups
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)


	## Player Instance
	pos_x = SCREEN_WIDTH / 2 # type: ignore
	pos_y = SCREEN_HEIGHT / 2 # type: ignore
	player = Player(pos_x, pos_y) # type: ignore
	asteroid_field = AsteroidField()	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen, (0,0,0))
		for sprite in updatable:
			sprite.update(dt)		
		for asteroid in asteroids:
			if asteroid.check_collision(player):
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if shot.check_collision(asteroid):
					shot.kill()
					new_asteroids = asteroid.split()
					asteroids.add(new_asteroids)
		for sprite in drawable:				
			sprite.draw(screen)
		pygame.display.flip()				
		dt = clock.tick(60) / 1000			
###

if __name__ == "__main__":
	main()
