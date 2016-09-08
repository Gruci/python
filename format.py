number = 20
greeting = '안녕 안녕'
place = '문자열 포맷'
welcome = '하이 하이'

print (number,'번 손님', greeting, '.', place, '이다', welcome)

base = '{}번 손님, {}. {}이다 {}'
new_way = base.format(number, greeting, place, welcome)

print(base)
print(new_way)

print ('나는 {} ,너는 {}, 그래서 {}'.format
    (greeting, welcome, place))