# 파일 추가
# - 파일 경로   : ~ /hello.txt
# - 모드        : 'at' (추가모드)

path = 'C:/LJYAI3/GITHUB/Python/11_파일입출력/file/'
# 파일 열기
file = open(path + "hello.txt", "at", encoding="utf-8")

# 추가할 내용
file.write("\n")
file.write("이어서 내용을 추가합니다.")
file.write("\n")
file.write("텍스트 파일 내용 추가 모드 : at")
print("파일에 새로운 내용을 추가하였습니다.")

# 파일 닫기
file.close()