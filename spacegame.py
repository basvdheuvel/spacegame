import pygame, engine
from pygame.locals import *
from cat import Cat

class SpaceGame(engine.Game):
    '''
    A simple space game.
    '''

    def __init__(self):
        '''
        Constructor.
        '''
        super(SpaceGame, self).__init__()

        self.cat = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def init(self):
        '''
        Initialize the game.
        '''
        super(SpaceGame, self).init()

        Cat.load_sprite()
        self.cat = Cat(0, 0)

    def step(self):
        '''
        Update objects.
        '''
        if self.left_pressed:
            self.cat.left()
        if self.right_pressed:
            self.cat.right()
        if self.up_pressed:
            self.cat.up()
        if self.down_pressed:
            self.cat.down()

    def render(self):
        '''
        Draw objects.
        '''
        surface = self.get_surface()

        surface.fill(engine.WHITE)
        self.cat.render(surface)

    def on_key_down(self, event):
        '''
        A key is pushed down.
        '''
        if event.key == K_LEFT:
            self.left_pressed = True
        elif event.key == K_RIGHT:
            self.right_pressed = True
        elif event.key == K_UP:
            self.up_pressed = True
        elif event.key == K_DOWN:
            self.down_pressed = True

    def on_key_up(self, event):
        '''
        A key is released.
        '''
        if event.key == K_ESCAPE:
            self.stop()
        elif event.key == K_LEFT:
            self.left_pressed = False
        elif event.key == K_RIGHT:
            self.right_pressed = False
        elif event.key == K_UP:
            self.up_pressed = False
        elif event.key == K_DOWN:
            self.down_pressed = False

if __name__ == '__main__':
    spaceGame = SpaceGame()
    spaceGame.run()
