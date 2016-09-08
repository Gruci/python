ages = {
    'Ted':23,
    'Jane':51,
    'Kim':18
} # key:value

'''
for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)
'''
for key in ages.keys():
    print('{}의 나이는 {} 입니다.'.format(key,ages[key]))

#or

for key in ages:
    print('{}의 나이는 {} 입니다.'.format(key,ages[key]))

for key,value in ages.items():
    print('{}의 나이는 {} 입니다.'.format(key,value))

#딕셔너리는 순서를 보장해주지 않는다