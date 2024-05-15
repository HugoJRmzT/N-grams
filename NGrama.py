import nltk.corpus

sentences = nltk.corpus.brown.sentences()

len(sentences)

sentences[0]

n_grams = {}

for sentence in sentences:
    words = [words for word in sentence if word[0].isalpha()]

    for ix in range(len(words)-1):
        try:
            n_grams[words[ix]].append(words[ix+1])
        except KeyError as _:
            n_grams[words[ix]] = []
            n_grams[words[ix]].append(words[ix+1])

        n_grams