word = input()
words = []

for i in range(len(word)):
    words.append(word[i:])

words.sort()

for w in words:
    print(w)