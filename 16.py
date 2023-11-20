# 5. 출력

# 5-1. 파일 생성
"""
from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder) :
    os.mkdir(folder)

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")"""
            
# 5-2. 파일 열기
"""
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)
"""
# 5-3. csv 파일 열기
"""
# print(df)
# print(df.values[0])

# print(type(df))
"""
# 5-18. 비교 연산 
"""
# print(df.name == "김영수")
# print(df.company == "박박정")

# temp = df[df.postcode > 70000]
# print(temp)

# res = df[df.postcode > 70000][["name", "postcode"]]
# print(res)
# print(res.count())

# temp = df.postcode.mean()
# temp = df.postcode.sum()
# print(temp)

# temp = df[df.color=="Ivory"].postcode.mean()
# print(temp)

# temp = df[df.color=="Ivory"].postcode.sum()
# print(temp)

# temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
# temp = df[df.postcode > df.postcode.mean()]
# print(temp)
"""
# 5-19. 결측 확인
"""
# temp = df.company.isnull()
# temp = df.company.empty
# temp = df[df.company.isnull()][["name", "postcode"]]
# print(temp)

temp = df.company.isnull()
for el in temp :
    if el == True :
        print(el)
"""
# 5-20. 비트연산 - Nor
"""
# temp = df[(df.color == "Ivory")]
# temp = df[~(df.color == "Ivory")]
temp = df[~(df.color == "Ivory")][["name"]]
# print(temp.count())
# print(temp.color.count())
print(temp)
"""
# 5-21. and 연산
"""
temp = df[(df.color == "Ivory") & (df.postcode > 70000)]
print(temp)
"""
# 5-22. or 연산
"""
# temp = df[(df.color == "Beige") | (df.postcode > 70000)]
temp = df[(df.color == "Beige") | (df.postcode > 70000)][["name"]]
print(temp)
"""
# 5-23. 정렬
"""
# temp = df.sort_values("postcode")
# temp = df.sort_values("postcode", ascending=False)
# temp = df.sort_values("name", ascending=False)
temp = df.sort_values("name", ascending=True)
print(temp)"""

# 6. 데이터 재배열
"""
import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n--------------------\n")
print(df.pivot(index='Machine',columns='Country',values='Price'))
"""