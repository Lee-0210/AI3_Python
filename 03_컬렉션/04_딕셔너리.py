# 딕셔너리
# '사전' - (단어) : (뜻)
# -키(Key) : 값(Value) 를 한 쌍으로 구성한 컬렉션
# - 기호 : { key : value }
# - dic = {키1 : 값1, 키2 : 값2, 키3...}

d = {'a' : 'apple', 'b' : 'banana'}
print('d :', d)

print('d[\'a\'] :', d['a'])
print('d[\'b\'] :', d['b'])

# 딕셔너리에 요소 추가
# 방법1
d['c'] = 'melon'
print('d :', d)

# 방법2
d.setdefault('d', 'dog')
print('d :', d)

# 딕셔너리 수정
d.update(a = 'airplane')
print('d :', d)

# 딕셔너리 삭제
d.pop('a')
print('d :', d)