import sys
zh_file, nan_file = sys.argv[1:]

import csv
zh_type_poses = csv.reader(open(zh_file), delimiter="\t")
nan_type_poses = csv.reader(open(nan_file), delimiter="\t")

#zh_types = set([type_pos[0] for type_pos in zh_type_poses if len(type_pos)==2])
zh_dict = dict([type_pos for type_pos in zh_type_poses if len(type_pos)==2])

#nan_types = set([type_pos[0] for type_pos in nan_type_poses if len(type_pos)==2])
nan_dict = dict([type_pos for type_pos in nan_type_poses if len(type_pos)==2])

#for common_type in zh_types & nan_types:
 #   print(common_type)
#print('zh_type', 'zh_pos', 'nan_pos')
print('nan_type', 'nan_pos')
for nan_type, nan_pos in nan_dict.items():
    if nan_type not in zh_dict:
#       zh_pos = zh_dict[nan_type]
#       if zh_pos == nan_pos:
        if nan_pos:
            print(nan_type, nan_pos.split(';')[0])
