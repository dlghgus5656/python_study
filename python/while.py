# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1

# numbers = [1, 2, 1, 2, 1, 2, 1, 2]

# while 1 in numbers:
#      numbers.remove(1)

# print(numbers)

# while 1 in numbers:
#     numbers.remove(1)

#     print(numbers) # print문을 반복문 안에 포함시키면 출력값이 달라진다.

import time

first = time.time()
while first + 5 >= time.time():
    pass
print("프로그램이 종료되었습니다.")  # 5초 뒤에 종료되는 반복문