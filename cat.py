import engine, pygame

class Cat(engine.GameObject):
    '''
    A cat object.
    '''

    _sprite = None

    @classmethod
    def load_sprite(cls):
        cls._sprite = pygame.image.load('cat.png').convert_alpha()

    def __init__(self, x, y):
        '''
        Construtor.
        '''
        self.x = x
        self.y = y

        self.sprite = Cat._sprite

    def left(self):
        '''
        Move the cat left.
        '''
        self.x -= 5
        
        if not self.sprite is Cat._sprite:
            self.sprite = Cat._sprite

    def right(self):
        '''
        Move the cat right.
        '''
        self.x += 5

        if self.sprite is Cat._sprite:
            self.sprite = pygame.transform.flip(Cat._sprite, True, False)

    def up(self):
        '''
        Move the cat up.
        '''
        self.y -= 5

    def down(self):
        '''
        Move the cat down.
        '''
        self.y += 5

    def render(self, surface):
        '''
        Draw the cat.
        '''
        surface.blit(self.sprite, (self.x, self.y))
