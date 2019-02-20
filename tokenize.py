#!/bin/python3

from pprint import pprint
import numpy as np

# Function defs

def tokenize(corpus : str) -> list:
    tokens = []
    for sentence in corpus:
        tokens.append(sentence.split())
    return tokens

def generate_center_context_pair(tokens, window: int) -> dict:
    pairs = dict()
    for row in tokens:
        for idx, center_word in enumerate(row):
            pairs.setdefault(center_word, [])
            for i in range(idx - window, idx + window + 1):
                if (i >= 0 and i != idx and i < len(row)):
                    pairs[center_word].append(row[i])
    return pairs

def code_in_the_blog() -> dict:
    corpus = [
            'he is a king',
            'she is a queen',
            'he is a man',
            'she is a woman',
            'warsaw is poland capital',
            'berlin is germany capital',
            'paris is france capital',
    ]
    def tokenize_corpus(corpus):
        tokens = [x.split() for x in corpus]
        return tokens

    tokenized_corpus = tokenize_corpus(corpus)
    vocabulary = []
    for sentence in tokenized_corpus:
        for token in sentence:
            if token not in vocabulary:
                vocabulary.append(token)

    word2idx = {w: idx for (idx, w) in enumerate(vocabulary)}
    idx2word = {idx: w for (idx, w) in enumerate(vocabulary)}

    vocabulary_size = len(vocabulary)
    window_size = 2
    idx_pairs = []
    # for each sentence
    for sentence in tokenized_corpus:
        indices = [word2idx[word] for word in sentence]
        # for each word, threated as center word
        for center_word_pos in range(len(indices)):
            # for each window position
            for w in range(-window_size, window_size + 1):
                context_word_pos = center_word_pos + w
                # make soure not jump out sentence
                if context_word_pos < 0 or context_word_pos >= len(indices) or center_word_pos == context_word_pos:
                    continue
                context_word_idx = indices[context_word_pos]
                idx_pairs.append((indices[center_word_pos], context_word_idx))

    idx_pairs = np.array(idx_pairs) # it will be useful to have this as numpy array

    for center, context in idx_pairs:
        print(vocabulary[center], vocabulary[context])

corpus = [
        "he is a king",
        "she is a queen",
        "he is a man",
        "she is a woman",
        "warsaw is poland capital",
        "berlin is germany capital",
        "paris is france capital",
        # "Sxi este juna kaj bela",
]

def main():
    pprint(corpus)

    tokens = tokenize(corpus)
    cc_pair = generate_center_context_pair(tokens, 2)

    pprint(cc_pair)

    print("Printing from the code from the blog.")

    code_in_the_blog()

if __name__ == "__main__":
    main()