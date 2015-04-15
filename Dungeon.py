import os
import numpy


class Dungeon:

    def __init__(self, map_file):
        if os.path.isfile(map_file) == False:
            raise AttributeError("No such directory !")
        with open(filepath, "r") as f:
            height = len(f.readlines())
            width = len(f.read())


