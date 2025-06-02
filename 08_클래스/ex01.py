'''
    클래스 선언

    class 클래스명:
        # 생성자
        def __init__(sefl, 매개변수):

        # 소멸자
        def __del__(self):
            소멸자 내용

        # 메서드
        def 메서드명(self, 매개변수):
            메서드 내용
'''

class Person:

    # 생성자
    # None : 값이 없음을 의미하는 키워드
    def __init__(self, name=None, age=None, tel=None):
        # pass : 아무 동작도 하지 않는 키워드
        # pass
        self.name = name
        self.age = age
        self.tel = tel
        print("Person 객체 생성!")

    # 소멸자
    def __del__(self):
        print("Person 객체 소멸!")

    # 메서드
    def show_info(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 전화번호 {self.tel}")

# 객체 생성
# 변수명 = 클래스명()

# 인스턴스 : 클래스를 통하여 만들어진 객체
person = Person()

person.name = '김조은'
person.age = 20
person.tel = "010-1234-1234"

person.show_info()

# 생성자를 통하여 객체 생성
person2 = Person("박조은", 20, "010-1111-1111")

person2.show_info()