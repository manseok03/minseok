# 1) 삼각형 출력

# 1-1) 직각 삼각형

"""for i in range(1, 6):
    print("*" * i)"""

# 1-2) 역직각 삼각형

"""for i in range(5, 0, -1):
    print("*" * i)"""
    
# 1-3) 이등변 삼각형

"""for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
    
# 1-4) n = 5 / 삼각형의 높이를 설정
    
for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)"""
    
# 2) 5x5 출력

# 2-1) 정상 출력

"""num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = []"""
    
# 2-2) 세로 출력

"""line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = []"""
    
# 2-3) 역순 출력

"""num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = []"""
    
# 3) 가위바위보 게임

# 3-1) 예시

"""import random

pro = random.choice(["1","2","0"])
user = input("숫자를 입력해 주세요 :")
print ("상대 :", pro)

if user == "2" or user == "1" or user == "0":
    if user == pro :
        print("비겼다")
    elif (user == "2" and pro == "1") or (user == "1" and pro == "0") or (user == "0" and pro == "2"):
        print("이겼다!")
    else :
        print ("졌다...")
else :
    print("가위는 1, 바위는 2, 보는 0")"""

# 3-2) 교수님

"""import random
def get_computer_choice():
    choices = ['1', '2', '0']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum :
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '0') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '0' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")
        return

print("1 : 가위")
print("2 : 바위")
print("0 : 보")
print("0~2 숫자를 입력하세요!")
chnum = input()
pcnum = get_computer_choice()

determine_winner(chnum)"""

# --------------------------------------------

# 파일 생성

"""file = open("temp.txt", "w")
file.close()"""

# 파일 쓰기

"""file = open("temp.txt", "w")

# file.write("hello")
file.write("hello\n")
file.write("world")

file.close()"""

# C:/Users/minse/temp.txt

"""f = open("C:\\Users\\minse\\temp.txt", "w")
for i in range(100) :
    f.write(f"{i}\n")
    
f.close()"""

# 추가 쓰기

"""f = open("C:\\Users\\minse\\temp.txt", "w")

f.write("hello\n")
f.write("world")

f.close()"""

# 파일 읽기

"""f = open("temp.txt", "r")
res = f.read()
print(res)

f.close()"""

# 다른 경로로 파일 읽기

"""f = open("C:\\Users\\minse\\temp.txt", "r")
res = f.read()
print(res)

f.close()"""

# readline

"""# f = open("temp.txt", "r")
f = open("temp.txt", "r")

for i in range(110) :
    res = f.readline()
    print(res)

f.close()"""

# readlines 읽기

"""f = open("temp.txt", "r")
res = f.readlines()
print(res)

f.close()"""

# readlines 읽기

"""f = open("temp.txt", "r")
line = f.readlines()
for l in line :
    print(l)
    
f.close()"""

# file object

f = open("temp.txt", "r")
for line in f :
    print(line)
    
f.close()