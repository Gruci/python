wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}
#print(wintable['가위'])

#words = ['a', 'b', 'c']
#print(words[0])

def rsp(mine,yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

result = rsp ('가위', '바위')
#print(result)

messages = {
    'win':'승리',
    'drow':'비김',
    'lose':'졌다..'
}

print(messages[result])

dict = {
    'one':1,
    'two':2
}

print(dict)

dict['one'] = 11 #딕셔너리의 값 변경

print(dict)

dict['three'] = 3 #딕셔너리의 값 추가

print(dict)

del(dict['one']) #딕셔너리의 값 삭제

print(dict)

list = [1, 2, 3, 4, 5]
print(list.pop(2))  #list의값을 pop을 통해서 삭제

print(list)

print(dict.pop('two'))  #dict의 값을 pop을 통해서 삭제

print(dict)
