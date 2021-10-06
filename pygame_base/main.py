from game import Game


def run():
    while True:
        game.update()

if __name__ == "__main__":
    game = Game("config.yml")
    run()
