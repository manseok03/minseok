# 1. 막대그래프 그리기-------------------------------
"""
import matplotlib.pyplot as plt
"""

# 1-1. 이종 그래프 출력
"""
x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

# ax1.plot(x, y1, "-o", color="C1")
ax1.plot(x, y1, "-o", color="C1", label="XData")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")

ax2 = ax1.twinx()
# ax2.bar(x, y2, color="C2")
ax2.bar(x, y2, color="C2", label="YData")
ax2.set_ylabel("Y2data")

ax1.legend(loc="ipper right")
ax2.legend(loc="upper left")
"""

# 1-2. 다중 그래프 출력
"""
x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]
"""

# (1) 각 패널 별 스타일 지정
"""
plt.style.use("bmh")

plt.subplot(2, 1, 1)  
plt.subplot(1, 2, 1)  
plt.subplot(3, 1, 1)  
plt.plot(x1, y1, "o-")

plt.title("x1 Graph")
plt.xlabel("x-data")
plt.xlabel("y-data")
"""

# (2) 결과 이미지 저장
"""
plt.savefig("data/img.jpg")
plt.savefig("data/img.png")
"""

# (3) 2행 2열(row) 그래프 출력
"""
plt.subplot(2, 2, 1)
plt.subplot(2, 2, 2)
plt.subplot(2, 2, 3)
plt.subplot(2, 2, 4)
"""

# (4) 다중 객체를 이용한 막대 그래프 출력
"""
x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.bar(x_years, y_data)
ax2.bar(x_years, y_data)
ax3.bar(x_years, y_data)
ax4.bar(x_years, y_data)

ax1.bar(x_years, y_data, color="aquamarine", edgecloer="black", hatch="/")
ax2.bar(x_years, y_data, color="salmon", edgecloer="black", hatch="\\")
ax3.bar(x_years, y_data, color="navajowhite", edgecloer="black", hatch="+")
ax4.bar(x_years, y_data, color="lightskyblue", edgecloer="black", hatch="*")

plt.tight_layout()
plt.show()
"""

# 2. 데이터 처리 활용---------------------------------

# 2-1. Seaborn 사용
"""
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")
print(tips)
"""

# (1) 산점도와 선형 회귀 선 표시
"""
sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()
"""

# (2) 각 지표별 상관관계 출력
"""
tips = sns.load_dataset("tips")
print(tips)

sns.regplot(x="total_bill", y="tip", data=tips)
sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")
sns.barplot(x="tip", y="total_bill", data=tips)
sns.barplot(x="sex", y="total_bill", data=tips)
sns.barplot(x="sex", y="tip", data=tips)
sns.barplot(x="smoker", y="total_bill", data=tips)
sns.barplot(x="smoker", y="total_bill", data=tips)
sns.barplot(x="time", y="total_bill", data=tips)

plt.title("Average Tips")
plt.xlabel("x")
plt.ylabel("Average")

plt.show()
"""

# 2-2. 타이타닉 데이터
"""
import seaborn as sns
import pandas as pd
"""

# (1) 예제코드
"""
titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)
plt.show()
"""

# (2) 탑승클래스별 인원구성
"""
sns.countplot(x="class", hue="who", data=titanic)
"""

# (3) 클래스별 생존자
"""
sns.countplot(x="class", hue="alive", data=titanic)
"""

# (4) 성별별 생존자
"""
sns.countplot(x="sex", hue="alive", data=titanic)
"""

# (5) 싱글 여행자별 인원구성
"""
sns.countplot(x="alone", hue="who", data=titanic)
"""

# (6) 탑승지별 생존자의 클래스 구별
"""
sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)

plt.show()
"""

# 2-3. 주식 데이터 분석
"""
import FinanceDataReader as fdr
"""

# (1) 예제 : 2023년 종가 기준 그래프 출력
'''
df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

df0["Close"].plot()

plt.grid(True)
'''

# (2) 다우지수와 코스피 비교
"""
dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")
"""

# (3) 각 지수별 종가 기준 그래프 출력
"""
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

plt.plot(dow.index, dow.High, "r--", label="Dow")
plt.plot(kospi.index, kospi.High, "b", label="KOSPI")
"""

# 2-4. 국내 개별 종목 분석
"""
import requests
import pandas as pd
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs
"""

# (1) 국내 주식 코드 확인
"""
url = "https://finance.naver.com/item/sise_day.nhn?code={}"
"""

# (2) 데이터 파싱
"""
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))
print(table)
"""

# (3) 해당 site 1~ 100 페이지 파싱
"""
df_list = []
page = 1
for page in range(1, 100):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break
    
    print(df_list)
"""    

# (4) 데이터 처리
"""
df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.plot(df["날짜"], df["종가"], "co-")
"""

# 2-5. 미국 개별 종목 분석

import yfinance as yfinance

# (1) ticker 확인
"""
ticker = "MSFT"

ticker = "APPL"
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)
"""

# (2) 종가 기준 데이터
"""
plt.plot(data["Close"], label="Close Price")
"""

# (3) 50일 평균
"""
data["MA_50"] = data["Close"].rolling(window=50).mean()
"""

# (4) 200일 평균
"""
data["MA_200"] = data["Close"].rolling(window=200).mean(
"""

# 2-6. 국가별 인구 데이터 분석

# (1) 데이터 다운로드 및 처리

url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")