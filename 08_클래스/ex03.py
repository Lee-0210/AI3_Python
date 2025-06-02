# 인스턴스 변수, 메서드
# 클래스 변수, 메서드

class Student:
    # 인스턴스 변수
    # name = ''
    # age = ''
    # tel = ''

    # 클래스 변수 : 객체간의 공유할 값으로 사용하는 변수
    count = 0
    student_list = []

    # 인스턴스 변수 접근 : self.변수
    # 클래스 변수 접근   : 클래스.변수
    def __init__(self, no, name, major):
        self.no = no
        self.name = name
        self.major = major
        Student.count += 1
        Student.student_list.append(self)

    def __str__(self):
        return f"{self.no} / {self.name} / {self.major}"

    # @이름     : 데코레이터
    #           - 해당 클래스나 메서드의 기능/용도를 명시하는 역할

    # 클래스 메서드
    # @classmethod : 해당 메서드를 클래스 메서드로 명시
    # 클래스 메서드의 첫 번째 매개변수로 클래스(cls) 를 받아온다.
    # 인스턴스 메서드는 첫 번째 매개변수로 인스턴스(self) 를 받아온다.

    @classmethod
    def show_info(cls):
        for student in cls.student_list:
            print(str(student))

# ----------------------------------------------------------

s1 = Student('김조은', 20, '010-1234-1234')
s2 = Student('박조은', 30, '010-2234-1234')
s3 = Student('황조은', 40, '010-3234-1234')

# 클래스 변수
print(f"{Student.count}명의 학생이 참여했습니다.")

print(s1.count)
print(s2.count)
print(s3.count)

# 클래스 메서드
Student.show_info()
