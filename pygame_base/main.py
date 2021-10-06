import argparse
import os
import pygame
import sys
import yaml

def get_args():
    parser = argparse.ArgumentParser(description="Base for coding challenge projects")
    parser.add_argument("-x", "--width", help="Width of the window", type=int)
    parser.add_argument("-y", "--height", help="Height of the window", type=int)
    return parser.parse_args()

def load_config(args, path="config.yml"):
    if not os.path.isfile(path):
        return None
    config = yaml.safe_load(open(path))
    for key, value in config.items():
        if vars(args)[key]:
            config[key] = vars(args)[key]
    return config

def run():
    config = load_config(get_args())
    if not config:
        print("Missing config file")
        sys.exit(1)
    pygame.init()
    display_screen = pygame.display.set_mode((config["width"],config["height"]))
    pygame.display.set_caption("Base")
    exit = False
    while not exit:
        pygame.display.update()
        for et in pygame.event.get():
            if et.type == pygame.QUIT:
                exit = True

if __name__ == "__main__":
    run()
