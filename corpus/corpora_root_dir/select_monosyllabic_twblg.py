from sys import argv
twblg_file = open(argv[1]) # nan/教育部閩南語辭典830650_11000900254_Attach1.tsv

from csv import reader
twblg_reader = reader(twblg_file, delimiter='\t')

for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader:
    words = 音讀.split('-')
    if len(words)==1 and len(words[0].split(" "))==1 and len(words[0].split('/'))==1 and '【' not in 音讀:
        print(音讀, 詞目)
