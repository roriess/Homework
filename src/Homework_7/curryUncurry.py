def checkArgsCount(countOfArgs):
    if countOfArgs > 3 or countOfArgs < 0: return 0
    else: return 1

def sum3(x, y, z):
    return x + y + z


def curry(sum3, countElm):
    return lambda a: lambda b: lambda c: sum3(a, b, c)


def uncurry(sum3Curry, countElm):
    return lambda a, b, c: sum3Curry(a)(b)(c)


countOfArgs = int(input("Enter a count of args: "))

if (checkArgsCount(countOfArgs) == 1):
    argA, argB, argC = map(int, input("Enter args: ").split())
    
    sum3Curry = curry(sum3, countOfArgs)
    sum3Uncurry = uncurry(sum3Curry, countOfArgs)
    
    print(f'After curry: {sum3Curry(argA)(argB)(argC)}')
    print(f'After uncurry: {sum3Uncurry(argA, argB, argC)}')

else: print("Error: count of args is incorrect")