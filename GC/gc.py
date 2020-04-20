# -*- coding: utf-8 -*-

"""<-- hack to import from parent dir"""
import sys
sys.path.insert(0, '..')
"""-->"""

from utils import fasta_reader


def gc_counter(dna_string):
    return (dna_string.count('G') + dna_string.count('C')) / len(dna_string)


gc_data = fasta_reader("rosalind_gc.txt")
#gc_data = fasta_reader("pr.fasta")
max_id = None
max_gc = None
for fasta_id, dna_string in gc_data.items():
    gc_content = gc_counter(dna_string)
    if max_gc is None or gc_content > max_gc:
        max_id = fasta_id
        max_gc = gc_content

print(max_id)
print(max_gc * 100)


