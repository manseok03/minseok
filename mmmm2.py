# 문자열을 날짜로 변환

"""from datetime import datetime as dt

date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)"""

# 날짜를 문자열로 변환

"""from datetime import datetime as dt

date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string)"""

# 현재 시간 출력

"""from datetime import datetime as dt

print(dt.now())"""

# 모듈화

"""import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time()
print(res)"""

# os 모듈 확인

"""import os"""

# 현재 작업 디렉토리 출력

"""print(os.getcwd())"""

# 디렉토리 변경

"""os.chdir('../')"""

# 변경된 디렉토리 출력

"""print(os.getcwd())"""

# 파일 목록 출력

"""print(os.listdir())"""

# 디렉토리 생성

"""os.mkdir('new_directory')
print(os.listdir())"""

# 디렉토리 삭제

"""os.rmdir('new_directory')
print(os.listdir())"""

#

"""import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())"""

#

"""import sys
print(sys.version)
print(sys.argv)"""

# 스택 생성, 값 넣기, 상태 확인, 값 빼기

"""st = []

st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

print(st)

top = st.pop()
print(top)
print(st)
print(len(st))"""

# 큐 생성, 값 넣기, 상태 확인, 값 빼기

"""queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

front = queue.pop(0)
print(front) # 1
print(queue) # [2, 3]
print(len(queue))"""