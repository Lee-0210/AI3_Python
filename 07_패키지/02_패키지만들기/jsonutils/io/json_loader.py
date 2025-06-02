import json
"""
    JSON 파일 읽기
"""

def read_json(filepath):
    # 파일열기
    with open(filepath, "r", encoding="utf-8") as f:
        # JSON 파일 읽기
        return json.load(f)
