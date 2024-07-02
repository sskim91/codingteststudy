# https://dmoj.ca/problem/ccc15j1

month = int(input())
day = int(input())

if month < 1 or month > 12:
    print("Invalid month")
    exit()
if day < 1 or day > 31:
    print("Invalid day")
    exit()

if month < 2:
    print('Before')
elif month == 2:
    if day == 18:
        print('Special')
    elif day > 18:
        print('After')
    else:
        print('Before')
else:
    print('After')
