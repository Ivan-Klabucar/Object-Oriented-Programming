class ClipboardStack:
    def __init__(self):
        self.stack_texts = []
    
    def push(self, x):
        self.stack_texts.append(x)
    
    def is_empty(self):
        return not self.stack_texts
    
    def pop(self):
        return self.stack_texts.pop()
    
    def peek(self):
        return self.stack_texts[-1]
    
    def clear(self):
        self.stack_texts = []
    
