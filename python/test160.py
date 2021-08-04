딕셔너리 = {
    "문자열" : "값A",
    273 : [1, 2, 3, 4],
    True: False
}

for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))

딕셔너리["키"] = "값"
print()
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))

del 딕셔너리["키"]
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))