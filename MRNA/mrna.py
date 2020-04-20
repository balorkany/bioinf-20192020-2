# -*- coding: utf-8 -*-

"""<-- hack to import from parent dir"""
import sys
sys.path.insert(0, '..')
"""-->"""

from utils import codon_table

# inverting codon_table
inverted_codon_table = {}

for codon, protein in codon_table.items():
    if protein in inverted_codon_table:
        inverted_codon_table[protein] += 1
    else:
        inverted_codon_table[protein] = 1


with open("rosalind_mrna.txt") as input_file:
    protein_string = input_file.read().strip()
    protein_string_with_stopcodon = protein_string + "*"

    num_of_inferred_rna = 1

    for p in protein_string_with_stopcodon:
        num_of_inferred_rna *= inverted_codon_table[p]
        num_of_inferred_rna %= 1000000

    print(num_of_inferred_rna)
