import curses
from time import sleep
import params

class sMenu():
    def __init__(self, screen, options):
        self.screen = screen
        self.HEIGHT, self.WIDTH = self.screen.getmaxyx()
        self.SPACING = self.HEIGHT // (len(options) + 1)
        self.NUM_ELEMENTS = len(options)
        step_time = params.LOAD_TIME / 2 / float(self.NUM_ELEMENTS)

        for i in range(len(options)):
            self.screen.addstr(self.SPACING * (i+1) - 1, self.WIDTH//2 - len(options[i])//2, options[i])
            self.screen.refresh()
            sleep(step_time)

    def update(self):
        event = self.screen.getch()
        self.screen.erase()
        self.screen.box()
        self.screen.addstr(str(event))
        self.screen.refresh()


        if event == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()
            #if (y < self.HEIGHT) and (y > 0) and (x < self.WIDTH) and (x > 0):
            self.screen.erase()
            self.screen.box()
            self.screen.addstr(str((x,y)))
            self.screen.refresh()
