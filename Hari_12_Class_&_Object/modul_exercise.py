# class Stack:
#     def __init__(self):
#         self.items = []

#     def push (self,item):
#         self.items.append = item
    
#     def IsEmpty(self):
#         return len(self.items) == 0

class Stack:
    def __init__(self):
        self.items = []  

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack Kosong")

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stak Kosong")

    def isEmpty(self):
        return len(self.items) == 0
