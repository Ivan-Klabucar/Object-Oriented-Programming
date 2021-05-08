from tkinter import Tk, Canvas, Frame, BOTH, W, YES
from TextEditorModel import *
from Location import *
from ClipboardStack import *

class TextEditor(Tk):
    def __init__(self, TextEditorModel):
        super().__init__()
        self.TextEditorModel = TextEditorModel
        self.canvas = None
        self.lines = []
        self.clipbrd = ClipboardStack()

        self.TextEditorModel.add_cursor_observer(self)
        self.TextEditorModel.add_text_observer(self)

        self.initUI()
        
    
    def initUI(self):
        self.title('Text Editor Klabuchar')
        self.geometry("600x700")
        self.canvas = Canvas(self, bd=0)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.update_text()
        self.canvas.focus_set()
        self.bind('<Left>', lambda e: self.TextEditorModel.moveCursorLeft())
        self.bind('<Up>', lambda e: self.TextEditorModel.moveCursorUp())
        self.bind('<Down>', lambda e: self.TextEditorModel.moveCursorDown())
        self.bind('<Right>', lambda e: self.TextEditorModel.moveCursorRight())
        self.bind('<Shift-Left>', lambda e: self.mov_sel_left())
        self.bind('<Shift-Up>', lambda e: self.mov_sel_up())
        self.bind('<Shift-Down>', lambda e: self.mov_sel_down())
        self.bind('<Shift-Right>', lambda e: self.mov_sel_right())
        self.bind('<BackSpace>', lambda e: self.TextEditorModel.deleteBefore())
        self.bind('<Shift-BackSpace>', lambda e: self.TextEditorModel.deleteAfter())
        self.bind('<Delete>', lambda e: self.TextEditorModel.deleteAfter())
        self.bind('<Key>', self.myb_insert)
        self.bind('<Control-Key-c>', self.copy_to_clipbrd)
        self.bind('<Control-Key-x>', self.copy_erase_to_clipbrd)
        self.bind('<Control-Key-v>', self.paste_top_of_clipbrd)
        self.bind('<Control-Shift-Key-V>', self.paste_from_clipbrd)
        self.bind('<Control-Key-z>', lambda e: self.TextEditorModel.undoManager.undo())
        self.bind('<Control-Key-y>', lambda e: self.TextEditorModel.undoManager.redo())
    
    def paste_from_clipbrd(self, event):
        if self.clipbrd.is_empty(): return
        self.TextEditorModel.insert(self.clipbrd.pop())

    def paste_top_of_clipbrd(self, event):
        if self.clipbrd.is_empty(): return
        self.TextEditorModel.insert(self.clipbrd.peek())

    def copy_to_clipbrd(self, event):
        if not self.TextEditorModel.selectionRange: return
        text_list = [line for line in self.TextEditorModel.linesRange(self.TextEditorModel.selectionRange.start.row, self.TextEditorModel.selectionRange.end.row + 1)]
        text = '\n'.join(text_list)
        text = text[self.TextEditorModel.selectionRange.start.col:]
        skip_at_end = len(self.TextEditorModel.lines[self.TextEditorModel.selectionRange.end.row]) - self.TextEditorModel.selectionRange.end.col
        text = text[:-skip_at_end]
        self.clipbrd.push(text)
    
    def copy_erase_to_clipbrd(self, event):
        if not self.TextEditorModel.selectionRange: return
        self.copy_to_clipbrd(event)
        self.TextEditorModel.deleteRange(self.TextEditorModel.selectionRange)

    def myb_insert(self, event):
        if event.char != '' and (event.char.isprintable() or ord(event.char) == 32):
            self.TextEditorModel.insert(event.char)
        
        if event.char == '\r' or event.char == '\n':
            self.TextEditorModel.insert('\n')


    def mov_sel_left(self):
        r = self.TextEditorModel.getSelectionRange()
        if r:
            old_loc = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorLeft(selection=True)
            new_loc = copy_Location(self.TextEditorModel.cursorLocation)
            if old_loc == new_loc: return
            new_r = copy_Range(r)
            if new_loc < r.end and new_loc >= r.start:
                new_r.end = new_loc
            elif new_loc < r.start:
                new_r.start = new_loc
            else:
                return
            self.TextEditorModel.setSelectionRange(new_r)
        else:
            new_end = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorLeft(selection=True)
            new_start = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.setSelectionRange(LocationRange(new_start, new_end))
    
    def mov_sel_right(self):
        r = self.TextEditorModel.getSelectionRange()
        if r:
            old_loc = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorRight(selection=True)
            new_loc = copy_Location(self.TextEditorModel.cursorLocation)
            if old_loc == new_loc: return
            new_r = copy_Range(r)
            if new_loc > r.start and new_loc <= r.end:
                new_r.start = new_loc
            elif new_loc > r.end:
                new_r.end = new_loc
            else:
                return
            self.TextEditorModel.setSelectionRange(new_r)
        else:
            new_start = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorRight(selection=True)
            new_end = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.setSelectionRange(LocationRange(new_start, new_end))
    
    def mov_sel_up(self):
        r = self.TextEditorModel.getSelectionRange()
        if r:
            old_loc = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorUp(selection=True)
            new_loc = copy_Location(self.TextEditorModel.cursorLocation)
            if old_loc == new_loc: return
            new_r = copy_Range(r)
            if new_loc < r.end and new_loc >= r.start:
                new_r.end = new_loc
            elif new_loc < r.start:
                new_r.start = new_loc
            else:
                return
            self.TextEditorModel.setSelectionRange(new_r)
        else:
            new_end = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorUp(selection=True)
            new_start = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.setSelectionRange(LocationRange(new_start, new_end))
    
    def mov_sel_down(self):
        r = self.TextEditorModel.getSelectionRange()
        if r:
            old_loc = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorDown(selection=True)
            new_loc = copy_Location(self.TextEditorModel.cursorLocation)
            if old_loc == new_loc: return
            new_r = copy_Range(r)
            if new_loc < r.start and new_loc <= r.end:
                new_r.start = new_loc
            elif new_loc > r.end:
                new_r.end = new_loc
            else:
                return
            self.TextEditorModel.setSelectionRange(new_r)
        else:
            new_start = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.moveCursorDown(selection=True)
            new_end = copy_Location(self.TextEditorModel.cursorLocation)
            self.TextEditorModel.setSelectionRange(LocationRange(new_start, new_end))

    def update_selection(self):
        r = self.TextEditorModel.getSelectionRange()
        self.canvas.delete('selection')
        if r:
            curr_row = r.start.row
            while curr_row <= r.end.row:
                s_col = 0
                e_col = len(self.TextEditorModel.lines[curr_row])
                if curr_row == r.start.row: s_col = r.start.col
                if curr_row == r.end.row: e_col = r.end.col
                s_id = self.canvas.create_rectangle(3 +7*s_col, 3+15*curr_row, 3 + 7*e_col,  15*(curr_row+1), fill='deep sky blue', tags='selection', outline='')
                self.canvas.tag_lower(s_id, "line")
                curr_row += 1
    
    def updateCursorLocation(self, loc):
        self.canvas.delete('cursor')
        self.canvas.create_line(3 + 7 * loc.col, 3+15*loc.row, 3 + 7 * loc.col, 15*(loc.row + 1), tags="cursor")

    def update_text(self):
        self.canvas.delete('all')
        idx = 0
        self.lines = []
        for textLine in self.TextEditorModel.allLines():
            self.lines.append(self.canvas.create_text(4, 8 + 15 * idx, anchor=W, text=textLine, font='TkFixedFont', width=500, tags="line"))
            idx += 1
        self.updateCursorLocation(self.TextEditorModel.cursorLocation)
        self.update_selection()


tem = TextEditorModel("But thttacked.\nOnred all four elements.\nOhed.")
te = TextEditor(tem)
te.mainloop()