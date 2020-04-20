# -*- coding: utf-8 -*-

"""<-- hack to import from parent dir"""
import sys
sys.path.insert(0, '..')
"""-->"""

from utils import mass_table

with open("rosalind_prtm.txt") as input_file:
    protein_string = input_file.read().strip()

    mass = 0

    for p in protein_string:
        mass += mass_table[p]

    print(mass)
