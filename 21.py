import matplotlib.pyplot as plt

# 1. 막대그래프 ---------------------------------------------------
"""
x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]
"""

# 1-1. 수평 그래프 그리기
"""
plt.bar(x_years, y_data)
"""

# (1) 그래프 설정
"""
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)
"""

# (2) 막대 문양 채우기
"""
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="///")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="////")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/////")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//////")

plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\\\")

plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+")

plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="*")

plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="o")

plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="x")

plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch=".")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="..")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="...")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="....")
"""

# 1-2. 산점도 그래프 그리기
"""
x = 1
y = 1

plt.scatter(x, y)

plt.scatter(x+1, y+1)
plt.scatter(x+2, y+1)
plt.scatter(x+3, y+1)
plt.scatter(x+3, y+2)
plt.scatter(x+3, y+1)
plt.scatter(x+3, y+3)
"""

# (1) 포인트 설정
"""
plt.scatter(x+1.5, y+1.5, 100, 2, alpah=0.5)
"""

# (2) 컬러맵 설정
"""
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="viridis")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="magma")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="infermo")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="Set1")
plt.colorbar()
"""

# 1-3. 히스토그램 그리기
"""
import numpy as np

rn = np.random.randint(1, 30, size=20)
# print(rn)

plt.hist(rn, bins=10)
plt.legend()
plt.show()
"""

# (1) 그래프 스타일 설정 (라벨 설정)
"""
plt.hist(rn,  bins=10, label="def") 
"""

# (1) 그래프 스타일 설정 (투명도 설정)
"""
plt.hist(rn,  bins=10, label="def", alpha=0.5)
plt.hist(rn,  bins=5, label="def", alpha=0.5)
"""

# (1) 그래프 스타일 설정 (그래프 스타일 설정)
"""
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step")
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="stepfilled")
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="")
"""

# 1-4. 파이챠트 그리기
"""
import platform as plat

rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]

# plat.pie({data})
plat.pie(rate)

plt.show()
"""

# (1) 라벨 표시
"""
plt.pie(rate, labels=labels)
"""

# (2) 퍼센트 표시
"""
plt.pie(rate, labels=labels, autopct='%.1d%%')
plt.pie(rate, labels=labels, autopct='%.1f%%')
plt.pie(rate, labels=labels, autopct='%.3f%%')
"""

# (3) 시작각도 설정
"""
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270)
"""

# (4) 시작방향 설정
"""
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270, counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=True)
"""

# (5) 공백 설정
"""
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0, 0, 0])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[1, 1, 1, 1])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.1, 0.1, 0.1, 0.1])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0, 0.1])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.5, 0, 0])
"""

# 1-5. 패널 스타일 설정
"""
print(plt.style.available)

plt.plot([2,3,6,7,10], [1,4,5,8,9])
plt.style.use("bmh")
plt.style.use("ggplot")
plt.style.use("classic")
plt.style.use("Solarize_Light2")
plt.style.use("dark_background")
plt.style.use("fast")
"""

# 1-6. 포맷 설정

# (1) 패널 사이즈 적용
"""
plt.rcParams['figure.figsize'] = (6, 3)
plt.rcParams['figure.figsize'] = (1, 2)
plt.rcParams['figure.figsize'] = (4, 3)
"""

# (2) 전체 폰트 사이즈 적용
"""
plt.rcParams['font.size'] = 15
plt.rcParams['font.size'] = 20
"""

# (3) 선 두께 설정
"""
plt.rcParams['lines.linewidth'] = 5
plt.rcParams['lines.linewidth'] = 50
"""

# (4) 선 스타일 설정
"""
plt.rcParams['lines.linestyle'] = '--'
"""

# (5) 눈금 설정 (위 눈금 설정)
"""
plt.rcParams['xtick.top'] = True
"""

# (5) 눈금 설정 (오른 눈금 설정)
"""
plt.rcParams['ytick.right'] = True
"""

# (5) 눈금 설정 (안쪽으로 눈금 설정)
"""
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
"""

# (5) 눈금 설정 (눈금 길이)
"""
plt.rcParams['ytick.major.size'] = 12
"""

# (5) 눈금 설정 (세부 눈금)
"""
plt.rcParams['xtick.minor.visible'] = True
"""

# 1-7. 객체 활용

# (1) 기본 예제
"""
fig, ax = plt.subplots()

ax = fig.add_axes([0, 0, 0, 0])
ax = fig.add_axes([1, 1, 0, 0])
ax = fig.add_axes([1, 1, 1, 1])
"""

# (2) 다중 패널 객체 생성
"""
fig, ax = plt.subplots(1, 1)
fig, ax = plt.subplots(1, 2)
fig, ax = plt.subplots(2, 1)
fig, ax = plt.subplots(2, 2)
fig, ax = plt.subplots(3, 2)
fig, ax = plt.subplots(3, 3)
"""

# (3) 다중 패널 그래프 출력
"""
x = [1,4,5,8,9]
y1 = [2,3,6,7,10]

fig, ax = plt.subplots(2, 2)

ax[0][0].plot(x, y1)
ax[0][1].plot(x, y1)
ax[1][0].plot(x, y1)
ax[1][1].plot(x, y1)
"""

# (4) 축 공유
"""
fig, ax = plt.subplots(2, 2, sharex=True)
fig, ax = plt.subplots(2, 2, sharey=True)
"""

# 1-8. Y축 동시 출력
"""
x = [1,4,5,8,9]

y1 = [2,3,6,7,10]
y2 = [10,8,6,4,2]

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Data")
ax1.set_ylabel("Y1")
ax1.plot(x, y1)

ax2 = ax1.twinx()
ax2.set_ylabel("Y2")
ax2.plot(x, y2)
"""

# (1) ax1 / ax2 개별 색상 설정
"""
ax1.plot(x, y1, color="C1")
ax2.plot(x, y2, color="C2")
"""

# (2) ax1 / ax2 개별 라벨 출력
"""
ax1.plot(x, y1, color="C1", label="y1 Data")
ax1.legend(loc="upper right")

ax2.plot(x, y2, color="C2", label="y2 Data")
ax2.legend(loc="lower right")
"""

# 1-9. 이종 그래프 출력

x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "-o", color="C1")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")

ax2 = ax1.twinx()
ax2.bar(x, y2, color="C2")
ax2.set_ylabel("Y2data")