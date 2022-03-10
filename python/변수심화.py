a = [1, 2, 3]
b = a  # b에게 a의 주소값을 준다
a[1] = 4  # a를 변경하면 같은 주소값을 공유하고있는 b도 변경된다.
# 단 b = a 이렇게가 아닌 b = a[:] 이런식으로 슬라이싱을 통해서 주면 새로운 리스트가 생겨 넘어가는것이어서
# 같은 주소값을 가지게 되는것이 아닌 값만 복사해가는 개념이다.
# from copy import copy 를 사용해서 b = copy(a) 로 값만 복사할 수 있다.
print(a)
print(b)

print(id(a))
print(id(b))  # id를 사용해서 주소값을 보면 동일한 것을 알 수 있다.

print(a is b)  # a와 b가 같은곳을 바로보고있냐 즉 같은 주소값을 가지고 있냐를 물어보는 is
