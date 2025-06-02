# 패키지 import
from jsonutils import read_json, filter_by_field, save_json

# JSON 파일을 읽어 드려서, 특정 필드 조건에 맞는 데이터만 필터링
# 1. JSON 파일 로드
data = read_json('student.json')
# 2. 필터링
filtered = filter_by_field(data, 'gender', 'female')
# 3. JSON 파일 저장
save_json(filtered, 'filtered.json')
