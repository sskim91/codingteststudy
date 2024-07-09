# https://dmoj.ca/problem/ccc11s2

N = int(input())

student_answer = ''
correct_answer = ''

for i in range(N):
    student_answer += input()

for i in range(N):
    correct_answer += input()

answer = 0  # 맞은 개수 초기화

for i in range(N):
    if student_answer[i] == correct_answer[i]:
        answer += 1

print(answer)