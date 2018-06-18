import curses
from time import sleep
from curses import wrapper
import sys
from UI import params
from UI.selection_menu import sMenu
from UI import ascii_art
from UI import movement
from UI.string_display import display_string

class General_Display:
    def __init__(self, screen):
        self.screen = screen
        self.elements = {}
        size = screen.getmaxyx()
        self.screen.clear()
        self.screen.refresh()
        self.load(screen)

    def load(self, screen):
        pass

    def refresh_all(self):
        self.screen.erase()
        for key in self.elements.keys():
            self.elements[key].update()

    def add_elem(self, elem, elem_name):
        self.elements[elem_name] = elem

class Menu(General_Display):
    def load(self, screen):
        #self.screen.addstr(0,0,"test", curses.color_pair(1))
        self.screen.refresh()
        size = self.screen.getmaxyx()
        self.HEIGHT = size[0]
        self.WIDTH = size[1]

        #load the actual menu window
        self.text_win = self.growing_square(13, params.LOAD_TIME, (10,0))

    #tells the screen to create
    def growing_square(self, final_size, time, offset):
        #make sure it will be able to grow
        assert(final_size > 1)

        box_curr_size = 1
        self.win = self.screen.derwin(box_curr_size, box_curr_size, self.HEIGHT//2, self.WIDTH//2)
        self.win.nodelay(True)

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

    def load_items(self, window):
        text = sMenu(window, ["Play Game", "Create Game", "Setup Game", "Options", "Help", "Close"])
        end = False

        new_sprite = {"term": ascii_art.TERM}

        m = movement.MovingObject(new_sprite, self.screen)
        m.move([0, self.WIDTH//2 - m.sizes[m.curr_sprite].WIDTH//2])
        self.add_elem(m, 'term')
        self.add_elem(text, "menu")

        self.elements['term'].glide_move([1,0], [10, 0])

        for i in range(10):
            sleep(0.1)
            self.refresh_all()

        while end == False:
            end = text.update()

        return end

class MainDisplay:
    def __init__(self):
        #first resize the screen to fit the entire window
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=params.WINDOW_HEIGHT,cols=params.WINDOW_WIDTH))
        sys.stdout.flush()

        #initialize the first screen objects
        self.stdscr = curses.initscr()
        self.stdscr.nodelay(True)
        self.stdscr.erase()

        #set up initial configurations
        curses.cbreak()
        curses.noecho()
        curses.mousemask(1)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.stdscr.keypad(True)
        curses.curs_set(0);

        #start up the main menu
        option = 1
        while option != 6:
            m = Menu(self.stdscr)
            #get the user's input
            option = m.load_items(m.text_win)

            if option == 1:
                #play game that is in the load section
                pass
            if option == 2:
                #begin the level creation process
                pass
            if option == 3:
                #begin process where you specify certain levels to load when playing
                pass
            if option == 4:
                #Set options for sound and stuff
                pass
            if option == 5:
                #link to github probably
                pass
            if option == 6:
                self.close()

    def close(self):
        #close everything down properly
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
