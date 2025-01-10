from collections import deque

#Deklarasi objek

queue = deque()

def enqueue(value):
    queue.append(value)

def enqueueLeft(value):
    queue.appendleft(value)

enqueue('Sepongbob')
enqueue('Petrick')
enqueueLeft('Squirtwod')
print(queue)