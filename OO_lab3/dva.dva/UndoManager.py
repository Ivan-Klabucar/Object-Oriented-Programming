class UndoManager:
    __instance = None

    @staticmethod 
    def getInstance():
        if UndoManager.__instance == None:
            UndoManager()
        return UndoManager.__instance

    def __init__(self):
        if UndoManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UndoManager.__instance = self

        self.undo_stack = []
        self.redo_stack = []
    
    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            action.execute_undo()
            self.redo_stack.append(action)
    
    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            action.execute_do()
            self.undo_stack.append(action)
    
    def push(self, action):
        self.redo_stack = []
        self.undo_stack.append(action)