import curses
from time import sleep
import params

class sMenu():
    def __init__(self, screen, options):
        self.screen = screen
        self.HEIGHT, self.WIDTH = self.screen.getmaxyx()
        self.SPACING = self.HEIGHT // (len(options) + 1)
        self.NUM_ELEMENTS = len(options)
        self.options = options
        step_time = params.LOAD_TIME / 2 / float(self.NUM_ELEMENTS)
        self.highlight_attr = curses.color_pair(1)

        for i in range(len(options)):

            if i == 0:
                self.screen.addstr(self.SPACING * (i+1) - 1, self.WIDTH//2 - len(options[i])//2, options[i], self.highlight_attr)
            else:
                self.screen.addstr(self.SPACING * (i+1) - 1, self.WIDTH//2 - len(options[i])//2, options[i])

            self.screen.refresh()
            sleep(step_time)

        self.highlighted = 1

    def update(self):
        event = self.screen.getch()
        self.screen.erase()

        #curses base values wasn't working for me soooooooo rip
        if event == 10:
            return self.highlighted

        if event == 65 and self.highlighted > 1:
            self.highlighted -= 1
        elif event == 66 and self.highlighted < self.NUM_ELEMENTS:
            self.highlighted += 1
        elif event == 66 and self.highlighted >= self.NUM_ELEMENTS:
            self.highlighted = 1
        elif event == 65 and self.highlighted <= 1:
            self.highlighted = self.NUM_ELEMENTS

        for i in range(self.NUM_ELEMENTS):
            if (i+1) == self.highlighted:
                self.screen.addstr(self.SPACING * (i+1) - 1, self.WIDTH//2 - len(self.options[i])//2, self.options[i], self.highlight_attr)
            else:
                self.screen.addstr(self.SPACING * (i+1) - 1, self.WIDTH//2 - len(self.options[i])//2, self.options[i])

        self.screen.box()
        self.screen.refresh()

        return False
