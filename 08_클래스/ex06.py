import math

class Circle:

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            print("반지름은 양수여야 합니다.")
            self.__radius = 0
            return
        self.__radius = value

    @radius.getter
    def radius(self):
        return self.__radius

circle = Circle()
circle.radius = 10

print(f"circle - radius : {circle.radius}")