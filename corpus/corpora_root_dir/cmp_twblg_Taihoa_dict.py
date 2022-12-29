import sys
twblg_file, nan_file = sys.argv[1:3]

import csv
twblg_reader = csv.reader(open(twblg_file), delimiter="\t")
#twblg_lexicon = [詞目 for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader]
twblg_dict = dict([(詞目,釋義1) for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader])

nan_type_poses = csv.reader(open(nan_file), delimiter="\t")
nan_dict = dict([type_pos for type_pos in nan_type_poses if len(type_pos)==2])

print("nan_type", "nan_pos", sep=",")
for nan_type, nan_poses in nan_dict.items():
#   if nan_type not in twblg_lexicon:
    if nan_type in twblg_dict:
        nan_pos = nan_poses.split(';')[0]
        if nan_pos:
            print(nan_type, nan_poses, twblg_dict[nan_type], sep=",")
