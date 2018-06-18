def display_string(screen, pos, string, attr=None):
    count = 0
    pos = list(pos)[:]
    string = string.split("\n")
    for line in string:
        if attr==None:
            screen.addstr(pos[0] + count, pos[1], line)
        else:
            screen.addstr(pos[0] + count, pos[1], line, attr)
        count += 1
