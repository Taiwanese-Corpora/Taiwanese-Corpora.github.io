from nltk.corpus.reader.tagged import TaggedCorpusReader
root = "Hakka/"
fileids = "Hakka0_tagged"
hakka_sents = TaggedCorpusReader(root, fileids).sents()
hakka_tagged_sents = TaggedCorpusReader(root, fileids).tagged_sents()

import nltk
unigram_tagger = nltk.UnigramTagger(hakka_tagged_sents)
for sent in hakka_sents:
    tagged_sent = unigram_tagger.tag(sent)
    if None in [tag for word, tag in tagged_sent]:
        continue
    tagged_words = [word + "/" + tag for word, tag in tagged_sent]
    print(" ".join(tagged_words))
