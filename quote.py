string1 = 'text'
string2 = "text2"
string3 = '{}도 {}도 둘다 문자열이다'.format(string1, string2)

print(string1, string2, string3)

quote = ' "를 표시할수있다!'
doublequote = " '를 표시할수 있다!"

print(quote)
print(doublequote)

long_string = """hello ""''"''"
word""" #'든 "든 한줄안에 끝내야 하는반면 ''' 또는 """는 여러줄 사용할수 있다

print(long_string)

#"'" 이런건 안됨