text_1 = "パトカー"
text_2 = "タクシー"
temp = ""
for t0, t1 in zip(text_1, text_2):
    temp += t0
    temp += t1
print(temp)
