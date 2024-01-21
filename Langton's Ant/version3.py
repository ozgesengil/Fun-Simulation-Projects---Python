
'''
2 Langton's Ants colonies in the same env with same rules seemingly interacting due to sharing the same env but there is no real collision mechanics '

Two ant colonies that are starting in different environments but identical in behavior since their environment is essentially the same with the same rules
Number of ants in a colony is customizable
Colors are randomly picked and by so quasirandomly assigned

Things to consider in the future:
    * the grid that underlies their environment could be made to differentiate by colony and by iteration to observe any anomalies that could occur in a ny case
    * number of ants in each colony could be made to differentiate
    * there can be a collision mechanism added to each colony with specific rules
    * number of colonies to live in the same env could be costumized

'''
import pygame as pg
from collections import deque
from random import choice, randrange

fps_intended = 60
num_ants = 400 # number of ants in each colony

class Ant:
    def __init__(self, app, pos, color):
        self.app = app
        self.color = color
        self.x, self.y = pos
        self.increments = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    def run(self):
        value = self.app.grid[self.y][self.x]
        self.app.grid[self.y][self.x] = not value

        SIZE = self.app.CELL_SIZE
        center = self.x * SIZE, self.y * SIZE
        if value:
            pg.draw.circle(self.app.screen, self.color, center, SIZE)

        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0]
        self.x = (self.x + dx) % self.app.COLS
        self.y = (self.y + dy) % self.app.ROWS


class App:
    def __init__(self, WIDTH=1600, HEIGHT=900, CELL_SIZE=6):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()

        self.CELL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)]

        colors1 = [(50, 30, i) for i in range(256)]
        colors2 = [(150, i, 120) for i in range(256)]
        ants1 = [Ant(self, [self.COLS // 3, self.ROWS // 2],
                     choice(colors1)) for i in range(num_ants)]
        ants2 = [Ant(self, [self.COLS - self.COLS // 3, self.ROWS // 2],
                     choice(colors2)) for i in range(num_ants)]
        
        self.ants = ants1 + ants2
        
        

    @staticmethod
    def get_color():
        channel = lambda: randrange(30, 220)
        return channel(), channel(), channel()

    def run(self):
        while True:
            [ant.run() for ant in self.ants]

            for event in pg.event.get():
                    
              if event.type == pg.QUIT: # if the event is an event that means to close in the documentation
                pg.quit()
                exit()
                
            #[exit() for i in pg.event.get() if i.type == pg.QUIT]
            #pg.display.flip()
            pg.display.update()
            self.clock.tick(fps_intended)


if __name__ == '__main__':
    app = App()
    app.run()