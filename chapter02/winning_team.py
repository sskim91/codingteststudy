# https://dmoj.ca/problem/ccc19j1

apple_three = input()
if apple_three.isdigit() == False:
    exit('숫자가 아님')
apple_three = int(apple_three)
if apple_three < 0 or apple_three > 100:
    exit('범위를 벗어남 0< n <100')

apple_two = input()
if apple_two.isdigit() == False:
    exit('숫자가 아님')
apple_two = int(apple_two)
if apple_two < 0 or apple_two > 100:
    exit('범위를 벗어남 0< n <100')

apple_one = input()
if apple_one.isdigit() == False:
    exit('숫자가 아님')
apple_one = int(apple_one)
if apple_one < 0 or apple_one > 100:
    exit('범위를 벗어남 0< n <100')

banana_three = input()
if banana_three.isdigit() == False:
    exit('숫자가 아님')
banana_three = int(banana_three)
if banana_three < 0 or banana_three > 100:
    exit('범위를 벗어남 0< n <100')

banana_two = input()
if banana_two.isdigit() == False:
    exit('숫자가 아님')
banana_two = int(banana_two)
if banana_two < 0 or banana_two > 100:
    exit('범위를 벗어남 0< n <100')
    
banana_one = input()
if banana_one.isdigit() == False:
    exit('숫자가 아님')
banana_one = int(banana_one)
if banana_one < 0 or banana_one > 100:
    exit('범위를 벗어남 0< n <100')

apple_total = apple_three * 3 + apple_two * 2 + apple_one * 1
banana_total = banana_three * 3 + banana_two * 2 + banana_one * 1

if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else:
    print('T')
