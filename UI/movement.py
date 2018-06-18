import curses
import math

class SizeObject:
    def __init__(self, width=0, height=0):
        self.WIDTH = width
        self.HEIGHT = height

    def set_size(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height

class MovingObject:
    def __init__(self, sprites, screen, pos=(0,0), main_display):

        #sprites is meant to be a dictionary of names that connect to the various string based sprites
        assert(type(sprites) == dict)
        self.sprites = sprites
        self.screen = screen
        self.main_display = main_display
        self.maxy, self.maxx = self.screen.getmaxyx()
        self.load_size(pos)
        self.pos = pos
        self.curr_sprite = list(self.sprites.keys())[0]
        self.next_move = [0,0]
        self.speed = 0

        #pos is meant to be the position of the top left corner of the sprite

    def load_size(self, pos):
        self.sizes = {}

        for name is self.sprites.keys():
            string = self.sprites[name]

            self.load_single_size(name, string)

    def load_single_size(self, name, sprite):
        string = sprite.split("\n")

        width = 0
        for line in string:
            width = max(width, line)

        height = len(string)

        assert(pos[0] + height < self.maxy)
        assert(pos[1] + width < self.maxx)

        self.sizes[name] = SizeObject(width=width, height=height)

    def move(self, end_pos):
        assert(end_pos[0] > 0)
        assert(end_pos[1] > 0)
        assert(end_pos[0] + height < self.sizes[self.curr_sprite].HEIGHT)
        assert(end_pos[1] + width < self.sizes[self.curr_sprite].WIDTH)

        self.pos = end_pos
        self.main_display.update()

    def change_sprite(self, name):
        assert(name in self.sprites.keys())
        self.curr_sprite = name
        self.main_display.update

    def add_sprite(self, name, sprite):
        self.sprites[name] = sprite
        self.load_single_size(name, sprite)

    def get_curr_pos(self):
        return self.pos

    def glide_move(self, speed, final_change):
        assert(self.pos[0] + self.next_move[0] + final_size[0] > 0)
        assert(self.pos[1] + self.next_move[1] + final_size[1] > 0)
        assert(self.pos[1] + self.next_move[1] + final_size[1] < self.sizes[self.curr_sprite].WIDTH)
        assert(self.pos[0] + self.next_move[0] + final_size[0] < self.sizes[self.curr_sprite].HEIGHT)

        self.next_move[0] += final_change[0]
        self.next_move[1] += final_change[1]
        self.speed = speed

    def update(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        self.next_move[0] -= self.speed[0]
        self.next_move[1] -= self.speed[1]

        if self.next_move[0] < 0:
            self.pos[0] += self.next_move[0]
            self.new_move[0] = 0

        if self.next_move[1] < 0:
            self.pos[1] += self.next_move[1]
            self.next_move[1] = 0


class Object(MovingObject):
    def __init__(self, sprites):
        super().__init__(sprites, sprites)
