from audioop import add
from unicodedata import name


dic = {'name': 'Eric', 'age': 15}
dic['add'] = "추가"

print(dic)

del dic['add']  # add키값 삭제

print(dic)


for k, v in dic.items():
    print("키는: " + str(k))
    print("벨류는:" + str(v))

print(dic.get("name", "없음"))
print(dic.get("11", "없음"))
