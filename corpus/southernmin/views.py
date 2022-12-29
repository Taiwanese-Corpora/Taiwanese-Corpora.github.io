from django.http import HttpResponse
from klokahAPI import klokahAPI
from django.shortcuts import render
import csv
from utilities import generic_concordancer, concordance

nan_dir = 'corpora_root_dir/nan/'
Hakka_dir = 'corpora_root_dir/Hakka/'

from nltk.util import bigrams
import collections
def query_results(request):
    if 'corpus' not in request.GET:
        return HttpResponse('請選擇語料庫檔案')

    corpus_file = request.GET['corpus']
    kw = request.GET['kw']
    gram=request.GET['gram']

    if corpus_file.isnumeric(): # for 族語
        d = int(corpus_file)
        kw = kw.replace("'","’")
        text_chinese = klokahAPI(d=corpus_file, txt=kw)
        if kw[0] > '一' and kw < '龜':
            target_column_num = 1
        else:
            target_column_num = 0
        output_rows = generic_concordancer(kw,text_chinese,target_column_num)
        return render(request, 'generic_concordance_list.htm', {"output_rows": output_rows})

    elif corpus_file == "Hakka0.tsv":
        target_column_num = 10
        sentences=[]
#       for line in open(Hakka_dir+corpus_file):
 #          sentences.append(line)
        sentences = [row[target_column_num] for row in csv.reader(open(Hakka_dir+corpus_file), delimiter="\t")]
        rows = csv.reader(open(Hakka_dir+corpus_file), delimiter="\t")


    else: # for 閩南語
        if corpus_file == 'liching-all_v3.tsv':target_column_num = 2
        elif corpus_file == 'u-yan_new.tsv':   target_column_num = 2
        elif corpus_file == "教育部閩南語辭典830650_11000900254_Attach1-19230筆詞義含詞類-斷詞11168_noEvaluation.tsv": target_column_num = 8
        sentences = [row[target_column_num] for row in csv.reader(open(nan_dir+corpus_file), delimiter="\t")]
        rows = csv.reader(open(nan_dir+corpus_file), delimiter="\t")

    if gram:
        bigram_sents = collections.defaultdict(list)
        for words in sentences:
            for bigram in bigrams(words):
                bigram_sents[bigram].append(''.join(words))#content)
        gram_sents = {}
        for bigram, sents in bigram_sents.items():
            if gram in bigram:
                gram_sents[bigram] = sents
        return render(request, 'query_results.htm', {'corpus_file':corpus_file, 'kw_sents':sorted(gram_sents.items(), key=lambda item: len(item[1]), reverse=True)})

    elif kw:
        output_rows = generic_concordancer(kw,rows,target_column_num)
        return render(request, 'generic_concordance_list.htm', {"output_rows": output_rows})

    else:
        w1 = request.GET['w1']
        w21 = request.GET['w21']
        w22 = request.GET['w22']
        w23 = request.GET['w23']
        concordance_list=[]
        for w2 in [w21,w22,w23]:
            concordance_list+=concordance(kw=w1+w2,sentences=sentences)
        return render(request, 'concordance_list.htm', {'concordance_list': concordance_list})

from collections import defaultdict
def bigram_concordance(request,corpus_file,w1,w2):
    if corpus_file == 'liching-all_v3.tsv':target_column_num = 2
    elif corpus_file == 'u-yan_new.tsv':   target_column_num = 2
  # rows = csv.reader(open(nan_dir+corpus_file), delimiter="\t")
   #output_rows = generic_concordancer(w1+w2,rows,target_column_num)
   #return render(request, 'generic_concordance_list.htm', {"output_rows": output_rows})

    sentences = [row[target_column_num] for row in csv.reader(open(nan_dir+corpus_file), delimiter="\t")]

    bigram_sents = defaultdict(list)
    for words in sentences:
        for bigram in bigrams(words):
            bigram_sents[bigram].append(''.join(words))#content)

    concordance_list = []
    for sentence in bigram_sents[(w1,w2)]:
        i = sentence.index(w1+w2)
        left = sentence[:i]
        right = sentence[i+2:]
        concordance_list.append([left,w1+w2,right])
    return render(request, 'concordance_list.htm', {'concordance_list': concordance_list})
