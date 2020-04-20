# -*- coding: utf-8 -*-

with open("rosalind_subs.txt") as input_file:
    dna_string = input_file.readline().strip()
    substring = input_file.readline().strip()
    len_substring = len(substring)
    i = 0

    locations = []
    while i + len(substring) <= len(dna_string):
        if dna_string[i: i + len_substring] == substring:
            locations.append(i + 1)

        i += 1

    print(str(locations)[1:-1].replace(',', ''))
