sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 文を単語に分解し、句読点を除去
words = [word.strip(",.") for word in sentence.split()]

# 先頭1文字を取り出す単語の位置（1始まり）
one_char_indices = {1, 5, 6, 7, 8, 9, 15, 16, 19}

# 辞書を作成
word_map = {i + 1: (word[:1] if i + 1 in one_char_indices else word[:2]) for i, word in enumerate(words)}

print(word_map)
