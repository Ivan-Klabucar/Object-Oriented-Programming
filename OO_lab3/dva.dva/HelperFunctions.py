from Location import *

def copy_Location(l):
    return Location(l.row, l.col)

def copy_Range(r):
    return LocationRange(copy_Location(r.start), copy_Location(r.end))