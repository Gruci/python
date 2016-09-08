list = ['A', 'B', 'C']

print(list)

list[2] = 'D'

print(list)

list[-1] = 'E'

print(list)

list.append('F')

print(list)

list2 = list + ['G']

print(list2)

ask = 'F'
answer = ask in list2
print(answer)

ask2 = 'R'
if not ask2 in list2:
    print('{}는 list2에 없다'.format(ask2))

del list[3] #list 배열 하나 삭제
print(list)

list2.remove('G') #list안에 선택 삭제
print(list2)
