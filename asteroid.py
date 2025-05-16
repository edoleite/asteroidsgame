from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen, color=(255, 255, 255)):
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        #killling permanently if the asteroid is small
        if self.radius <    ASTEROID_MIN_RADIUS:
            return
        

        #creating new ones otherwise
        #compute velocity and radius        
        random_angle = random.uniform(20, 50)
        new_velocity_vektor1 = self.velocity.rotate(random_angle)
        new_velocity_vektor2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        #create two new asteroids
        new_asteroid1 = Asteroid(*self.position, new_radius)        
        new_asteroid2 = Asteroid(*self.position, new_radius)
        
        #setting and multiplying velocities
        new_asteroid1.velocity = new_velocity_vektor1 * 1.2
        new_asteroid2.velocity = new_velocity_vektor2 * 1.2