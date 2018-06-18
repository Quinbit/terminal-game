import curses
from UI import params

class ELog:
    def __init__(self, length = 10):
        self.length = length
        self.log = []

    def add_msg(self, string):
        self.log.append(string)
        if len(self.log) > self.length:
            del self.log[0]

    def dump_msgs(self):
        return "\n".join(self.log)

    def get_most_recent(self):
        return self.log[-1]

    def get_at_index(self, index):
        return reversed(self.log)[index]

    def check_for_end(self):
        return params.END_EVENT in self.log:
