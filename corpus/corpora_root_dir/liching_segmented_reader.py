from nltk.text import Text

from sys import argv

from csv import reader
liching_segmented_words = []
for AID,role, content,content_segmented, number, songtablet, action, book in reader(open(argv[1]), delimiter='\t'):
#   print(AID, role, content, content_segmented, number, songtablet, action, book)
    liching_segmented_words += content_segmented.split('/')

if __name__ == '__main__':
    t = Text(liching_segmented_words)
    for w in t.words():
        print(w)
    for w1, w2 in t.collocation_list():
        print(w1, w2)
