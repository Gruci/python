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

#list.index( value ) : 값을 이용하여 위치를 찾는 기능
#list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가 ->더하기 연산보다 성능이 좋다
#list.insert( index, value ) : 원하는 위치에 값을 추가
#list.sort( ) : 값을 순서대로 정렬
#list.reverse( ) : 값을 역순으로 정렬

my_list = [1, 2, 5, 6]
value = 3

def safe_index(my_list, value):
    if value in my_list:
        return my_list.index(value)
    else:
    	return print('{}는 my_list에 없다'.format(value))

safe_index(my_list,value)