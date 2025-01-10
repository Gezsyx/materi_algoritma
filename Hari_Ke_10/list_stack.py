# # stack kosong
# stack = []

# stack.append("1")
# stack.append("2")
# stack.append("3")

# # print(stack)

# # Melihat data
# print(stack[-1])
# print(stack)


# # menghapus data terakhir, terbaru, teratas
# stack.pop()
# stack.pop()
# # print(stack)

stack = []

def push(value):
    if len(stack) >= 4:
        print("Penuh")
    else :
        stack.append(value)


def top():
    print(f"DATA TERAKHIR : {stack[-1]}")

def isempty():
    print(f"KOSONG" if len(stack) == 0 else "Tidak Kosong")

def destroy():
    stack.clear()

push("1")
push("2")
push("3")
push("4")
push("5")

isempty()
print(stack)
destroy()
isempty()

print(stack)

