#!/usr/bin/python2

import sys

def promote( name="John Doe"  ):
    print "%s is awesome!" % name

if __name__ == '__main__':
    if len(sys.argv) > 1:
        promote(sys.argv[1])
    else:
        promote()
