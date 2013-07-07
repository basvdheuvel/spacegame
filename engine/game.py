import events, pygame

class Game(object):
    '''
    Basic engine for a pygame game.
    '''

    def __init__(self, fps=30):
        '''
        Initial settings.
        '''
        self._running = False
        self._display_surf = None
        self._clock = None
        self._fps = fps

    def init(self):
        '''
        Initialize pygame and start the game.
        '''
        pygame.init()
        self._display_surf = pygame.display.set_mode((350, 350))
        self._clock = pygame.time.Clock()
        self._running = True

    def step(self):
        '''
        Update objects.
        '''
        pass

    def render(self):
        '''
        Draw objects.
        '''
        pass

    def cleanup(self):
        '''
        Cleanup the game when it has finished.
        '''
        pygame.quit()

    def stop(self):
        '''
        End the game.
        '''
        self._running = False

    def on_exit(self):
        '''
        Default exit behaviour.
        '''
        self.stop()

    def run(self):
        '''
        Run the game.
        '''
        self.init()

        while self._running:
            for event in pygame.event.get():
                events.handle_event(event, self)
            self.step()
            self.render()
            pygame.display.flip()
            self._clock.tick(self._fps)

        self.cleanup()

    def get_surface(self):
        '''
        Get the main surface.
        '''
        return self._display_surf
