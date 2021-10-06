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
    def __init__(self, config_file):
        self.loop = True
        self.config = _load_config(path=config_file)
        pygame.init()
        self.surface = pygame.display.set_mode((self.config["width"], self.config["height"]))
        pygame.display.set_caption(self.config.get("title", "Pygame"))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        if self.loop:
            pygame.display.update()

