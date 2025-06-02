# 부모 클래스 - Robot
class Robot:

    # 생성자
    def __init__(self, name, power, battery):
        self.name = name
        self.power = power
        self.battery = battery

    # 메소드 - 전원, 이동, 충전
    def power(self, power):
        self.power = power
        print('power : ', power)

    def move(self, direction):
        print('{} (으/)로 이동합니다.'.format(direction))

    def charge(self):
        self.battery = 100
        print('충전이 완료되었습니다.')