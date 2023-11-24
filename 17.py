# 1-1. 파일 생성
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
            temp.color_name() + "\n")
"""

# 1-2. 파일 열기
"""
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)
"""
# 1-3. 순위 매기기
"""
df["aver"] = df.postcode.rank(method="average")
print(df[["postcode", "aver"]])
"""
"""
df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode", "dense"]])
"""
"""
df["first"] = df.postcode.rank(method="first")
print(df[["postcode", "first"]])
"""
"""
df["min"] = df.postcode.rank(method="min")
print(df[["postcode", "min"]])
"""
"""
df["max"] = df.postcode.rank(method="max", ascending=False)
df["max"] = df.postcode.rank(method="max")
print(df[["postcode", "max"]])
"""
"""
print(df[["postcode", "aver", "dense", "first", "min", "max"]])
"""

# 1-4. 컬럼-로우 변경
"""
print(df.transpose())
"""

# 1-5. 누적계산
"""
# print(df["postcode"].expanding().sum())
# print(df["postcode"].expanding())
"""

# 1-6. 정렬 찾기
"""
# 가장 작은수
print(df.postcode.idxmax(axis=0)) """
"""
# 가장 큰수
print(df.postcode.idxmin(axis=0))"""

# 1-7. empty 추가
"""
print(df.empty)
"""

# 1-8. 검색
"""
# print(df.isin([48742]))
# print(df.isin(["김예원"]))
# print(df.isin([48742, 12834]))
print(df.isin([48742, 12834, "김예원"]))
"""

# 1-9. 기간 계산
"""
period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf)
"""

# 1-10. 시간값을 인덱스
"""
i = pd.date_range("2023-11-10", periods=10, freq="1H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print("\n--------------------\n")
"""

# 1-11. 특정시간 인덱스 찾기
"""
print(df.at_time("09:00"))
print(df.at_time("03:00"))
"""

# 1-12. 시간 범위 출력
"""
print(df.between_time(start_time="12:00", end_time="00:00"))
"""

# 1-13. 시간간격 데이터 생성
"""
i = pd.date_range("2023-11-10", periods=10, freq="3D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

# print(df.first("5D"))
# print(df.first("7D"))
# print(df.last("7D"))
"""

# --------------------------------------------------------------

# 2. 코스피지수
"""
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n--------------------\n")
"""
# 2-1. 최고가 확인
"""
res = ksp["High"].max()
print(res)
"""
"""
res = ksp["High"].idxmax()
print(res)
"""

# 2-2. 최저가 확인
"""
res = ksp["Low"].min()
print(res)
"""
"""
res = ksp["Low"].idxmin()
print(res)
"""

# 2-3. 최고가 값 찾기
"""
res = ksp["Volume"].nlargest(n=5)
# res = ksp["Volume"].nlargest(n=16)
print(res)
"""

# 2-4. 최하위 값 찾기
"""
res =ksp["Volume"].nsmallest(n=5)
#res =ksp["Close"].nsmallest(n=5)
print(res)
"""

# 2-5. kospi 3000 달성 최초일 찾기
"""
cond = ksp["Close"] >= 3000
# cond = ksp["Close"] >= 2000
res = ksp[cond].index[0]
print(res)
"""

# 2-6. 위(shift) 값 참조, 처리
"""
res = ksp["Volume"] > ksp["Volume"].shift()
print(res)
"""
"""
ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
res = ksp["up"] != ksp["up"].shift().cumsum()
print(res)
"""

# 2-7. 연속 증가값 확인
"""
ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
ksp["grp"] = (ksp["up"] != ksp["up"].shift()).shift()

ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)
"""

# 2-8. 연속 상승값 확인
"""
ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
ksp["grp"] = (ksp["up"] != ksp["up"].shift()).shift()
ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1

print(ksp["up_cnt"].max())
"""

# --------------------------------------------------------------

# 3. 부동산 정보 처리

# 3-1. 변환
"""
import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")
df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head())
"""

# 3-4. head 출력
"""
import pandas as pd

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head())
"""

# 3-3. 컬럼명 바꾸기

import pandas as pd

df = pd.read_csv("./data/conv_apt.csv", index_col=0)

print(df.head())
print("\n--------------------\n")
df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)

# 3-4. 컬럼 타입변경

#print(df.dtypes)
# df["분양가"] = df["분양가"].convert_dtypes()
#df(df.dtypes)

# 3-5. array로 변환하기

arr = df.to_numpy()
# print(arr)
# print(arr[2])
# print(len(arr))

# 3-6. 요약정보

# print(df.describe())

# 3-7. 축변환하기

print(df.transpose())
print("\n--------------------\n")
print(df.T.head())