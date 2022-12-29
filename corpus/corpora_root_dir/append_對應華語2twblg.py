import sys
twblg_file, translation_file = sys.argv[1:3]

import csv
no_kokgi = dict([(n_no, kokgi_v) for kokgi_no, n_no, kokgi_v in csv.reader(open(translation_file), delimiter=",")])
for n_no, kokgi_v in no_kokgi.items():
    continue
    print(n_no, kokgi_v)

twblg_reader = csv.reader(open(twblg_file), delimiter="\t")
for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader:
    kokgi_v = ""
    if n_no in no_kokgi:
        kokgi_v = no_kokgi[n_no]
        print(n_no,詞目,kokgi_v,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中)
