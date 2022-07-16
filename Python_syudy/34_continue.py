drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print("시즌3은 재미 없데, 건너뛰자")
        continue
    print(f"{x} 시청")  # continue로 인해서 시즌3 일때는 실행되지 않고 넘어감
