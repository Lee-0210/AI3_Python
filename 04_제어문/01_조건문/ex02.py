# 다중 조건문
# - 위에 나온 조건이 만족하지 않을 때, (if)
#   아래 조건을 확인하고, (elif)
#   모두 만족하지 않으면 else 문을 실행한다.

score = int(input("성적 : "))

if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")