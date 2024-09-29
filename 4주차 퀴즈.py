#1번
input_ = input("문자를 입력해주세요: ")

if input == "안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요.")

#2번
numbers = int(input("값을 입력하세요:"))
a = numbers + 100
if a >= 150 :
    print(a)
elif a <= 150 :
    print("값이 부족합니다")

#3번
nb = [100, 200, 300]
result = []

for price in nb:
    result.append(int(price * 1.1))

print(result)

#4번
nbs = [3, 100, 23, 33, 72, 94]
result = []

for num in nbs:
    if num % 3 == 0:
        result.append(num)

print(result)


#5번
a = 1
while a <= 1000:
    print(a)
    a=a+1

#6번
n = 1
s = 0

while n <= 100:
    if n % 2 != 0:
        s += n
    n += 1

print(s)