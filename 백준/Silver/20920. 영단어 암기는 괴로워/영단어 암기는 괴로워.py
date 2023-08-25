#딕셔너리 정렬
n, m = map(int, input().split())
word_list = {}

for _ in range(n):
    word = input()
    if len(word) >= m:
        if word not in word_list:
            word_list[word] = 1
        else:
            word_list[word] += 1

word_list = sorted(word_list.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, num in word_list:
    print(word)