from re import search
import csv

from nltk.text import ConcordanceIndex
def generic_concordancer(kw, rows, target_column_num):
    header_row = next(rows)
    header_row.insert(target_column_num+1, "right_print")
    header_row.insert(target_column_num, "left_print")
    
    output_rows= [header_row]
    for row in rows:
        if kw in row[target_column_num].split(" "):
            CI = ConcordanceIndex(tokens=row[target_column_num].split(' '))
            ConcordanceLine = CI.find_concordance(word=kw)[0]
            row.insert(target_column_num+1, ConcordanceLine.right_print)
            row[target_column_num] = kw
            row.insert(target_column_num, ConcordanceLine.left_print)
            output_rows.append(row)
    return output_rows

import sys
if __name__ == "__main__":
    csvfile = open(sys.argv[1])
    kw = sys.argv[2]
    target_column_num = sys.argv[3]

    for row in generic_concordancer(kw=kw, rows=csv.reader(csvfile, delimiter="\t"), target_column_num=int(target_column_num)):
        print(row)
