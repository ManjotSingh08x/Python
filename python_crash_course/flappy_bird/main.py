import pygame 
import neat
import time
import os
import random
from bird import Bird

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]
PIP_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))
BASE_IMG= pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))

