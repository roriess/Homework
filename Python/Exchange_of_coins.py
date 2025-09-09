n = int(input('Enter your number: '))


coin_name = len('Vika')
coin_surname = len('Parfyonova')
coin_patronymic = len('Vadimovna')

the_biggest_coin = max(coin_name, coin_patronymic, coin_surname)
the_smallest_coin = min(coin_name, coin_patronymic, coin_surname)
medium_coin = (coin_surname + coin_name + coin_patronymic) - the_biggest_coin - the_smallest_coin

count_of_the_biggest_coin = 0
count_of_the_smallest_coin = 0
count_of_medium_coin = 0


while the_smallest_coin <= n:
    if the_biggest_coin <= n:
        n -= the_biggest_coin
        count_of_the_biggest_coin += 1

    if medium_coin <= n:
        n -= medium_coin
        count_of_medium_coin += 1

    if the_smallest_coin <= n:
        n -= the_smallest_coin
        count_of_the_smallest_coin += 1

if n != 0: print('-42!')
else: 
    print(
        f"Count of the biggest coin is {count_of_the_biggest_coin}\n"
        f"Count of medium coin is {count_of_medium_coin}\n"
        f"Count of the smallest coin is {count_of_the_smallest_coin}"
    )