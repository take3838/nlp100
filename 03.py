sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 単語に分解し、句読点を除去
words = [word.strip(",.") for word in sentence.split()]

# 各単語の文字数を取得
word_lengths = [len(word) for word in words]

print(word_lengths)