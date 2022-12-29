dir = 'corpus_files/'
dir = 'corpora_root_dir/nan/'

import csv

def load_u_yan():
    sentences = []
    file = open(dir + 'u-yan.tsv')
    for UID, content, so, ti, pl, ps, book in csv.reader(file, delimiter='\t'):
        sentences.append(content)
    return sentences

def load_u_yan_new():
    sentences = []
    file = open(dir + 'u-yan_new.tsv')
    for UID, role, content, issuePageLine, book in csv.reader(file, delimiter='\t'):
        sentences.append(content)
    return sentences

if __name__ == '__main__':
    for sentence in load_u_yan_new():
        print(sentence)
