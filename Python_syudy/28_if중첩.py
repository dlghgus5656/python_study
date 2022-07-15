# if 조건1:
#     이 문장
#     if 조건2:
#         저 문장
# 다음 문장

yellow_card = 0
foul = True

if foul:
    yellow_card += 1
    if yellow_card == 2:
        print("경고 누적 퇴장")
    else:
        print("경고..조심하자")
else:
    print("파울은 아니지만 주의")
