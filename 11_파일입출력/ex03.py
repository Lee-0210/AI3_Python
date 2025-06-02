# 파일 입력
# - 파일 경로   : ~ /hello.txt
# - 모드        : 'rt' (읽기모드)

path = 'C:/LJYAI3/GITHUB/Python/11_파일입출력/file/'
# 파일 열기
file = open(path + "hello.txt", "rt", encoding="utf-8")

while True:
    # str = file.read(10)     # 파일로부터 10글자씩 읽어온다
    str = file.readline()   # 파일로부터 한 줄 씩 읽어온다
    if not str:
        break
    print(str, end="")

# 파일 닫기
file.close()