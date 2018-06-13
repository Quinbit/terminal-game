import curses
from time import sleep
from curses import wrapper
import sys
import params
from selection_menu import sMenu

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
        #self.screen.addstr(0,0,"test", curses.color_pair(1))
        self.screen.refresh()
        size = self.screen.getmaxyx()
        self.HEIGHT = size[0]
        self.WIDTH = size[1]

        #load the actual menu window
        self.text_win = self.growing_square(13, params.LOAD_TIME, (10,0))
        self.load_text(self.text_win)

    #tells the screen to create
    def growing_square(self,final_size, time, offset):
        #make sure it will be able to grow
        assert(final_size > 1)

        box_curr_size = 1
        self.win = self.screen.derwin(box_curr_size, box_curr_size, self.HEIGHT//2, self.WIDTH//2)

        #set up the correct number of steps
        step = final_size - 1.0

        steps_per_sec = time / step

        while box_curr_size != final_size:
            self.win.erase()
            self.win.mvwin(self.HEIGHT//2 - box_curr_size + offset[0], self.WIDTH//2 - box_curr_size*3 + offset[1])
            self.win.resize(box_curr_size*2, box_curr_size*6)
            self.win.box()
            self.win.refresh()
            sleep(steps_per_sec)
            box_curr_size += 1

        sleep(1)
        return self.win

    def load_text(self, window):
        sMenu(window, ["test", "test2"])
        sleep(5)

class MainDisplay:
    def __init__(self):
        #first resize the screen to fit the entire window
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=params.WINDOW_HEIGHT,cols=params.WINDOW_WIDTH))
        sys.stdout.flush()

        #initialize the first screen objects
        self.stdscr = curses.initscr()
        self.stdscr.erase()

        #set up initial configurations
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)
        curses.curs_set(0);

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
