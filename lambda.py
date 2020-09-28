sum = lambda d,e: d + e
print(sum (11,2))

def num (x):
    return lambda y : y * x
double_num = num(2)
print(double_num(40))
