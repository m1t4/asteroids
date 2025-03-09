# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
import player
import asteroid
import asteroidfield
import shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield.AsteroidField.containers = (updatable)
    af = asteroidfield.AsteroidField()

    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable)

    player.Player.containers = (updatable, drawable)
    p = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick() / 1000
        # p.update(dt)
        updatable.update(dt)

        for aster in asteroids:
            if aster.collided(p):
                print("Game over!")
                sys.exit(1)
            
            for s in shots:
                if aster.collided(s):
                    aster.split()
                    s.kill()

        # render
        screen.fill((0, 0, 0))
        # p.draw(screen)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
