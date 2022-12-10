lines = open("corpora_root_dir/nan/MOEminPOStagged.tsv").readlines()

i = 0
while i < len(lines):
#   tagged_words = lines[i].split("\t")[24:]
#   tagged_words = " ".join(tagged_words).strip()
    tagged_words = [w for w in lines[i].split(")")]# if w.split("(")[0]]
    tagged_words = [word_tag.replace("(","/") for word_tag in tagged_words]
    print(" ".join(tagged_words).rstrip())
    i += 1
