from Location import *
from HelperFunctions import *

class TextEditorModel:
    def __init__(self, initial_text):
        self.lines = initial_text.split('\n')
        self.selectionRange = None
        self.cursorLocation = Location()
        self.cursor_observers = []
        self.text_observers = []

    def notify_text_observers(self):
        for o in self.text_observers: o.update_text()
    
    def notify_cursor_observers(self):
        for o in self.text_observers: o.updateCursorLocation(self.cursorLocation)
    
    def valid_location(self, l):
        if l.row >= 0 and l.row < len(self.lines) and \
           l.col >= 0 and l.col <= len(self.lines[l.row]):
            return True
        return False
    
    def valid_range(self, r):
        if r and self.valid_location(r.start) and self.valid_location(r.end) and \
           r.start < r.end:
           return True
        return False
    
    def allLines(self):
        return iter(self.lines)
    
    def linesRange(self, index1, index2):
        return (self.lines[i] for i in range(index1, index2))
    
    def curr_line(self, new_line=None):
        if new_line != None: self.lines[self.cursorLocation.row] = new_line
        return self.lines[self.cursorLocation.row]
    
    def above_line(self):
        return self.lines[self.cursorLocation.row - 1]
    
    def below_line(self):
        return self.lines[self.cursorLocation.row + 1]
    
    def add_cursor_observer(self, o):
        self.cursor_observers.append(o)
    
    def remove_cursor_observer(self, o):
        if o in self.cursor_observers:
            self.cursor_observers.remove(o)

    def add_text_observer(self, o):
        self.text_observers.append(o)
    
    def remove_text_observer(self, o):
        if o in self.cursor_observers:
            self.text_observers.remove(o)
    
    def moveCursorLeft(self, selection=False):
        if not selection: self.setSelectionRange(None)
        if self.cursorLocation.col > 0:
            self.cursorLocation.col -= 1
            self.notify_cursor_observers()
        elif self.cursorLocation.row > 0:
            self.cursorLocation.row -= 1
            self.cursorLocation.col = len(self.lines[self.cursorLocation.row])
            self.notify_cursor_observers()
    
    def moveCursorRight(self, selection=False):
        if not selection: self.setSelectionRange(None)
        if self.cursorLocation.col < len(self.curr_line()):
            self.cursorLocation.col += 1
            self.notify_cursor_observers()
        elif self.cursorLocation.row < len(self.lines) - 1:
            self.cursorLocation.col = 0
            self.cursorLocation.row += 1
            self.notify_cursor_observers()

    def moveCursorUp(self, selection=False):
        if not selection: self.setSelectionRange(None)
        if self.cursorLocation.row > 0:
            self.cursorLocation.col = min(self.cursorLocation.col, len(self.above_line()))
            self.cursorLocation.row -= 1
            self.notify_cursor_observers()
    
    def moveCursorDown(self, selection=False):
        if not selection: self.setSelectionRange(None)
        if self.cursorLocation.row < (len(self.lines) - 1):
            self.cursorLocation.col = min(self.cursorLocation.col, len(self.below_line()))
            self.cursorLocation.row += 1
            self.notify_cursor_observers()
    
    def deleteBefore(self, private=False):
        if self.selectionRange:
            self.deleteRange(self.selectionRange)
            return

        if self.cursorLocation.col > 0:
            curr_l = self.curr_line()
            curr_l = curr_l[:self.cursorLocation.col - 1] + curr_l[self.cursorLocation.col:]
            self.curr_line(curr_l)
            self.cursorLocation.col -= 1
        elif self.cursorLocation.row > 0:
            curr_l = self.curr_line()
            above_line_len = len(self.above_line())
            self.lines[self.cursorLocation.row - 1] += curr_l
            del self.lines[self.cursorLocation.row]
            self.cursorLocation.row -= 1
            self.cursorLocation.col = above_line_len
        else:
            return
        if not private:
            self.notify_text_observers()
            
    
    def deleteAfter(self):
        if self.selectionRange:
            self.deleteRange(self.selectionRange)
            return

        if self.cursorLocation.col < len(self.curr_line()):
            curr_l = self.curr_line()
            curr_l = curr_l[:self.cursorLocation.col] + curr_l[self.cursorLocation.col + 1:]
            self.curr_line(curr_l)
        elif self.cursorLocation.col == len(self.curr_line()) and self.cursorLocation.row < len(self.lines) - 1:
            self.lines[self.cursorLocation.row] += self.below_line()
            del self.lines[self.cursorLocation.row + 1]
        else:
            return
        self.notify_text_observers()
    
    # def del_at(self, loc): # does not update the observers
    #     cl = self.lines[loc.row]
    #     self.lines[loc.row] = cl[:loc.col] + cl[loc.col + 1:]
    #     if not self.lines[loc.row]: del self.lines[loc.row]
    
    # def decrement_Location(self, loc):
    #     if loc.col == 0:
    #         loc.row -= 1
    #         loc.col = len(self.lines[loc.row])
    #     else:
    #         loc.col -= 1

    def deleteRange(self, r):
        if self.valid_range(r):
            lstart = copy_Location(r.start)
            self.cursorLocation = copy_Location(r.end)
            self.selectionRange = None
            while self.cursorLocation != lstart:
                self.deleteBefore(private=True)
            self.notify_text_observers()
    
    def getSelectionRange(self):
        return self.selectionRange
    
    def setSelectionRange(self, r):
        if self.valid_range(r): 
            self.selectionRange = r
        else:
            self.selectionRange = None
        self.notify_text_observers()
    
    def insert(self, text):
        if self.selectionRange: self.deleteRange(self.selectionRange)

        new_lines = text.split('\n')
        if len(new_lines) == 1:
            new_line = new_lines[0]
            curr_line = self.curr_line()
            curr_line = curr_line[:self.cursorLocation.col] + new_line + curr_line[self.cursorLocation.col:]
            self.curr_line(curr_line)
            self.cursorLocation.col += len(new_line)
        else:
            first = True
            overflow = ''
            for new_line in new_lines:
                if first:
                    curr_line = self.curr_line()
                    overflow = curr_line[self.cursorLocation.col:]
                    first = False
                    curr_line = curr_line[:self.cursorLocation.col] + new_line
                    self.curr_line(curr_line)
                else:
                    self.cursorLocation.row += 1
                    self.cursorLocation.col = 0
                    self.lines.insert(self.cursorLocation.row, new_line)
            self.cursorLocation.col = len(self.lines[self.cursorLocation.row])
            self.lines[self.cursorLocation.row] += overflow
        self.notify_text_observers()

        
            
                