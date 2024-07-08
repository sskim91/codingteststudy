# https://dmoj.ca/problem/coci16c1p1

monthly_mb = int(input())
n = int(input())

excess = 0

for i in range(n):
    used = int(input())
    excess = excess + monthly_mb - used

print(excess+monthly_mb)
