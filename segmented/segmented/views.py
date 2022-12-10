from django.http import HttpResponse
from klokahAPI import klokahAPI
from django.shortcuts import render
import csv
from utilities import generic_concordancer

corpora_dir = 'corpora/'

from nltk.util import bigrams
import collections
def query_results(request):

    corpus_file = request.GET['corpus']
    kw = request.GET['kw']


    if corpus_file == '教育部閩南語辭典830650_11000900254_Attach1-19230筆詞義含詞類-斷詞11168.tsv':
        target_column_num = 9
#       return HttpResponse('教育部閩南語辭典830650_11000900254_Attach1-19230筆詞義含詞類-斷詞11168.tsv')

#       sentences = [row[target_column_num] for row in csv.reader(open(nan_dir+corpus_file), delimiter="\t")]
        rows = csv.reader(open(corpora_dir+corpus_file), delimiter="\t")


    if kw:
        output_rows = generic_concordancer(kw,rows,target_column_num)
        return render(request, 'generic_concordance_list.htm', {"output_rows": output_rows})

