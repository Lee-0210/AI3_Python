# getter, setter
# - getter : 변수의 값을 가져오는 메서드
# - setter : 변수의 값을 지정하는 메서드

class Person:

    def __init__(self, name):
        self.name = name

    # getter
    def get_name(self):
        return self.name

    # setter
    def set_name(self, value):
        self.name = value

person = Person('김조은')

print(f"person - name : {person.get_name()}")