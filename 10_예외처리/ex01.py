'''
    예외 처리
    - 예외 발생 가능성이 있는 문장에 대응을 하는 것

    예외(exception)?
    : 프로그램 실행 중 예상치 못하게 발생한 오류
    - 예외 발생 시, 프로그램 진행 중단
    - 예외 발생 가능성이 있는 문장을 파악하여 대응 가능
'''

# 숫자를 0으로 나누는 경우
print("X / Y")
X = int(input("X : "))
Y = int(input("Y : "))

try:
    result = X / Y
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다.")
    print(err.args[1])
else:
    print(result)