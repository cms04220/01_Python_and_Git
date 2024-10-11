#1번
class name:
    def __init__(self, i, g, j):
        self.i = i
        self.g = g
        self.j = j

    def at(self):
        print("가입하신 계정의 이름은", self.i, "이며", "나이는", self.g, "그리고 연락처는", self.j, "입니다" )


character = name("최민석", "23세", "010-0000-0000")
character.at()

#2번
me=input("메시지를 입력하세요:")

def c_message(message):
    Z=len(message)
    if Z <= 20:
        return "요금은 50원 입니다"
    elif Z > 20:
        return "요금은 100원입니다"
print(c_message(me))