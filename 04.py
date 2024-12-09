dict = {}
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text = text.replace(".", "")
list = text.split(" ")

# 1文字をキーにする単語の位置（1始まり）を格納したセット
num_list = {1, 5, 6, 7, 8, 9, 15, 16, 19}
for i, atom in enumerate(list, 1):
    if i not in num_list:
        temp = atom[:2]
        dict[temp] = i
    else:
        temp = atom[0]
        dict[temp] = i
print(dict)
