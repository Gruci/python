str = 'Hello word!'
#string은 리스트와 매우 비슷하다

if 'H' in str:
    print('H는 {} 안에 있습니다'.format(str))

characters = list('abcdef')
print(characters)

words = "Hello Wordl 프로그래밍 사이트"
words_list = words.split()

print(words_list)

time_str = '13:45:33'
time_list = time_str.split(':')

print(time_list)

time_list_str = ':'.join(time_list)
print(time_list_str)

words_list_str = ' '.join(words_list)
print(words_list_str)