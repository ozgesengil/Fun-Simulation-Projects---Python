'''
A simulation for the classical Langton's Ant case
Classical Rules apply: if the ant is in a white square, turn 90 degrees clockwise, move forward 1 unit, and change the color. If on the colored square, turn counterclockwise, move forward and change the color.

Colors are set to be orange and white. Change as you wish 
'''

import pygame as pg
from collections import deque



color = 'orange'
fps_intended = 60

class Ant:
    def __init__(self, app, pos, color):
        self.app = app
        self.color = color
    
        self.x, self.y = pos
        self.x = round(self.x)
        self.y = round(self.y)
        pos = [ round(x) for x in pos ]
        
        self.increments  = deque([(1,0),(0,1),(-1,0),(0,-1)])
        
        
        
    def run(self):
        
        value = self.app.grid[self.y][self.x]
        self.app.grid[self.y][self.x] = not value
        
        SIZE = self.app.CELL_SIZE
        rect = self.x*SIZE, self.y*SIZE, SIZE-1, SIZE-1
        
        if value:
            pg.draw.rect(self.app.screen, pg.Color('white'), rect)
        else:
            pg.draw.rect(self.app.screen, self.color, rect)
        
        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0]
        self.x = (self.x + dx) % self.app.COLS
        self.y = (self.y + dy) % self.app.ROWS        
        
class App:
    def __init__(self, WIDTH = 1600, HEIGHT = 900, CELL_SIZE = 12):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH,HEIGHT])
        self.clock = pg.time.Clock()
        self.title = pg.display.set_caption('Langton-Ant')
        
        self.CELL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGHT // CELL_SIZE, WIDTH//CELL_SIZE
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)]# the grid itself will be a two dimensional array each element of which is equal to zero
        self.ant = Ant(app = self, pos = [self.COLS / 2, self.ROWS /2], color = color) # if you want to change the start point randomize the pos here
    
    def run(self): # our application will be launched by a method in which we place the program for main loop for application and a loop for closing 
        while True:
            
            self.ant.run()
            
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
    