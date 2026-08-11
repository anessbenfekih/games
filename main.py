import pygame
import sys
from constants import SCREEN_WIDTH , SCREEN_HEIGHT 
from logger import log_state, log_event 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0.0
    
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)

    
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    
    while True :
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for aster in asteroids :
            if player.collides_with(aster):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
    

    
if __name__ == "__main__":
    main()
