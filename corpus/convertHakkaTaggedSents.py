lines = open("Hakka/Hakka0.tsv").readlines()

i = 1
while i < len(lines):
    tagged_words = lines[i].split("\t")[24:]
    tagged_words = " ".join(tagged_words).strip()
    tagged_words = [w for w in tagged_words.split() if w.split("(")[0]]
    tagged_words = [word_tag.replace("(","/").strip(")") for word_tag in tagged_words]
    print(" ".join(tagged_words))
    i += 2
