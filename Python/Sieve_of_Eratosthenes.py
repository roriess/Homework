def sieve_of_eratosthenes(n):
    all_number = [True]*(n + 1)
    all_number[0] = all_number[1] = False

    for i in range(2, n + 1):
        if all_number[i]:
            for j in range(i*i, n + 1, i):
                if j % i == 0: all_number[j] = False

    simple_numbers = []
    for x in range(n + 1):
        if all_number[x] == True: simple_numbers.append(x)
    
    return simple_numbers


print(sieve_of_eratosthenes(n = int(input())))