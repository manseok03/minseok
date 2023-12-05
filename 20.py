# 1. 데이터 시각화 -------------------------------------------------------

# (1) 모듈 선언

import matplotlib.pyplot as plt

# 1-1. 선 스타일 설정

# (1) 선 스타일 지정
"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")
"""

# (2) 선 스타일 수동 지정
"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 1)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (5, 10)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (5, 5)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (3, 10, 1, 10)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (3, 5, 1, 5)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (3, 5, 1, 1)), label="PData(km)")
"""

# (3) 문자열 색 지정
"""
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
"""

# (4) 키워드 색 지정
"""
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="lime", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
"""

# (5) hex - rgb값 적용 색 지정
"""
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#35FA8D", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#51EEFF", label="Value(m)")
"""

# (6) 지정 키 색 지정
"""
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C2", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C3", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C4", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C5", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")
"""

# (7) 모양 설정
"""
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)"
"""

# 1-2. 마커 지정
"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")
"""

# (1) 마커 / 선 동시 설정
"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-.", label="PData(km)")
"""

# (2) marker 파라메터 사용
"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="D", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="X", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$y$", label="PData(km)")
"""

# 1-3. 그래프 영역 채우기
"""
xdata = [2, 3, 6, 7, 10]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]

plt.plot(xdata, ydata)
plt.plot("x_data")
plt.plot("y_data")
"""

# (1) 세로 축 채우기
"""
plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
plt.fill_between(xdata[:4], ydata[:4], alpha=0.5)
plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)
"""

# (2) 가로 축 채우기
"""
plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
plt.fill_betweenx(ydata[:4], xdata[:4], alpha=0.3)
plt.fill_betweenx(ydata[1:5], xdata[1:5], alpha=0.3)
"""

# (3) 두 선간의 영역 채우기
"""
plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
"""

# (4) 범위 지정 영역 채우기
"""
plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 4.5, 2.5], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 4.5, 2.5], alpha=0.3)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 4.5, 2.5], alpha=1)
"""

# 1-4. 배경 설정
"""
plt.grid()
plt.grid(axis="x")
plt.grid(axis="y")
"""

# (1) 그리드 설정 (색상 설정)
"""
plt.grid(axis="y", color="g")
plt.grid(axis="y", color="b")
"""

# (1) 그리드 설정 (투명도 설정)
"""
plt.grid(axis="y", color="g", alpha=0.5)
plt.grid(axis="y", color="g", alpha="-")
plt.grid(axis="x", color="r", alpha="-")
"""

# (1) 그리드 설정 (선 종류 선택)
"""
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
plt.grid(axis="y", color="g", alpha=0.5, linestyle="--")
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")
plt.grid(axis="x", color="r", alpha=0.5, linestyle="-.")
"""

# (2) 눈금표시
"""
plt.xticks()
plt.yticks()
"""

# (2) 눈금표시 (임의 데이터 지정)
"""
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
"""

# (2) 눈금표시 (라벨 지정)
"""
plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
"""

# (2) 눈금표시 (눈금 안쪽/바깥쪽)
"""
plt.tick_params(axis="x", direction="in")
plt.tick_params(axis="x", direction="out")
plt.tick_params(axis="y", direction="in")
"""

# 1-5. 막대그래프 그리기

x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

"""
plt.bar(x_years, y_data)
plt.show()
"""

# (1) 색 지정
"""
plt.bar(x_years, y_data, color="g")
plt.bar(x_years, y_data, color="C7")
plt.bar(x_years, y_data, color="#75FA8D")
"""

# (2) 개별 색 지정
"""
plt.bar(x_years, y_data, color=clr)
"""

# (3) 막대 너비 설정
"""
plt.bar(x_years, y_data, color=clr, width=2)
plt.bar(x_years, y_data, color=clr, width=0.5)
plt.bar(x_years, y_data, color=clr, width=0.1)
"""

# (4) 막대 위치 선정 edge/center
"""
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", width=0.5)
"""

# (5) 막대 테두리 설정 (라인 색 선택)
"""
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)
"""

# (5) 막대 테두리 설정 (테두리 라인 설정)
"""
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="blue", linewidth=3, width=0.5)
"""

# (6) 축 지표 설정
"""
plt.xticks(x_years)
plt.yticks(y_data, y_data)
plt.yticks(100, 200, 300, 400, 500, 900)
"""

# 1-6. 수평 그래프 그리기

plt.barh(x_years, y_data)

# (1) 그래프 설정

plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.show()