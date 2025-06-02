from Robot import Robot

# 로봇 청소기
class CleanRobot(Robot):
    max_bin = 50

    # 생성자
    def __init__(self, name, power, battery, bin):
        super().__init__(name, power, battery)
        self.bin = bin

    # 메소드 오버라이딩
    def move(self, direction):
        print('{} 으(/로) 이동하여 청소합니다.'.format(direction))
        self.bin += 1            # 먼지 흡입

    def mapping(self):
        print('청소할 영역을 기억합니다.')


    # 먼지통 비우기
    def vacate(self):
        self.bin = 0
        print('먼지통을 비웁니다.')