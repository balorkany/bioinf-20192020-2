# -*- coding: utf-8 -*-

"""<-- hack to import from parent dir"""
import sys
sys.path.insert(0, '..')
"""-->"""

from utils import fasta_reader
from itertools import combinations


grph_data = fasta_reader("rosalind_grph.txt")

edges = []
for key1, key2 in combinations(grph_data.keys(), 2):
    if grph_data[key1][:3] == grph_data[key2][-3:]:
        edges.append("{} {}".format(key2, key1))

    if grph_data[key2][:3] == grph_data[key1][-3:]:
        edges.append("{} {}".format(key1, key2))

for edge in edges:
    print(edge)
