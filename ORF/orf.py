# -*- coding: utf-8 -*-

"""<-- hack to import from parent dir"""
import sys
sys.path.insert(0, '..')
"""-->"""

from utils import fasta_reader, reverse_compliment, dna_to_rna, read_reading_frames

orf_data_dict = fasta_reader("rosalind_orf.txt")

orf = list(orf_data_dict.values())[0]
orf_revc = reverse_compliment(orf)

orf_rna = dna_to_rna(orf)
orf_revc_rna = dna_to_rna(orf_revc)


orf_cand_prot = read_reading_frames(orf_rna)
orf_revc_cand_prot = read_reading_frames(orf_revc_rna)


candidates = set(orf_cand_prot + orf_revc_cand_prot)

for c in candidates:
    print(c)


