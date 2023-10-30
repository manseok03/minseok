# 속성 출력
"""
class Person :
	name = "python"
	age = 23
	number = "01012345678"
 
p = Person()
print(p.name)
print(p.age)
print(p.number)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number)"""

# 메서드, 셀프

"""
class Person :
	name = "python"
	age = 23
	number = "01012345678"

	def getIntroduce(self):
		return f"My name is {self.name}"

p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce())"""

# 클래스 초기화

"""
class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
  
p = Person("hello", 24, "01012345678")
p1 = Person("he", 21, "0108")
p2 = Person("hee", 24, "028764321")

print(p.name)
print(p1.name)
print(p2.name)"""

# 클래스 변수

class Person :
	count = 0
	
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
		Person.count +=1
  
p = Person("hello", 24, "01012345678")
print(p.name)
print(p.count)
p1 = Person("he", 21, "0108")
print(p1.name)
print(p1.count)
p2 = Person("hee", 24, "028764321")
print(p2.name)
print(p2.count)

print(p.count)
print(p1.count)
print(p2.count)