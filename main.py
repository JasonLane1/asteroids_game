import pygame
#from database import connect_database, database_version
from constants import *
from player import *

def main(self, x, y):
    def __init__(self, x, y):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

    pygame.init()
    print('Starting Asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(self.x, self.y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()



        dt = clock.tick(60) / 1000


    
if __name__ == "__main__":
    main()