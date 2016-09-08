list = [1,2,3,4,5]

for i, v in enumerate(list):
    print('{}번쨰 값: {}'.format(i,v))

for a in enumerate(list):
    print('{}번쨰 값: {}'.format(a[0],a[1]))

for a in enumerate(list):
    print('{}번쨰 값: {}'.format(*a))

#tuple을 활용한 packing unpacking in list

ages = {
    'Ted':23,
    'Jane':51,
    'Kim':18
}

for a in ages.items():
    print('{}의 나이: {}'.format(*a))

#in dictionary