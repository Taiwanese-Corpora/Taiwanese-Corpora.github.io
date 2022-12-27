import sys, csv
twblg_lines = open(sys.argv[1]) #教育部閩南語辭典830650_11000900254_Attach1.tsv 
twblg_reader = csv.reader(twblg_lines, delimiter="\t")
headers = next(twblg_reader)
lexicon = [詞目 for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader]


lines = sys.stdin.readlines()

for line in lines:
    for word in line.split():
        if word not in lexicon:
            print(word)
