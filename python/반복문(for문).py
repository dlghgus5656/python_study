# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first)
#     print(last)

# (a, b) = (1, 2)

import numbers


marks = [90, 25, 67, 45, 80]
number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

for mark in marks:
    number = number + 1
    if mark < 60:
        continue  # 컨티뉴를 만나면 다시 처음으로 돌아가서 실행
    print("%d번 학생은 합격입니다." % number)

sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)
