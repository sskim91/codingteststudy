# https://dmoj.ca/problem/dmopc16c1p0

# 입력 받기
width = int(input())
cheesiness = int(input())

# 입력 사양 확인
if not (1 <= width <= 3 and 0 <= cheesiness <= 100):
    exit("입력 에러")

# 조건에 따른 출력
if width == 3 and cheesiness >= 95:
    print("C.C. is absolutely satisfied with her pizza.")
elif width == 1 and cheesiness <= 50:
    print("C.C. is fairly satisfied with her pizza.")
else:
    print("C.C. is very satisfied with her pizza.")
