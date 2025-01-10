from queue import LifoQueue

stack = LifoQueue(maxsize=5)

stack.put("1")
stack.put("2")
stack.put("3")
stack.put("4")

print(stack.queue)

stack.get()

print(f"Data Terakhir : {stack.queue[-1]}")
print(f"Apakah Data Penuh : {stack.full()}")
print(f"Apakah Data Kosong : {stack.empty()}")
print(f"Jumlah Data : {stack.qsize()}")

print(stack.queue)