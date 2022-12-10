import sys,csv

twblg_file = open(sys.argv[1])
twblg_reader = csv.reader(twblg_file, delimiter="\t")
headers = next(twblg_reader)
for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader:
#   POS = 釋義1.replace("1.", "").split("】")[0]
    POS = 釋義1.replace("1.", "")
    try:
        if POS[0] == "【":
    #       print(n_no, 詞目, 音讀, POS.split("【")[1], sep="\t")
            print(n_no, 詞目, 音讀, POS[1], sep="\t")
    except:
        pass
