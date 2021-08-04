dictionary = {
    "name": "7 망고",
    "type": "당절임"
}

# 사용자로부터 입력받음
key = input("> 접근하고자 하는 키:")

#출력합니다.
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")