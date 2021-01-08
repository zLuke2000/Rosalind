import os

f = open((os.path.dirname(__file__) + '\\fasta.fas'), 'r')
inputNum = []
temp = f.readlines()
#temp = temp.replace('\n', '')
#temp = temp.split(">")
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
    dna

GCpercentageList = []
for n in dna:
    count_GC = 0
    for c in n[1]:
        if c == 'G' or c == 'C':
            count_GC += 1
    percentage = count_GC/len(n[1])*100
    GCpercentageList.append((n[0], percentage))

maxGCcontent = 0
for i in GCpercentageList:
    if i[1] > maxGCcontent:
        maxGCcontent = i[1]
        dnaID = i[0]

print(dnaID)
print("%.6f" % maxGCcontent)