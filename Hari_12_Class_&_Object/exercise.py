from modul_exercise import Stack


stack1 = Stack()
stack1.push('Joko')
stack1.push('Aji')
stack1.push('Wiwi')
stack1.pop()
print(stack1.items)
print(stack1.top())


nama = str(input("Masukan Nama :"))
stack1.push(nama.capitalize())

