import csv
from nltk import bigrams
from collections import defaultdict


dd = defaultdict(list)
for MID, state, page, role, content, ps, book in csv.reader(open('modern.xls.tsv'), delimiter='\t'):
    sent = list(content)
    for bigram in bigrams(sent):
        dd[bigram].append(content)
#       print(bigram, content)

kw = '打'
for k, v in sorted(dd.items()):
    if kw in k:
        print(k, len(v), v)
