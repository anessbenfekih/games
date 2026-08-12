import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH ,ASTEROID_MIN_RADIUS
from logger import log_state, log_event

class Asteroid (CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            LINE_WIDTH,
        )

    def update(self, dt : float) :
        self.position += self.velocity * dt

    def split(self,asteroid_radius) :
        self.kill()
        if asteroid_radius <= ASTEROID_MIN_RADIUS :
            return
    
        log_event("asteroid_split")
        asteroid1 = Asteroid(
                self.position.x,
                self.position.y,
                asteroid_radius - ASTEROID_MIN_RADIUS
            )
        
        angle = random.uniform(20, 50)
        asteroid1.velocity = self.velocity.rotate(angle)
        asteroid1.velocity *= 1.2
        
        asteroid2 = Asteroid(
                self.position.x,
                self.position.y,
                asteroid_radius - ASTEROID_MIN_RADIUS
            )
        
        asteroid2.velocity = self.velocity.rotate(-angle)
        asteroid2.velocity *= 1.2
        
            
            
        
    
        