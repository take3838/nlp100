def n_grams(seq, n):
    result = []
    for i in range(len(seq) - n + 1):
        result.append(seq[i:i+n])
    return result

# 文から単語bi-gram
text = "I am an NLPer"
words = text.split()
word_bigrams = n_grams(words, 2)

# 文から文字bi-gram (空白を除外)
text_without_spaces = text.replace(" ", "")
char_bigrams = n_grams(text_without_spaces, 2)

print("単語 bi-grams:", word_bigrams)
print("文字 bi-grams:", char_bigrams)
