# 1. Dataframe

# 1-1. Dataframe 출력
"""
import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])

print(df)
print("\n--------------------\n")

print(df[1])
print("\n--------------------\n")

print(df[1][1])
print("\n--------------------\n")
print(df[2][2])"""

# 1-2. dictionary
"""
import pandas as pd

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

# print(fr)
# print("\n--------------------\n")

# print(fr["x"])
# print(fr["z"])
# print("\n--------------------\n")

# print(fr.x)
# print(fr.y)
# print("\n--------------------\n")

# print(fr.iloc[1])
# print(fr.iloc[2])
# print("\n--------------------\n")

# print(fr.loc["y축"])

# 1-3. 컬럼(열)추가

frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
print(frs)
print("\n--------------------\n")

frs["t"] = [60, 120, 180]
print(frs)
print("\n--------------------\n")

# 1-4. 행 추가

frs.loc["t축"] = [100, 200, 300, 400]
print(frs)
print("\n--------------------\n")

# 1-5. 행 수정

frs.loc["t축"] = [500, 600, 700, 800]
print(frs)
print("\n--------------------\n")

# 1-6. 행 / 열 삭제

#행 삭제
frs.drop("x", axis=1, inplace=True)
# frs.drop("x", axis=1, inplace=False)
print(frs)
print("\n--------------------\n")

# 열 삭제
frs.drop("x축", inplace=True)
print(frs)
print("\n--------------------\n")"""

# 2. 컬럼추가

"""
import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
# col = ["x","y","z"]
# idx = ["x축","y축","z축"]

col = ["col1", "col2", "col3"]
idx = ["삼성", "현대", "LG"]

df = pd.DataFrame(data=dt,index=idx,columns=col)

# 2-1. 출력

print(df)
print("\n--------------------\n")

# 2-2. 컬럼 / 행 출력

# print(df["x"])
# print(df["y"])
# print("\n--------------------\n")

# 2-3. 인덱스 / 로우 출력

# print(df.loc["x축"])
# print(df.loc["y축"])
# print("\n--------------------\n")

# 2-4. 연산

# print(df + 1)
# print(df + 1)
# print(df / 100)
# print(df.mul(100))

# 2-5. 두 데이터프레임간 연산

# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
# df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])
df2 = pd.DataFrame(data=dt2,index=["삼성","현대","LG"],columns=["col2"])

print(df2)
print("\n--------------------\n")

# print(df.div(df2))
print(df.mul(df2))
print("\n--------------------\n")

print(df.div(df2, fill_value=100))"""

# 3. 멀티인덱스

"""
import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)
print("\n--------------------\n")

# 3-1. 출력

# print(df.loc["row3"])
print(df.iloc[0])
print("\n--------------------\n")

print(df.loc[("row2", "val3")])
print("\n--------------------\n")

# 3-2. 엘레멘트 출력

df.loc[("row3", "val3"), "col1"]"""

# 4. 랜덤 데이터 생성

"""
import numpy as np
import pandas as pd

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

print(df)
print("\n--------------------\n")

# 4-1. 출력

print(df[2])
print("\n--------------------\n")

print(df.loc[2])
print("\n--------------------\n")

print(df.loc[3][1])
print("\n--------------------\n")

# 4-2. 범위 출력

print(df.head(3))
print("\n--------------------\n")

print(df.tail(3))"""

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

import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

# 5-3. csv 파일 열기

# print(df)
# print(df.values[0])

# print(type(df))

# 5-4. csv 파일 열기
"""
print(df.head())
print("\n--------------------\n")

print(df.head(3))
"""
# 5-5. 끝에서 부터 부분 읽기
"""
print(df.tail())
print("\n--------------------\n")

print(df.tail(3))
"""
# 5-6. sampling 
"""
print(df.sample())
print("\n--------------------\n")

print(df.sample(4))
"""
# 5-7. 인덱스 설정 확인
"""
print(df.index)
"""
# 5-8. 컬럼별 타입확인
"""
print(df.dtypes)
"""
# 5-9. 출력
"""
print(df.values)
print("\n--------------------\n")

print(df.values[3])
"""
# 5-10. 엘레멘트 출력
"""
for el in df.values[0] :
    print(el)
"""
# 5-11. - 데이터프레임 정보확인
"""
print(df.info())
"""
# 5-12. null 값 확인
"""
print(df.isnull())
print("\n--------------------\n")

print(df.isnull().sum())
"""
# 5-13. 컬럼 / 행 데이터 확인
"""
# print(df.name)
# print(df.postcode)
# print(df.color)

# df["name"]
# df["postcode"]
# df["color"]


df["name", "id"]
"""
# 5-14. 여러 컬럼 확인
"""
# df[["name", "id"]]
df[["name", "address", "postcode"]]
"""
# 5-15. 컬럼 데이터 상세
"""
# print(df.postcode.describe())
print(df.color.describe())
"""
# 5-16. 컬럼 데이터 갯수
"""
# print(df.color.count())
print(df.color.value_counts())
"""
# 5-17. 데이터간 연산
"""
temp = df.postcode.sum() / df.name.count()
print(temp)
"""
# 5-18. 비교 연산 
"""
print(df.name == "이민석")
"""
# 5-19. 결측 확인
"""
temp = df[df.color == "Beige"].head(1)
print(temp)
"""