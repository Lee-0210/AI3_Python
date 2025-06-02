from Robot import Robot

# 자식 클래스 - DroneRobot, CleanRobot
# 상속 정의 : class 클래스명(부모클래스):

# 드론
class DroneRobot(Robot):
    # 부모 클래스의 변수와 메소드를 모두 재사용한다.
    # 단, 프라이빗 멤버는 상속되지 않음

    # 최대 높이
    max_height = 50

    # super() : 자식 클래스의 생성자에서 부모클래스의 생성자를 호출하는 메소드
    def __init__(self, name, power, battery, height):
        # self.name = name
        # self.power = power
        # self.battery = battery
        super().__init__(name, power, battery)
        self.height = height


    # 오버라이딩
    # : 부모 클래스의 메소드를 자식 클래스에서 재정의하는 것
    def move(self, direction, height):
        if height > DroneRobot.max_height:
            print('{}m 이상으로는 비행할 수 없습니다'.format(DroneRobot.max_height))
            return

        self.height = height
        print('고도 : {}'.format(height))
        print('{} (으/)로 방향으로 비행합니다.'.format(direction))