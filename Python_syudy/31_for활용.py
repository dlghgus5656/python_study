# 리스트, 튜플, 딕셔너리 등 범위로 지정할 수 있다.

# 예시 코드

from re import L


my_list = [1, 2, 3]
for x in my_list:
    print(x)
# >
# 1
# 2
# 3

my_tuple = (1, 2, 3)
for a in my_tuple:
    print(a)
# > 위와 동일

# 딕셔너리 경우엔 좀 다르다
person = {'이름': '홍길동', '나이': "20", '키': 180, '몸무게': 70}
for v in person.values():
    print(v)
# > 홍길동 20 180 70 같이 값에 해당되는 값 출력

person = {'이름': '홍길동', '나이': "20", '키': 180, '몸무게': 70}
for k in person.keys():
    print(k)
# > 이름 나이 키 몸무게 같이 키에 해당되는 값 출력

person = {'이름': '홍길동', '나이': "20", '키': 180, '몸무게': 70}
for k, v in person.items():
    print(k, v)
# >
# 이름 홍길동
# 나이 20
# 키 180
# 몸무게 70 키랑 값 둘다 출력

fruit = 'apple'
for p in fruit:
    print(p)
# >
# a
# p
# p
# l
# e 단어 하나씩 출력됨
