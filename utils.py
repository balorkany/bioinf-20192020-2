
def reverse_compliment(dna_string):
    compliment_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    reverse_comp = ""

    for c in dna_string[::-1]:
        reverse_comp += compliment_map[c]

    return reverse_comp


mass_table = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


codon_table = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


# FASTA Reader
def fasta_reader(path, with_ordered_keys=False):
    with open(path) as fasta_file:
        fasta_dict = {}
        keys_in_order = []
        fasta_data = ''
        fasta_key = ''
        for line in fasta_file.readlines():
            stripped_line = line.strip()
            if stripped_line and stripped_line[0] == '>':
                if fasta_data:
                    fasta_dict[fasta_key] = fasta_data
                    keys_in_order.append(fasta_key)

                fasta_key = stripped_line[1:]
                fasta_data = ""
            else:
                fasta_data += stripped_line
        fasta_dict[fasta_key] = fasta_data
        keys_in_order.append(fasta_key)

        if with_ordered_keys:
            return fasta_dict, keys_in_order

        return fasta_dict


def dna_to_rna(dna_string):
    return dna_string.replace('T', 'U')


def rna_to_protein(rna_codon):
    if rna_codon in codon_table:
        return codon_table[rna_codon]
    else:
        raise ValueError("Hianyzo codon: {0}".format(rna_codon))
    
    
def read_reading_frames(rna_string):
    candidate_proteins = []
    n = len(rna_string)

    for maradek in [0, 1, 2]:
        i = 0
        while 3 * (i + 1) + maradek <= n:
            codon = rna_string[3 * i + maradek: 3 * (i + 1) + maradek]
            ammino = rna_to_protein(codon)

            if ammino == 'M':
                j = 3 * (i + 1) + maradek
                candidate_protein = "M"
                reading = True

                while j + 3 <= n and reading:
                    inner_codon = rna_string[j: j + 3]
                    inner_ammino = rna_to_protein(inner_codon)

                    if inner_ammino == "*":
                        reading = False
                        candidate_proteins.append(candidate_protein)

                    else:
                        candidate_protein += inner_ammino

                    j += 3

            i += 1

    return candidate_proteins


def hamming_distance(s1, s2):
    hd = 0
    for c1, c2 in zip(s1, s2):
        if not c1 == c2:
            hd += 1

    return hd
