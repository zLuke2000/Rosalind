from Bio import Entrez
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term='"Atta"[Organism] AND rbcL[Gene]')
record = Entrez.read(handle)
print(record)
