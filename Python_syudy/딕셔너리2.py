# 딕셔너리
# 딕셔너리 = {key1: value1, key2: value2,...}

person = {'이름': '홍길동', '나이': 20, '키': 180, '몸무게': 70}
print(person)  # {'이름': '홍길동', '나이': 20, '키': 180, '몸무게': 70}

# key에 해당하는 value 확인?
print(person['이름'])  # 홍길동
# 존재하지 않는 키에 접근하면 에러 발생
# print(person['별명']) # error

# get() 메소드를 사용하면 에러 없이 None이 출력됨
print(person.get('별명'))  # None

# 새로운 데이터를 추가하려면?
person['최종학력'] = '대학교'
print(person['최종학력'])  # 대학교

# 특정 key의 value를 바꾸려면?
person['키'] = '170'
print(person['키'])  # 170

# 여러 ket들의 value를 동시에 바꾸려면?
person.update({'키': 160, '몸무게': 60})
print(person['키'], person['몸무게'])  # 160 60

# 어떤 key들이 있는지 확인하려면?
print(person.keys())  # dict_keys(['이름', '나이', '키', '몸무게', '최종학력'])

# 어떤 value들이 있는지 확인하려면?
print(person.values())  # dict_values(['홍길동', 20, 160, 60, '대학교'])

# 어떤 key와 value들이 있는지 확인하려면?
print(person.items())
# # dict_items([('이름', '홍길동'), ('나이', 20), ('키', 160), ('몸무게', 60), ('최종학력', '대학교')])

# 특정 key와 value를 함께 삭제하려면?
person.pop('몸무게')
print(person)  # {'이름': '홍길동', '나이': 20, '키': 160, '최종학력': '대학교'}

# 모든 데이터를 삭제하려면?
person.clear()
print(person)  # {}


# 그 외
# fromkeys() - 제공된 keys를 통해 새로운 딕셔너리 생성 및 반환

# popitem() - 마지막으로 추가된 데이터 삭제

# setdefault() - key에 해당하는 value 반환
#                key가 없다면 새로 만들고 default value 설정 및 반환
