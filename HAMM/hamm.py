# -*- coding: utf-8 -*-

with open("rosalind_hamm.txt") as input_file:
    s1 = input_file.readline()
    s2 = input_file.readline()

    hd = 0
    for c1, c2 in zip(s1, s2):
        if not c1 == c2:
            hd += 1

    print(hd)
