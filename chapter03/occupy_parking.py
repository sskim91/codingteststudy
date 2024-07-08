# https://dmoj.ca/problem/ccc18j2

N = input()
if not N.isdigit():
    exit('숫자가 아님')
N = int(N)
if not 1 <= N <= 100:
    exit('범위를 벗어남 1<=n<=100')

yesterday = input()
today = input()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1

print(occupied)
