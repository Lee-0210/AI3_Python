# 컬렉션 반복

# [] : 리스트
stars = ["최민식", "유해진", "브래드 피트", "고윤정", "이병헌"]
for star in stars:
  print(star)
print()

# () : 튜플
menu = ("굶음", "짜장면", "버거킹", "아웃닭", "부평닭강정")
for food in menu:
  print(f"오늘 점심 메뉴는 {food} 입니다.")
print()

# {} : 세트
mac_set = {"1955 버거", '고구마 프라이', "코카콜라"}
for item in mac_set:
  print(f"item : {item}")
print()

# {"key" : "value"} : 딕셔너리
users = {
  "joeun1004" : "123456",
  "yunhongmin" : "ghdals1234*",
  "admin" : "유목민"
}

# items() : 딕셔너리의 (키, 값) 쌍의 튜플로 반환
for id, pw in users.items():
  print(f"아이디 : {id}, 비밀번호 : {pw}")
print()

for id in users:
  print(f"아이디 : {id}, 비밀번호 : {users[id]}")