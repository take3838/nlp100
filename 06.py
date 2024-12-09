def char_bigrams(text):
    result = set()
    for i in range(len(text) - 1):
        result.add(text[i:i+2])
    return result

X = char_bigrams("paraparaparadise")
Y = char_bigrams("paragraph")

# 和集合
union = X | Y
# 積集合
intersection = X & Y
# 差集合
difference = X - Y

print("和集合:", union)
print("積集合:", intersection)
print("差集合:", difference)
print("'se' in X:", 'se' in X)
print("'se' in Y:", 'se' in Y)
