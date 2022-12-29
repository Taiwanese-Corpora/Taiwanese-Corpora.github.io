import sys
twblg_file, translation_file, TBCL漢字分級表_file = sys.argv[1:4]

import csv
no_kokgi = dict([(n_no, kokgi_v) for kokgi_no, n_no, kokgi_v in csv.reader(open(translation_file), delimiter=",")])

TBCL漢字分級表 = dict([(漢字,級別) for 序號,漢字,等別,級別,書面字頻,口語字頻 in csv.reader(open(TBCL漢字分級表_file), delimiter=",")])
for 漢字,級別 in TBCL漢字分級表.items():
    continue
    print(漢字,級別)

twblg_reader = csv.reader(open(twblg_file), delimiter="\t")
for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader:
    kokgi_v = 級別 = ""
    if n_no in no_kokgi:
        kokgi_v = no_kokgi[n_no]
        if kokgi_v in TBCL漢字分級表 and len(詞目)==1:
            級別 =  TBCL漢字分級表[kokgi_v]
            print(n_no,詞目,kokgi_v,級別,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中, sep="\t")
