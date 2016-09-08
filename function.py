def print_sqrt(a, b, c): # 함수의 선언!
    r1 = (-b + (b ** 2 - 4 * a *  c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a *  c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {} '.format(r1,r2))

x = 1
y = 2
z = -8

print_sqrt(x, y, z)

def print_round(number):
    runded = round(number) # round() 반올림
    print(rounded)

print_round(2.2)
print_round(4.6)

def add_10(value):
    result = value + 10
    return result

n = add_10(40)
print(n)

def print_sqrt_rt(a, b, c): # 함수의 선언!
    r1 = (-b + (b ** 2 - 4 * a *  c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a *  c) ** 0.5) / (2 * a)
    return r1, r2

r1, r1 = print_sqrt_rt(x, y, z)
print('해는 {} 또는 {} '.format(r1,r2))
