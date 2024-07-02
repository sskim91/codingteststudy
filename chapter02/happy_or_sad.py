# https://dmoj.ca/problem/ccc15j2

feeling = input()
if len(feeling) < 0 or len(feeling) > 255:
    exit('입력줄 초과')

happy_count = feeling.count(":-)")
sad_count = feeling.count(":-(")

if happy_count == 0 and sad_count == 0:
    print("none")
elif happy_count == sad_count:
    print("unsure")
elif happy_count > sad_count:
    print("happy")
else:
    print("sad")
