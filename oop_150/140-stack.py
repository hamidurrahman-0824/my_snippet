#Rule: FIFO (First In, First Out)
"""Operations:

enqueue(item) → add to the back

dequeue() → remove from the front"""
class Stack:
    def __init__(self):
        self.stack = []
    def add(self,task):
        self.stack.insert(task,0)
    def remove(self,task):
        self.stack.pop(0)
    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False
        