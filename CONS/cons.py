# -*- coding: utf-8 -*-

"""<-- hack to import from parent dir"""
import sys
sys.path.insert(0, '..')
"""-->"""

from utils import fasta_reader

cons_data = fasta_reader("rosalind_cons.txt")

a = []
c = []
g = []
t = []

first = True
for _, dna_string in cons_data.items():
    if first:
        a = [0] * len(dna_string)
        c = [0] * len(dna_string)
        g = [0] * len(dna_string)
        t = [0] * len(dna_string)
        first = False

    for ind, dna_char in enumerate(dna_string):
        if dna_char == 'A':
            a[ind] += 1
        elif dna_char == 'C':
            c[ind] += 1
        elif dna_char == 'G':
            g[ind] += 1
        elif dna_char == 'T':
            t[ind] += 1
        else:
            raise ValueError("Ismeretlen nuklein-sav: {}".format(dna_char))

cons_string = ""
for i in range(len(a)):
    cons_ertek = max(a[i], c[i], g[i], t[i])

    if a[i] == cons_ertek:
        cons_string += 'A'
    elif c[i] == cons_ertek:
        cons_string += 'C'
    elif g[i] == cons_ertek:
        cons_string += 'G'
    else:
        cons_string += 'T'

print(cons_string)
print("A: {}".format(str(a)[1:-1].replace(',', '')))
print("C: {}".format(str(c)[1:-1].replace(',', '')))
print("G: {}".format(str(g)[1:-1].replace(',', '')))
print("T: {}".format(str(t)[1:-1].replace(',', '')))
