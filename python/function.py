# 함수를 선언한다
# def 함수이름():
#     print("안녕하세요") #두번째
#     print("안녕하세요") #세번쨰
#     print("안녕하세요") #네번쨰
# # 함수를 호출한쨰
# 함수이름() # 첫번째 순서로됨 호출이

# def 함수이름(매개변수1, 매개변수2, 매개변수3, 매개변수4):
#     print("안녕하세요" + str(매개변수1))
#     print("안녕하세요" + str(매개변수2))
#     return 매개변수1 + 매개변수2 + 매개변수3 + 매개변수4 #밑에 프린트문은 실행안됨
#     print("안녕하세요" + str(매개변수3))
#     print("안녕하세요" + str(매개변수4))
    
# print(함수이름(1, 2, 3, 4)) #매개변수에 각각 숫자가 대입됨됨

# ---------------------
# def print_n_times(value, n):
#      for i in range(n):
#         print(value)

# print_n_times("안녕하세요", 5) # 출력가능
# print_n_times("안녕하세요", 5, 100) # 여기서 매개변수로 준 2개보다 많거나 적은 매개변수를 프린트문으로 출력할순 없다

# def 함수이름(매개변수1, 매개변수2, *가변매개변수):
#     print(매개변수1)
#     print(매개변수2)
#     print(가변매개변수)

# 함수이름(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# def print_n_times(value, n=5):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요")


# def function(일반매개변수A, 일반매개변수B, *가변매개변수, 기본매개변수A=10, 기본매개변수B=20):
#     print(일반매개변수A, 일반매개변수B)
#     print(가변매개변수)
#     print(기본매개변수A, 기본매개변수B)

# function(0,1,2,3,4,5,6,7,8,9,10, 기본매개변수A=11, 기본매개변수B=12)



# def print_n_times(*values, n=2):
#     #n번 반복합니다ㅣ.
#     for i in range(n):
#         #values 는 리스트처럼 활요한다.
#         for value in values:
#             print(value)
#         #단순한 줄바꿈
#         print()

# #함수를 호출한다.
# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)


def test(a, b=10, c=100):
    print(a + b+ c)

#1 기본형태
test(10, 20, 30)
#2 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)
#3 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)
#4 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)
