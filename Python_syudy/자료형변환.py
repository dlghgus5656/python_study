# 튜플에 값 추가하는 법

# 먼저 리스트에 저장해준다
my_tuple = ('오예스', '몽셀')
my_list = list(my_tuple)
print(my_tuple)

# 리스트에서 제공하는 append() 메소드를 이용해 값을 추가한다
my_list.append('초코파이')

# 다시 튜플로 감싸준다
my_tuple = tuple(my_list)
print(my_tuple)

# -------------------------------------------
print("")

# 리스트에 중복값을 제거하는 법

# 세트로 바꾸어준다. 세트는 중복값 허용이 안되기 때문에 이 과정에서 중복값이 사라짐
my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
print(my_list)
my_set = set(my_list)  # 초코파이는 하나만 남고 나머지는 사라짐

# 다시 리스트로 바꾸어 주면 중복값 제거 된 리스트 완성
my_list = list(my_set)
print(my_list)
# 다만 set는 순서도 보장하지 않기 때문에 결과값의 순서가 랜덤이다.

# ---------------------------------------------
print("")

# 순서가 중요할땐 딕셔너리를 이용하자
my_list2 = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
print(my_list2)
my_dic = dict.fromkeys(my_list2)  # 딕셔너리는 키의 중복을 허용하지 않아 초코파이는 하나만 남는다.

# 다시 리스트로 바꾸어 주면 순서가 보장되고 중복값 제거 된 리스트 완성
my_list2 = list(my_dic)
print(my_list2)
