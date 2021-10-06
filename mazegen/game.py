import os
import pygame
import sys
import yaml


def _load_config(path="config.yml"):
    if not os.path.isfile(path):
        raise Exception(f"Config file {path} not found")
    config = yaml.safe_load(open(path))
    return config

class Game:
    def __init__(self, config_file, extravars=None):
        self.loop = True
        self.config = _load_config(path=config_file)
        for k, v in extravars.items():
            self.config[k] = v
        pygame.init()
        self.surface = pygame.display.set_mode((self.config["width"], self.config["height"]))
        pygame.display.set_caption(self.config.get("title", "Pygame"))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        if self.loop:
            pygame.display.update()

    def line(self, *args):
        pygame.draw.line(self.surface, *args)

    def square(self, color, x, y, w, h=None):
        if not h:
            h=w
        pygame.draw.rect(self.surface, color, pygame.Rect((x,y), (w,h)))

class Colors:
    BLACK=pygame.Color(0,0,0)
    WHITE=pygame.Color(255,255,255)
