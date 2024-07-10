import pygame
import pathlib

class Rocket:
    """A class to represent a rocket"""
    def __init__(self, rocket_game,) -> None:
        self.screen = rocket_game.screen
        self.image = pygame.image.load('rocketship.bmp')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def update(self):
        pass 
    
    def blitme(self):
        pass 
    