# -*- coding: utf-8 -*-

"""<-- hack to import from parent dir"""
import sys
sys.path.insert(0, '..')
"""-->"""

from utils import rna_to_protein

with open("rosalind_prot.txt") as input_file:
    rna_string = input_file.readline().strip()
    protein = ""

    for i in range(len(rna_string) // 3):
        codon = rna_string[i*3:i*3+3]
        prot = rna_to_protein(codon)
        if not prot == '*':
            protein += prot

    print(protein)
