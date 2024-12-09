def n_grams(seq, n):
    return [seq[i:i+n] for i in range(len(seq) - n + 1)]

# 文から単語bi-gram
text = "I am an NLPer"
words = text.split()
word_bigrams = n_grams(words, 2)

# 文から文字bi-gram
char_bigrams = n_grams(text, 2)

print("Word bi-grams:", word_bigrams)
print("Character bi-grams:", char_bigrams)
