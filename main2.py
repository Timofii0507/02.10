text = input("Введіть текст: ")
reserved_words = input("Введіть список зарезервованих слів через пробіли: ").split()
words = text.split()
for i in range(len(words)):
    if words[i] in reserved_words:
        words[i] = words[i].upper()
modified_text = ' '.join(words)
print("Змінений текст:")
print(modified_text)
