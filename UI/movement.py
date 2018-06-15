import curses

class SizeObject:
    def __init__(self, width=0, height=0):
        self.WIDTH = width
        self.HEIGHT = height

    def set_size(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height

class MovingObject:
    def __init__(self, sprites, screen, pos=(0,0)):

        #sprites is meant to be a dictionary of names that connect to the various string based sprites
        assert(type(sprites) == dict)
        self.sprites = sprites
        self.screen = screen
        self.maxy, self.maxx = self.screen.getmaxyx()
        self.load_size(pos)

        #pos is meant to be the position of the top left corner of the sprite

    def load_size(self, pos):
        self.sizes = {}

        for name is self.sprites.keys():
            string = self.sprites[name]

            string = string.split("\n")

            width = 0
            for line in string:
                width = max(width, line)

            height = len(string)

            assert(pos[0] + height < self.maxy)
            assert(pos[1] + width < self.maxx)

            self.sizes[name] = SizeObject(width=width, height=height)

    def move(self, start_pos, end_pos):

    def change_sprite(self):

    def add_sprite(self):

    def get_curr_pos(self):

class Object(MovingObject):
    def __init__(self, sprites):
        super().__init__(sprites, sprites)