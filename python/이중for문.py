a = 10
for i in range(2, 10):
    for j in range(1, 10):
        # end=""를 써주면 가로로 이어서 출력 해준다 "" 사이에 공백을 한칸 넣어주면 한칸 띄어쓰기가 된 채로 출력된다.
        print(i * j, end=" ")
    print('')
