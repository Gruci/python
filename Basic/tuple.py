tuple1 = (1,2,3)
print(type(tuple1))

tuple2 = 1,2,3

print(type(tuple2))

list1 = [1,2,3]

tuple3 = tuple(list1)

print(type(tuple3))

#tuple은 값의 변경과 삭제가 불가능 pop +등..

x = 5
y = 10

#norm x.y change
temp = x
x = y
y = temp

print (x,y)

x,y = y,x

print (x,y)
#using tuple

def tuple_func():
    return 1,2

q,w = tuple_func()

print(q,w)

#tuple은 함수의 값을 여러개 전달하는데 편하다