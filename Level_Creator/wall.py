import curses
from Level_Creator import event_logger
from UI.string_display import display_string

class Wall:
    def __init__(self, pos, orientation, log, screen, is_exit==False):
        self.HEIGHT = screen.getmaxyx()[0]
        self.WIDTH = screen.getmaxyx()[1]
        self.screen = screen
        self.pos = list(pos)
        self.orientation = orientation[0].lower()
        self.is_exit = is_exit

        assert(pos[0] >= 0)
        assert(pos[1] >= 0)
        assert(pos[1] <= self.WIDTH + self.pos[1])
        assert(pos[0] <= self.HEIGHT + self.pos[0])

    def is_wall(self, location):
        return (location[1] > self.pos[1] and location[1] <= self.pos[1] + self.WIDTH) and (location[0] > self.pos[0] and location[0] <= self.pos[0] + self.HEIGHT)

    def rotate(self, location):
        self.WIDTH, self.HEIGHT = self.HEIGHT, self.WIDTH

        assert(pos[1] <= self.WIDTH + self.pos[1])
        assert(pos[0] <= self.HEIGHT + self.pos[0])

    def move(self, delta):
        assert(pos[0] + delta[0] >= 0)
        assert(pos[1] + delta[1] >= 0)
        assert(pos[1] + delta[1] <= self.WIDTH + self.pos[1])
        assert(pos[0] + delta[0]<= self.HEIGHT + self.pos[0])

        self.pos[0] += delta[0]
        self.pos[1] += delta[1]

    def update(self):
        string = "_" * self.WIDTH + "\n"

        if not self.is_exit:
            for i in range(self.HEIGHT - 2):
                string += "|" + " " * (self.WIDTH - 2) + "|"
        else:
            for i in range(self.HEIGHT - 2):
                string += "|" + "X" * (self.WIDTH - 2) + "|"

        string = "|" + "_" * (self.WIDTH - 2) + "|"

        display_string(self.screen, self.pos, string)
