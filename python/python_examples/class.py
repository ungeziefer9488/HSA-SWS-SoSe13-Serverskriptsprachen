#!/usr/bin/python2

class zombie(object):
    # constructor
    def __init__(self, hitpoints = 10):
        # global
        self.hitpoints = hitpoints
        # protected: one underscore
        self._infestation = 100
        # private: two underscores
        self.__brains_eaten = 0

    # same modifier as attributes
    def eat_brain(self, target):
        target.remove_brain()
        self.__brains_eaten += 1

    def __add__(self, other_zombie):
        print "Super Zombie!"

if __name__ == '__main__':
    z1 = zombie(23)
    print z1.hitpoints
    z2 = zombie(45)
    z1 + z2
