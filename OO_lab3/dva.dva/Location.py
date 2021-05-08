from functools import total_ordering

@total_ordering
class Location:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
    
    def __lt__(self, o):
        return (self.row, self.col) < (o.row, o.col)
    
    def __eq__(self, o):
        return (self.row, self.col) == (o.row, o.col)

class LocationRange:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        if not self.start: self.start = Location()
        if not self.end: self.end = Location()