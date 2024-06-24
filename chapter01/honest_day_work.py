paint = int(input())

badge = int(input())

selling_price = int(input())

num_of_badges = paint // badge

leftover_paint = paint % badge

leftover_sale = leftover_paint * 1

# 총합
profit = num_of_badges * selling_price + leftover_sale

print(profit)
