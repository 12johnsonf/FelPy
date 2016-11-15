import random

class Formatter():

    def __init__(self, args):
        self.builder = []
        self.add(args)


    def add(self, toAdd):
        if (type(toAdd) is list):
            for item in toAdd:
                self.builder.append(item)
        else:
            self.builder.append(toAdd)

    def randomize(self):
        self.builder=random(self.builder)

    def simpleOutput(self):
        return self.builder

    def formatOutput(self, x, y):
        return formatOutput(self.builder, x, y)

    def clear(self):
        self.builder = []

def random(lst):
    used = []
    top = len(lst)
    for i in range(0,top):
        while True:
            rand = random.randrange(0,top)
            if (rand not in used):
                used.append(rand)
                break
    builder2 = []
    for num in used:
        builder2.append(lst[used[num]])
    return builder2

def formatOutput(lst, x, y):
    if x*y > len(lst):
        raise IndexError('The list cannot be put in a grid that small')
    final = []
    for i in range(0,x):
        row = []
        for j in range(0,y):
            row.append(lst[i+j*x])
        final.append(row)
    return final
