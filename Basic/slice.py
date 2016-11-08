text = "Hello world!"

print(text[1])
print(text[5])

print(text[1:5])

list = ['영', '일', '이', '삼', '사', '오', '육']

print(list[1:3])

print(list[2:len(list)])
print(list[2:])

list1 = [213, 3, 42415, 1214, 1123, 1231, 62]
list2 = list1[:]
list1.sort()

print(list1)
print(list2)