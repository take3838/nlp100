def char_bigrams(text):
    result = set()
    for i in range(len(text) - 1):
        result.add(text[i:i+2])
    return result

X = char_bigrams("paraparaparadise")
Y = char_bigrams("paragraph")

print("X:", X)
print("Y:", Y)

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

ー出力ー
X: {'ar', 'ap', 'ad', 'di', 'pa', 'ra', 'is', 'se'}
Y: {'ar', 'ap', 'pa', 'ag', 'ph', 'ra', 'gr'}
和集合: {'ar', 'ap', 'ad', 'di', 'pa', 'ag', 'ph', 'ra', 'is', 'gr', 'se'}
積集合: {'ar', 'pa', 'ra', 'ap'}
差集合: {'ad', 'di', 'se', 'is'}
'se' in X: True
'se' in Y: False
