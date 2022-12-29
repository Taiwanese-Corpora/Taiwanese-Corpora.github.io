import csv
r = csv.reader(open('教育部閩南語辭典830650_11000900254_Attach1. - fullTable.tsv'), delimiter='\t')
header = next(r)
  
import re
for line in r:
    n_no = line[0]
    word_form = line[1]

    sense_no = 1
    example = line[sense_no + 6]
    while example:
        pattern='例：(?P<taiwanese>[^A-z]+)(?P<pinyin>.+)(?P<chinese>\(.*\))'
        pattern='例：(?P<taiwanese>[^A-z]+)(?P<pinyin>.+)'
        m = re.search(pattern=pattern, string=example)
        if m:
#           print(n_no, word_form, m.group('taiwanese'), m.group('pinyin'), m.group('chinese'), '\t'.join(line),  sep='\t')
            print(n_no, word_form, m.group('taiwanese'), m.group('pinyin'), '\t'.join(line),  sep='\t')
#       else:
 #          print(example)
        sense_no += 1
        example = line[sense_no + 6]
