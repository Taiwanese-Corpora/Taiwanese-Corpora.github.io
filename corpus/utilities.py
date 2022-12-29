from re import search
import csv

def concordance(kw,sentences):
    concordance_list = []
    for sentence in sentences:
        m = search(pattern='(?P<left>.*)(?P<kw>' + kw + ')(?P<right>.*)', string=sentence)
        if m:
            concordance_list.append([m.group('left'), m.group('kw'), m.group('right')])
    return concordance_list

from nltk.text import ConcordanceIndex
def generic_concordancer(kw, rows, target_column_num):
    header_row = next(rows)
    header_row.insert(target_column_num+1, "right_print")
    header_row.insert(target_column_num, "left_print")
    
    output_rows= [header_row]
    for row in rows:
        if kw in row[target_column_num]:
            CI = ConcordanceIndex(tokens=list(row[target_column_num]))
            ConcordanceLine = CI.find_concordance(word=kw)[0]
            row.insert(target_column_num+1, ConcordanceLine.right_print)
            row[target_column_num] = kw
            row.insert(target_column_num, ConcordanceLine.left_print)
            output_rows.append(row)
    return output_rows

def segmented_concordancer(kw, rows, target_column_num):
    header_row = next(rows)
    header_row.insert(target_column_num+1, "right_print")
    header_row.insert(target_column_num, "left_print")
    
    output_rows= [header_row]
    for row in rows:
        if kw in row[target_column_num]:
            CI = ConcordanceIndex(tokens=row[target_column_num].split("/"))
            ConcordanceLine = CI.find_concordance(word=kw)[0]
            row.insert(target_column_num+1, ConcordanceLine.right_print)
            row[target_column_num] = kw
            row.insert(target_column_num, ConcordanceLine.left_print)
            output_rows.append(row)
    return output_rows

import sys
from klokahAPI import klokahAPI
if __name__ == "__main__":
#   csvfile = open(sys.argv[1]) #corpora_root_dir/nan/liching-v3-all.tsv
 #  kw = sys.argv[2] # 打
  # for row in generic_concordancer(kw=kw, rows=csv.reader(csvfile, delimiter="\t"), target_column_num=2):
   #    print(row)

    d = sys.argv[1]
    txt = kw = sys.argv[2]
    target_column_num = int(sys.argv[3])

    rows = klokahAPI(d=int(d), txt=txt)
    for row in generic_concordancer(kw, rows, target_column_num):
        print(row)
