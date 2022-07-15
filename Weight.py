#퀴즈
#함수 활용
def weight(height, gender):
    if gender == "M":
        result = height * height * 22 / 10000
        print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg".format(height, result))
    elif gender == "W":
        result = height * height * 21 / 10000
        print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg".format(height, result))
    return height,result

weight(175, "M")
weight(160, "W")