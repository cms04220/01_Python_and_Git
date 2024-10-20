#1
import random

results = []
while len(results) < 6:
   number = random.randint(1,45)
   if number in results:
       print("results 안에 number이 있으므로, results를 제거하고 출력했습니다.")
   else:
       results.append(number)


print("생성된 로또 번호는",(results),"입니다.")

#2
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for x in range(1, self.num + 1):
            print("------", "[", x, "단", "]", "------")
            for y in range(1, 10):
                print(f"{x} * {y} = {x * y}")

a = int(input("몇 단까지 출력할까요?: "))
gugu = Gugudan(a)
gugu.output()



#신호등 작동 및 고장 관리 시스템
class TrafficLight:
    def __init__(self, location, color="Red", working=True):
        # 신호등의 위치, 색상, 작동 여부를 초기화
        self.location = location
        self.color = color
        self.working = working

    def change_light(self, new_color):
        # 신호등 색상을 변경
        if self.working:
            self.color = new_color
            print(f"{self.location}: 신호등이 {self.color}로 변경")
        else:
            print(f"{self.location}: 고장으로 변경 불가")

    def check_status(self):
        # 신호등의 작동 상태를 확인
        status = "정상" if self.working else "고장"
        print(f"{self.location}: {status}")

    def malfunction(self):
        # 신호등을 고장 상태로 변경
        self.working = False
        print(f"{self.location}: 고장 발생")


class TrafficLightSystem:
    def __init__(self):
        # 신호등을 관리하는 리스트 초기화
        self.lights = []

    def add_light(self, location, color="Red"):
        # 새로운 신호등을 시스템에 추가
        self.lights.append(TrafficLight(location, color))

    def check_all(self):
        # 모든 신호등의 상태를 확인
        [light.check_status() for light in self.lights]

    def change_light_at(self, location, new_color):
        # 특정 위치의 신호등 색상을 변경
        for light in self.lights:
            if light.location == location:
                light.change_light(new_color)
                return
        print(f"{location}: 신호등이 없음")


#예시
system = TrafficLightSystem()  # 신호등 시스템 객체 생성
system.add_light("교차로 A")  # 교차로 A에 신호등 추가
system.add_light("교차로 B", "Green")  # 교차로 B에 초록색 신호등 추가
system.check_all()  # 모든 신호등 상태 확인
system.change_light_at("교차로 A", "주황색")  # 교차로 A 신호등을 주황색(고장난 색으로 선정)으로 변경
system.lights[0].malfunction()  # 교차로 A 신호등을 고장 상태로 변경 
system.check_all()  # 모든 신호등 상태 다시 확인
