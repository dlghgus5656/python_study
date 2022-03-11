from tkinter.tix import Tree


TreeHit = 0
while TreeHit < 10:
    TreeHit = TreeHit + 1
    print("나무를 %d번 찍었습니다." % TreeHit)
    if TreeHit == 10:
        print("나무가 넘어갑니다.")
