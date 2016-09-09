try:
    list = []
    print(list[0])

    text = 'abc'
    number = int(text)
except Exception as e: 
    #Exception as ~ = 에러의 종류를 알고싶을때 
    #except:만 한다면 에러가 발생할경우 전부 에러처리
    print('{}에러가 발생했습니다.'.format(e))