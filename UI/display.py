import curses
from time import sleep
from curses import wrapper
import sys
import params

class General_Display:
    def __init__(self, screen):
        self.screen = screen
        size = screen.getmaxyx()
        self.screen.clear()
        self.screen.refresh()
        self.load(screen)

    def load(self, screen):
        pass

class Menu(General_Display):
    def load(self, screen):
        self.screen.addstr(0,0,"test", curses.color_pair(1))
        self.screen.refresh()
        try:
            while True:
                pass
        except:
            pass

class MainDisplay:
    def __init__(self):
        #first resize the screen to fit the entire window
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=params.WINDOW_HEIGHT,cols=params.WINDOW_WIDTH))
        sys.stdout.flush()

        #initialize the first screen objects
        self.stdscr = curses.initscr()
        self.stdscr.clear()

        #set up initial configurations
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

        Menu(self.stdscr)

        self.close()

    def run(self):
        pass

    def close(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

a = MainDisplay()
