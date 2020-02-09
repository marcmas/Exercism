def to_rna(dna_strand):
    rna = ""
    dna_trans = {"G": "C", "C": "G", "T": "A", "A": "U"}
    for dna in dna_strand:
        rna += dna_trans[dna]
    return rna