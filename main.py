import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Groups and containers
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)    
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)  

    # initiating objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    #starting game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        
        screen.fill((0, 0, 0))       
        
        for drawable in drawables:
            drawable.draw(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player.shoot()           
        
        pygame.display.flip()        
        dt = clock.tick(60) /1000

        for updatable in updatables:
            updatable.update(dt)       

        #checking for collisions
        for asteroid in asteroids:
            if asteroid.is_collading(player):
                print("Game over!")
                draw_game_over(screen)
                pygame.display.flip()  # Update display
                pygame.time.delay(3000)
                pygame.quit()  # Ensures Pygame shuts down cleanly
                sys.exit()

        
        
def draw_game_over(screen):
    pygame.font.init()
    font = pygame.font.Font(None, 50)  # Use default font with size 50
    text_surface = font.render("GAME OVER", True, (255, 0, 0))  # Red text
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()  # Update display

    




if __name__ == "__main__":
    main()