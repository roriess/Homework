from inspect import signature

def sum3(x, y, z):
    return x + y + z


def curry(sum3, countElm):
    return lambda a: lambda b: lambda c: sum3(a, b, c)


def uncurry(sum3Curry, countElm):
    return lambda a, b, c: sum3Curry(a)(b)(c)


sum3Curry = curry(sum3, 3)
sum3Uncurry = uncurry(sum3Curry, 3)

print(signature(sum3Curry))
print(sum3Curry(1)(2)(3))
print(sum3Uncurry(1, 2, 3))
