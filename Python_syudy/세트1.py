'''세트
- 값들의 순서가 보장되지 않음
- 중복이 불가함
'''
#  세트 = {값1, 값2, ...}
A = {'돈가스', '보쌈', '제육덮밥'}
B = {'짬뽕', '초밥', '제육덮밥'}

# 교집합
print(A.intersection(B))

# 합집함
print(A.union(B))

# 차집합
print(A.difference(B))
