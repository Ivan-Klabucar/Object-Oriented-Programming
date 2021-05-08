from tkinter import Tk, Canvas, Frame, BOTH, W, YES

class MyCanvas(Canvas):

    def __init__(self, window, width, height):
        super().__init__(master=window, width=width, height=height, bg='white')
        self.master_window=window
        self.initUI()
    
    def initUI(self):
        self.pack(expand=YES, fill=BOTH)
        self.create_line(250, 0, 250, 500, width=1, fill='green')
        self.create_line(0, 250, 500, 250, width=1, fill='red')
        txt_id = self.create_text(20, 30, anchor=W, text="But that all changed when the Fire Nation attacked.\nOnly the Avatar mastered all four elements.")
        self.focus(txt_id)
        self.icursor(txt_id, 4)
        def close_window(event):
            if ord(event.char) == 13:
                self.master_window.destroy()
        self.bind("<Key>", close_window)
        self.focus_set()

window = Tk()
window.geometry("500x500")
canvas = MyCanvas(window=window, width=500, height=500)
window.mainloop()

        
