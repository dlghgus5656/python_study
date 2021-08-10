# def function():
#     print("A")
#     print("B")
#     return 1

# print(function())


# def return_test():
#     print("A 위치입니다.")
#     return
#     print("B 위치입니다.")  #위에서 리턴이 일어났기때문에 아래 코드는 실행되지 않음

# return_test()



# start~end 까지 있는 모든 정수를 더하는 함수
# def sum_all(start, end):
#     변수 = 0
#     for i in range(start, end + 1):
#         변수 += i
#     return 변수
# print(sum_all(1, 100))
# print(sum_all(50, 100))



# def f_1(x):
#     return (2 * x) + 1
# print(f_1(10))

# def f_2(x):
#     return (x ** 2) + (2 * x) + 1  # ** 2 는 제곱이다
# print(f_2(10))



def mul(*values):
    변수 = 1
    for i in values:
        변수 *= i
    return 변수
print(mul(5, 7, 9, 10))