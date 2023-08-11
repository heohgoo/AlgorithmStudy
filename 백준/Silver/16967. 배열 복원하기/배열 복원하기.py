import sys
input = sys.stdin.readline
h, w, x, y = map(int, input().split())
B  = []
for i in range(h+x):
	B.append(list(map(int, input().split())))

A = [[0]*(w+y) for _ in range(h+x)]
for i in range(h+x):
	for j in range(w+y):
    		# 겹치지 않는 부분은 그대로 들어감 , 겹치는 부분은 B 배열에서 A 배배열의 x, y만큼 돌아가서 빼줌
		if x <= i < x+h and y <= j < y+w:
			A[i][j] = B[i][j] - A[i-x][j-y]
		elif i < x or i >= x+h:
			A[i][j] = B[i][j]
		elif j < y or j >= y+w:
			A[i][j] = B[i][j]


for i in range(h):
	for j in range(w):
		print(A[i][j], end = ' ')
	print()