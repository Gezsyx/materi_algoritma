class Stack:
    def __init__(self):
        self.items = []  

    def push(self, push):
        self.items.append(push)

    def pop(self):
        if self.isEmpty():
            print("Stack Kosong")
        else:
            self.items.pop()

    # def top(self):
    #     return self.items[-1]

    def top(self):
        if self.isEmpty():
            print("Stak Kosong")
        else:
            return self.items[-1]
            # f"DATA TERAKHIR : {self.items[-1]}"

    def isEmpty(self):
        return len(self.items) == 0

