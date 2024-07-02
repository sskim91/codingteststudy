burger = input()
if not burger.isdigit():
    exit('숫자가 아님')
burger = int(burger)
if burger < 1 or burger > 4:
    exit('범위를 벗어남 1< n <4')

side = input()
if not side.isdigit():
    exit('숫자가 아님')
side = int(side)
if side < 1 or side > 4:
    exit('범위를 벗어남 1< n <4')

drink = input()
if not drink.isdigit():
    exit('숫자가 아님')
drink = int(drink)
if drink < 1 or drink > 4:
    exit('범위를 벗어남 1< n <4')

dessert = input()
if not dessert.isdigit():
    exit('숫자가 아님')
dessert = int(dessert)
if dessert < 1 or dessert > 4:
    exit('범위를 벗어남 1< n <4')

if burger == 1:
    burger = 461
elif burger == 2:
    burger = 431
elif burger == 3:
    burger = 420
else:
    burger = 0

if drink == 1:
    drink = 130
elif drink == 2:
    drink = 160
elif drink == 3:
    drink = 118
else:
    drink = 0

if side == 1:
    side = 100
elif side == 2:
    side = 57
elif side == 3:
    side = 70
else:
    side = 0

if dessert == 1:
    dessert = 167
elif dessert == 2:
    dessert = 266
elif dessert == 3:
    dessert = 75
else:
    dessert = 0

total_calories = burger + side + drink + dessert

print('Your total Calorie count is ' + str(total_calories) + '.')
