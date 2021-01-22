import os

f = open((os.path.dirname(__file__) + '\\fasta.fas'), 'r')
temp = f.readlines()
f.close()

index = []
for i in range(len(temp)):
    if '>' in temp[i]:
        index.append(i)

for i in range(len(index)):
    i = index[i]
    offset = 2
    while(True):
        if '>' not in temp[i+1] and i+offset < len(temp) and '>' not in temp[i+offset]:
            temp[i+1] += temp[i+offset]
            offset += 1
        else:
            break

for i in range(len(temp)):
    temp[i] = temp[i].replace('\n', '')
    temp[i] = temp[i].replace('>', '')

dna = []
for i in range(len(index)):
    i = index[i]
    dna.append((temp[i], temp[i+1]))

dnaString = dna[0][1]
for i in range(1, len(dna)):
    dnaString = dnaString.replace(dna[i][1], "")

rna = dnaString.replace('T', 'U')

codons = []
for i in range(0, len(rna),3):
    codons.append(rna[i:i+3])

protein = ""
stopCount = 0
for c in codons:
    if c == 'UUU' or c == 'UUC':
        protein += 'F'
    if c == 'UUA' or c == 'UUG':
        protein += 'L'
    if c == 'UCU' or c == 'UCC' or c == 'UCA' or c == 'UCG':
        protein += 'S'
    if c == 'UAU' or c == 'UAC':
        protein += 'Y'
    if c == 'UGU' or c == 'UGC':
        protein += 'C'
    if c == 'UGG':
        protein += 'W'
    if c == 'CUU' or c == 'CUC' or c == 'CUA' or c == 'CUG':
        protein += 'L'
    if c == 'CCU' or c == 'CCC' or c == 'CCA' or c == 'CCG':
        protein += 'P'
    if c == 'CAU' or c == 'CAC':
        protein += 'H'
    if c == 'CAA' or c == 'CAG':
        protein += 'Q'
    if c == 'CGU' or c == 'CGC' or c == 'CGA' or c == 'CGG' :
        protein += 'R'
    if c == 'AUU' or c == 'AUC' or c == 'AUA':
        protein += 'I'
    if c == 'AUG':
        protein += 'M'
    if c == 'ACU' or c == 'ACC' or c == 'ACA' or c == 'ACG':
        protein += 'T'
    if c == 'AAU' or c == 'AAC':
        protein += 'N'
    if c == 'AAA' or c == 'AAG':
        protein += 'K'
    if c == 'AGU' or c == 'AGC':
        protein += 'S'
    if c == 'AGA' or c == 'AGG':
        protein += 'R'
    if c == 'GUU' or c == 'GUC' or c == 'GUA' or c == 'GUG':
        protein += 'V'
    if c == 'GCU' or c == 'GCC' or c == 'GCA' or c == 'GCG':
        protein += 'A'
    if c == 'GAU' or c == 'GAC':
        protein += 'D'
    if c == 'GAA' or c == 'GAG':
        protein += 'E'
    if c == 'GGU' or c == 'GGC' or c == 'GGA' or c == 'GGG':
        protein += 'G'
    if c == 'UAA' or c == 'UAG' or c == 'UGA':
        stopCount += 1
    if stopCount >= 3:
        break

print(protein)