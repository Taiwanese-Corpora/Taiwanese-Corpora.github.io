from django.http import HttpResponse
from klokahAPI import klokahAPI
from django.shortcuts import render
import csv

from utility import generic_concordancer
from klokahAPI import klokahAPI

corpora_dir = 'corpora/'

from nltk.util import bigrams
import collections
def query_results(request):
    if 'corpus' not in request.GET:
        return HttpResponse("請回上頁選擇語料庫")
    corpus_file = request.GET['corpus']
    kw = request.GET['kw']
    if corpus_file == '教育部閩南語常用詞辭典.tsv':
        target_column_num = 8
        rows = csv.reader(open(corpora_dir+corpus_file), delimiter="\t")

        output_rows = generic_concordancer(kw,rows,target_column_num)
        if len(output_rows) == 1:
            return HttpResponse("抱歉，辭典未收錄此字。")
        else:
            return render(request, 'generic_concordance_list.htm', {"output_rows": output_rows})
    elif corpus_file in [str(d) for d in range(1,44)]:
        rows = klokahAPI(d=corpus_file, txt=kw)
        if len(rows) == 1:
            return HttpResponse("抱歉，族語E樂園API查無此字, 可回上頁繼續查詢其他字詞。")
        else:
#           return HttpResponse(len(rows))
            return render(request, 'generic_concordance_list.htm', {"output_rows": rows})
