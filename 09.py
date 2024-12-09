import random

def typoglycemia(text):
    words = text.split()
    scrambled = []
    for word in words:
        if len(word) <= 4:
            scrambled.append(word)
        else:
            middle = ''.join(random.sample(word[1:-1], len(word[1:-1])))
            scrambled.append(word[0] + middle + word[-1])
    return ' '.join(scrambled)

sample_text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = typoglycemia(sample_text)
print(result)

ー出力ー
I co’ndult believe that I culod acltaluy utnenrsadd what I was riaedng : the pnahmeeonl peowr of the huamn mind .
