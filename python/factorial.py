# n! = 1 * 2 * 3 * ... (n-2) * (n-1) * n
# def factorial_1(n):
#     변수 = 1
#     for i in range(1, n + 1):
#         변수 *= i
#     return 변수
    
# 0! = 1
# n! = n * (n-1)!
# def factorial_2(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_2(n-1)
# print(factorial_1(3))
# print(factorial_2(3))



#f(1) = 1, f(2) = 1
#f(n) = f(n-1) + f(n-2)

# counter = 0
# def f(n):
#     global counter #global 함수 사용
#     counter += 1
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)

# print(f(20))
# print("계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))

# 위 코딩은 값이 커질경우 오래 걸리는 단점이있다 밑에 코딩은 이러한 단점을 해결해준다.

#메모화
# 메모 = {1: 1, 2: 1}
# def f(n):
#     if n in 메모:
#         return 메모[n]
#     else:
#         output = f(n-1) + f(n-2)
#         메모[n] = output
#         return output
# print(f(150)

#조기 리턴
메모 = {1: 1, 2: 1}
def f(n):
    if n in 메모:
        return 메모[n]
    output = f(n-1) + f(n-2)
    메모[n] = output
    return output
print(f(100))