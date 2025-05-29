# 퀴즈 프로그램
quiz = {
  1 : {
    "question" : "순서가 없고 중복 불가능한 컬렉션은?",
    "choice"   : ["1. 리스트", "2. 튜플", "3. 세트", "4. 딕셔너리"]
  },
  2 : {
    "question" : "다음 중 파이썬의 반복문은?",
    "choice"   : ["1. loop", "2. repeat", "3. cycle", "4. while"]
  },
  3 : {
    "question" : "반복문을 종료하는 키워드는?",
    "choice"   : ["1. brake", "2. break", "3. break dance", "4. break time"]
  },
}

answer = {
  1 : 3,
  2 : 4,
  3 : 2
}
score = 0

for no, content in quiz.items():
  # 1. 문제 출력
  print(f"{no}. {content['question']}")
  # 2. 보기 출력
  print(f"{content['choice']}")
  # 3. 입력
  user = input("답 : ")
  # 정답 확인
  if int(user) == answer[no]:
    print("정답입니다!")
    score += 10
  else:
    print(f"틀렸습니다. 정답은 {answer[no]}번 입니다.")
print(f"최종 점수는 {score}점 입니다")