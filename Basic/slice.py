text = "Hello world!"

print(text[1])
print(text[5])

print(text[1:5])

list1 = ['영', '일', '이', '삼', '사', '오', '육']

print(list1[1:3])

print(list1[2:len(list1)])
print(list1[2:])

list2 = [213, 3, 42415, 1214, 1123, 1231, 62]
list3 = list2[:]
list2.sort()

print(list2)
print(list3)

#step의 사용법

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(list4[5:14])
print(list4[5:14:2])
print(list4[5:14:3])
print(list4[5:14:-1])
print(list4[14:5:-1])
print(list4[::3])
print(list4[::-3])
#string에서도 활용가능!

numbers = list(range(10))
print(numbers)
del numbers[0]
print(numbers)

print(numbers[:5])
del numbers[:5]
print(numbers)

numbers[1:3]
print(numbers)

#slice를 활용하여 list의 내용을 한번에 변경
numbers[1:3] = [77, 88]
print(numbers)
numbers[1:3] = [77, 88, 99]
print(numbers)
numbers[1:4] = [8]
print(numbers)