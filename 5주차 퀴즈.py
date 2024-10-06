#1번
def add(a, b, c, d):
    return a + b + c + d

def multiply(a, b, c, d):
    return a * b * c * d

n1 = int(input("1: "))
n2 = int(input("2: "))
n3 = int(input("3: "))
n4 = int(input("4: "))

print("4개 합:", add(n1, n2, n3, n4))
print("4개 곱:", multiply(n1, n2, n3, n4))


#2번
def nb1(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

num = int(input("숫자: "))

print(f"{num} {nb1(num)}")

#3번
def ca(numbers):
    total = 0
    for numb in numbers:
        total += numb
    return total / len(numbers)

numbers = list(map(int, input("숫자 입력하세요(쉼표 사용): ").split(',')))
print("평균값:", ca(numbers))

#4번
class Game:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!", "(", self.id, ",", self.gender, ",", self.job, ")", )


character = Game("p1", "남성", "농부")
character.attack()

#5번
class RealEstate:
    def __init__(self, 위치, 크기, 종류, 가격, 년도):
        self.location = 위치
        self.size = 크기
        self.building_type = 종류
        self.price = 가격
        self.year_built = 년도

    def show_info(self):
        print(f"위치: {self.location}")
        print(f"평수: {self.size}평")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price}원")
        print(f"지어진 년도: {self.year_built}년")

estate1 = RealEstate("서울", 30, "아파트", 800000000, 2010)
estate1.show_info()