import time
import math

start_time = time.time()
count = 0

print("시작 시각은 " + time.ctime(start_time) + " 입니다.")

def find_d(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print("소수는 ", end="")

for i in range(2, 50001):
    if find_d(i):
        count += 1
        print(i, ",", end="")

end_time = time.time()
print("\n종료 시각은 " + time.ctime(end_time) + " 입니다.")
print(f"총 {int(end_time) - int(start_time)}초 실행하였습니다.")
print("총 소수의 갯수 : {}".format(count))