dna = "ATTACGCGTCCTGACCTATCGAAAAATCTCTTATACGCTATCCATTGCGAAAACATGACCGATAGTTGGGGCCGACATGCGACTTCAAAACAATCGTAAAGTCTTCCCATCTGATTTTAGGTTGTCCCTGGCTAGCCCAACTCAGCCTGTACCCAGGTCGAGTAAAGTGAGTTCTGCACATCGGCAATAATCTTCCATAAGGGGATCTCCATCACGCGTATACACTGATATCATTGGTGCACTATCGGCTGAACGTACCGCGGCTATTGGTTTATCCCATCTACTGCTAGGCGCCGTGATTCCTCAGGCCGGTCTCTCAAGGACTGCTAAACACGTCGTCAGTGCGCCTTTATTCGTGCGGTCATGTGTTGTCTTCAGACTGTCGCCCGTCCGACAAGAACTGAACCGATTATAACTTGGCGCCGCCCCGCCGGGTGTCCCGGAGCGAGGCTAACTTAGTTAATCCATCGGTCGCATTGCAAGAAAACGTGGGGGCAAGTAGGAGATTATGGACCTTGCATTCAACCGTCTGTTATAACACATTGGTGGAAAATATCGCATGTGTGGTCCAGTTATATGCAGAGACACGAATAACACCATGCGGAAGATCAGCCCGCTGACCATCTACACACTGACTAGAACTGGCGACTTGTTGATTTCGAGTTTGGCATGCCTTGATAGTCTGGCAGAAGATAAATTCGACGATGCCGAATTAAACCCCGTCTCAAACTGTAGTTTGTCACCGGCTCGCGCGAGGCAGTGAATGCCTAGGCACACATAGCGTGCGTTACGCAAGAGGCCATCTGCCCGTTGCCAGGACGAGATTGATGTCTAGTATCATCCCACCCCAACTCGATATGGTTGGATTGAGCC"
conteggio = [0, 0, 0, 0]
#            A, C, G, T

for c in dna:
    if(c == 'A'):
        conteggio[0] += 1
    if(c == 'C'):
        conteggio[1] += 1
    if(c == 'G'):
        conteggio[2] += 1
    if(c == 'T'):
        conteggio[3] += 1
print(conteggio[0], conteggio[1], conteggio[2], conteggio[3])

""" OPPURE """

conteggio[0] = dna.count('A')
conteggio[1] = dna.count('C')
conteggio[2] = dna.count('G')
conteggio[3] = dna.count('T')
print(conteggio[0], conteggio[1], conteggio[2], conteggio[3])