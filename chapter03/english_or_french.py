# https://dmoj.ca/problem/ccc11s1

# 입력 받기
N = int(input())

english_words = 0
french_words = 0

# N개의 줄을 입력받아 문자 개수 세기
for _ in range(N):
    line = input()
    english_words += line.count('t') + line.count('T')
    french_words += line.count('s') + line.count('S')

# 결과 출력
if english_words > french_words:
    print("English")
else:
    print("French")

