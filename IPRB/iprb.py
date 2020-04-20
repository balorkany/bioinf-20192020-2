# -*- coding: utf-8 -*-

with open("rosalind_iprb.txt") as input_file:
    data = input_file.read()

    splitted_data = data.split(' ')
    k = int(splitted_data[0])
    n = int(splitted_data[1])
    m = int(splitted_data[2])
    # egy sorban: k, n, m = map(lambda x: int(x), data.spilt(' '))

    osszeg = k + n + m

    recessziv = m*(m - 1) + n*(n-1)*0.25 + 2*n*m*0.5
    nevezo = osszeg * (osszeg - 1)

    print(1 - recessziv / nevezo)
