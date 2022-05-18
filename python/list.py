# 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()
# 리스트 뒤집기: reversed()
# 현재 인덱스가 몇 번째인지 확인하기: enumerate()
# 딕셔너리로 쉽게 반복문 작성하기: items()

# min(리스트) or min(숫자, 숫자, 숫자, ...)
# max(리스트) or max(;;)
# sum(리스트)
# for i in reversed(리스트):
# for i, element in enumerate(리스트):
# for key, value in 딕셔너리.items():
# ----------------------------------------------
# a = [0, 1, 2, 3, 4, 5]
# reversed_a = reversed(a)
# print(list(reversed_a)) # list를 안써주면 에러가난다.
# print(list(reversed_a)) # reversed는 일회용 함수로써 한번더 사용하게 되면 빈값을 출력한다.
# list(reversed(리스트)): 리스트 역으로 돌리기
# for i in reversed(리스트): 반복문에 적용하기
# ------------------------------------------
# a = [273, 103, 52, 32 ,57]
# print(list(enumerate(a)))
# for (i, element) in enumerate(a):
#     print("{}번째 요소는 {}입니다.".format(i, element))
# for i, element in enumerate(리스트) - 딱 한가지 형태로 사용한다고 기억하자
# reversed와 같이 일회용함수이다.
# -------------------------------------------
# a = { "key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
# for key, value in a.items():
#     print("{}키의 값은 {}입니다.".format(key, value))
# -----------------------------------------
# array = []
# for i in range(0,20, 2):
#     array.append(i*i)
# array = [i*i for i in range(0, 20, 2)]  # 위 세줄의 코딩을 이렇게 한줄로 작성 가능하다. 이러한 코딩을 리스트 내포(List Comprehension)라고 한다
# print(array)
# ---------------------------------------
# array_1 = [i for i in range(10)]
# array_2 = [i for i in range(0, 10, 2)]
# array_3 = [1 for i in range(10)]

# print(array_1)
# print(array_2)
# print(array_3)
# -------------------------------------
# array_1 = [i for i in range(10) if i % 2 == 0]

# print(array_1)
# --------------------------------

# 10진수와 2진수 변환
# print("{:b}".format(10)) # {:b} =십진수로 바꿔주는 코드

# print(int("1010", 2))

# 1~100 / 2진수 / 0이 하나만 포함된 숫자 > 합
# output = 0
# for i in range(1, 100 + 1):
#     if "{:b}".format(i).count("0") == 1:
#         print("{} : {:b}".format(i, i))
#         output += i
# print("합계: {}".format(output))

output = [i for i in range(1, 100 + 1) if "{:b}".format(i).count("0") == 1]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계: {}".format(sum(output)))  # 위 코딩과 같은 결과를 출력함 리스트내포를 사용한 코드이다.
