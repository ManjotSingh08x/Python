import pygame 
import sys
from rocket import Rocket
class RocketGame:
    """Overall game of moving a rocket ship"""
    
    def __init__(self) -> None:
        """Initialize the main game loop"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.rocket = Rocket(self)
        
        pygame.display.set_caption("Rocket game")
    
    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill((255,255,255))
        self.rocket.blitme()
        pygame.display.flip()
        
if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()

    