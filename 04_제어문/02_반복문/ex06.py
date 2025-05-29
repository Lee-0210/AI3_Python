# 가위바위보 게임
# : 컴퓨터랑 가위바위보 게임을 하여, 질 때까지 반복하는 게임을 완성하시오.

import random
choices = ["가위", "바위", "보"]

# 리스트 요소중 하나를 랜덤으로 선택
next = True
winCount = 0

while next == True:
  you = input("가위, 바위, 보 : ")
  computer = random.choice(choices)
  print(f"당신의 수 : {you} vs 컴퓨터의 수 : {computer}")

  if (you == "가위" and computer == "바위") or (you == "바위" and computer == "보") or (you == "보" and computer == "가위"):
    print("You lose..")
    next = False
  elif (you == "가위" and computer == "보") or (you == "바위" and computer == "가위") or (you == "보" and computer == "바위"):
    winCount += 1
    print("You win!!")
  else:
    next = False
    print("draw!")

print(f"게임이 종료되었습니다. 당신의 연승 수는 {winCount}승 입니다.")