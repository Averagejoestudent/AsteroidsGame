import pygame
from constants import *
def main():
    if __name__ == "__main__":
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        color = (0,0,0)
        while (True):
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.Surface.fill(screen,color)




            pygame.display.flip()
main()