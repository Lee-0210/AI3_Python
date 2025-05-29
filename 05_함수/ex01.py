'''
  # 함수 정의 키워드 : def
  def 함수명 (매개변수1, 매개변수2, ...):
    실행할 문장
    실행할 문장
    return (값)

  # return
  1. 함수를 종료
  2. (값)을 함수를 호출한 자리로 반환

'''

a = 10
b = 2

def plus(a, b):
  return a + b
def minus(a, b):
  return a - b
def mul(a, b):
  return a * b
def div(a, b):
  return a / b

print(f"a + b = {plus(a,b)}")
print(f"a + b = {minus(a,b)}")
print(f"a + b = {mul(a,b)}")
print(f"a + b = {div(a,b)}")


