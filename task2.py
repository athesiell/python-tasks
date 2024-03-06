def get_fractions(a_b: str, c_b: str) -> str:
    a = a_b.split('/')
    b = c_b.split('/')
    return f'{a_b} + {c_b} = {int(a[0]) + int(b[0])}/{b[1]}'

a_b = '1/3'
c_b = '5/3'
print(get_fractions(a_b, c_b))