#Rule: LIFO (Last In, First Out)
"""push(item) → add to the top

pop() → remove from the top"""
class Queue:
    def __init__(self):
        self.queue = []

    def add_task(self,task):
        if task not in self.queue:
            self.queue.append(task)
            return f"({task}) added successfully"
        
        return "Task already exists."
    def remove_task(self,task):
        if task in self.queue:
            self.queue.remove(task)
            print(f"{task} removed successfully")
        else:
            print("Task do not exists.")
    def total_task(self):
        return f"{len(self.queue)} task remaining"
    def show_task(self):
        for task in self.queue:
            print("-",task)
    def remove_first_task(self):
        if not self.queue:
            print('No task')
        else:
#            self.queue.remove(self.queue[-1])#self.queue.pop()
            self.queue.pop(0)
            print(f"{self.queue[-1]} removed")
obj = Queue()
obj.add_task('Shower')
obj.add_task('Study physics')
obj.add_task('Study python')
obj.add_task('Study math')
obj.show_task()
#chatgpt
from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def add(self, task):
        if task in self.queue:
            return "Task already exists"
        self.queue.append(task)
        return f"{task} added"

    def remove(self):
        if not self.queue:
            return "No task"
        return self.queue.popleft()

    def show(self):
        return list(self.queue)

    def total(self):
        return len(self.queue)