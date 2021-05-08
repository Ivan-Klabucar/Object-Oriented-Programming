from HelperFunctions import *
from TextEditorModel import *


class EditAction:
    def __init__(self, txtModel):
        self.tm = txtModel
    
    def execute_do(self):
        pass

    def execute_undo(self):
        pass

class deleteBeforeAction(EditAction):
    def __init__(self, txtModel, char, cloc_before, cloc_after):
        super().__init__(txtModel)
        self.char = char
        self.cloc_before = cloc_before
        self.cloc_after = cloc_after
    
    def execute_do(self):
        self.tm.cursorLocation = copy_Location(self.cloc_before)
        self.tm.deleteBefore(private=True)
    
    def execute_undo(self):
        self.tm.cursorLocation = copy_Location(self.cloc_after)
        self.tm.insert(self.char, private=True)

class deleteAfterAction(EditAction):
    def __init__(self, txtModel, char, cloc):
        super().__init__(txtModel)
        self.char = char
        self.cloc = cloc
    
    def execute_do(self):
        self.tm.cursorLocation = copy_Location(self.cloc)
        self.tm.deleteAfter(private=True)
    
    def execute_undo(self):
        self.tm.cursorLocation = copy_Location(self.cloc)
        self.tm.insert(self.char, private=True)
        self.tm.cursorLocation = copy_Location(self.cloc)
        self.tm.notify_cursor_observers()

class deleteRangeAction(EditAction):
    def __init__(self, txtModel, txt, txt_range):
        super().__init__(txtModel)
        self.txt = txt
        self.txt_range = txt_range
    
    def execute_do(self):
        self.tm.deleteRange(self.txt_range, private=True)
    
    def execute_undo(self):
        self.tm.cursorLocation = copy_Location(self.txt_range.start)
        self.tm.insert(self.txt, private=True)

class InsertAction(EditAction):
    def __init__(self, txtModel, txt, txt_range):
        super().__init__(txtModel)
        self.txt = txt
        self.txt_range = txt_range
    
    def execute_do(self):
        self.tm.cursorLocation = copy_Location(self.txt_range.start)
        self.tm.insert(self.txt, private=True)
    
    def execute_undo(self):
        self.tm.deleteRange(self.txt_range, private=True)