from cmath import rect


class myclass:
    pass

class Rectangure:
    # 클래스 변수 선언, 메서드 밖에 존재하는 값, 공용 변수
    count = 0

    # 초기자 (initializer),클래스로부터 새 객체를 생성할 때 마다 실행되는 메서드.
    def __init__(self, width, height):
        # self.* : 인스턴스 변수, 하나의 클래스로부터 여러 객체 인스턴스를 생성할 수 있음. 클래스 변수는 클래스 내에만 존재, 인스턴스는 각 객체의 인스턴스 마다 존재. 
        self.width = width
        self.height = height
        Rectangure.count += 1

    def calcArea (self):
        area = self.width * self.height
        return area
    
    # 정적 메소드
    @staticmethod
    def isSquare (rectWidth, rectHeight):
        return rectWidth == rectHeight

    # 클래스 메소드
    @classmethod
    def printCount (test):
        print(test.count)


# 테스트

rect1 = Rectangure(5,5)
rect2 = Rectangure(3,4)
rect1.printCount()
rect2.printCount()