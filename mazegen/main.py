from game import Game, Colors
from mazegen import Maze

rows=60
cols=80
resolution=10

BLACK=(0,0,0)
WHITE=(255,255,255)
GREY =(128,128,128)

def run(game, step):
    while True:
        if game.loop:
            try:
                grid = next(step)
                for row in grid:
                    for cell in row:
                        x = cell.x * resolution
                        y = cell.y * resolution
                        if cell.visited:
                            game.square(GREY, x, y, resolution)
                        if cell.walls["left"]:
                            game.line(WHITE, (x,y),(x,y+resolution))
                        if cell.walls["right"]:
                            game.line(WHITE, (x+resolution,y),(x+resolution,y+resolution))
                        if cell.walls["top"]:
                            game.line(WHITE, (x,y),(x+resolution,y))
                        if cell.walls["bottom"]:
                            game.line(WHITE, (x,y+resolution),(x+resolution,y+resolution))
            except:
                game.loop = False
        game.update()

if __name__ == "__main__":
    game = Game("config.yml", extravars={"width": cols*resolution+1, "height":rows*resolution+1})
    maze = Maze(rows, cols)
    step = maze.generate(0, 0, 15, 29)
    run(game, step)
