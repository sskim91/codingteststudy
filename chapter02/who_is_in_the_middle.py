# https://dmoj.ca/problem/ccc07j1

bear1 = input()
if not bear1.isdigit():
    exit('숫자가 아님')
bear1 = int(bear1)
if bear1 > 100:
    exit('범위를 벗어남 n<100')

bear2 = input()
if not bear2.isdigit():
    exit('숫자가 아님')
bear2 = int(bear2)
if bear2 > 100:
    exit('범위를 벗어남 n<100')

bear3 = input()
if not bear3.isdigit():
    exit('숫자가 아님')
bear3 = int(bear3)
if bear3 > 100:
    exit('범위를 벗어남 n<100')

if (bear1 > bear2 and bear1 < bear3) or (bear1 > bear3 and bear1 < bear2):
    print(bear1)
elif (bear2 > bear1 and bear2 < bear3) or (bear2 > bear3 and bear2 < bear1):
    print(bear2)
else:
    print(bear3)
