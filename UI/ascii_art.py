import curses

TERM = '''
 |__   __|  ____|  __ \|  \/  |
    | |  | |__  | |__) | \  / |
    | |  |  __| |  _  /| |\/| |
    | |  | |____| | \ \| |  | |
    |_|  |______|_|  \_\_|  |_|
    '''

class art:
    def __init__(self, string):
        self.string = string

    def glide_in_top(self):
