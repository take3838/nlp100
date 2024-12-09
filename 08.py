def cipher(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(219 - ord(char))
        else:
            result += char
    return result

message = "Hello World!"
encrypted = cipher(message)
decrypted = cipher(encrypted)

print("暗号化:", encrypted)
print("復号化:", decrypted)
