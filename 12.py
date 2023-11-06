# 입력 암호화
"""
import getpass

# pw = getpass.getpass("Pass : ")
pw = input("Pass :")
print(pw)"""

# 해시알고리즘
"""
import hashlib

hl = hashlib.sha256()
target = "hello"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())"""

# keccak256
"""
import Crypto.Hash.keccak as kek

target = "to be or not to be, That is a question"

kksh = keccak.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest())"""

# 입력키 변환
"""
import getpass
import hashlib

pw = getpass.getpass("Pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest())"""

# 암호화 파일 저장
"""
import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True

if pwInsert():
    pw = input('new pass :')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password")"""
    
# 시스템정보 확인
"""
import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)"""

# 웹페이지 읽기 1
"""
import urllib.request as ur

# url = 'https://www.google.com'
url = "https://daum.net"
# url = "https://xkcd.com/"

# res = urllib.request.urlopen(url)
res = ur.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)

# print(web.decode('utf-8'))
print(web)"""

# 웹페이지 읽기 2
"""
import http.client as hc

# url = "https://www.gogle.com"
url = "www.gogle.com"
# conn = http.client.HTTPSConnection(url)
conn = hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulcl.html", "wb") as fp:
    fp.write(r.read())
    
conn.close()

print(r)"""

# # 웹페이지 읽기 3
"""
import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)
    
print(web)"""

# 싱글스레드
"""
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()

for i in range(3) :
    counter(f"num{i}")
    
    end = time.time()

print("single end")   
print("single end", end - start)"""

# 멀티스레드
"""
import threading as td
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

start = time.time()

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

end = time.time()

# print("multi end")
print("multi end", end - start)"""

# 멀티프로세싱
"""
import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
process1 = mp.Process(target=counter, args=("1num",))
process2 = mp.Process(target=counter, args=("2num", ))
process3 = mp.Process(target=counter, args=("3num", ))

start = time.time()

process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()

end = time.time()

print("proc-end", end - start)"""

# main 실행

def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run()