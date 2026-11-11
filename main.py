import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable,drawable)

    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    dt = 0
    Player.timer = 0


    while True: #gameloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

            
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.check_collision(bullet) == True:
                    asteroid.split()
                    bullet.kill()


        screen.fill("black")

        for anything in drawable:
            anything.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60)/1000 #limiting the framerate to 60fps

if __name__ == "__main__":          
    main()