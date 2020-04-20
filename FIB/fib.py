# -*- coding: utf-8 -*-

with open("rosalind_fib.txt") as input_file:
    data = input_file.read()

    splitted_data = data.split(' ')
    n = int(splitted_data[0])
    k = int(splitted_data[1])
    # egy sorban: n, k = map(lambda x: int(x), data.spilt(' '))

    rabbits_list = [0, 1]

    for i in range(n - 1):
        rabbits_list.append(rabbits_list[-1] + k*rabbits_list[-2])

    print(rabbits_list[-1])
