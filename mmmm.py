"""def prt_func() :
    print("hello")

def callfunc(fx) :
		fx()

callfunc(prt_func)"""

"""def prt_func(n) :
    print("hello", n)

def callfunc(fx) :
    for i in range(5) :
        fx(i)

callfunc(prt_func)"""

"""def update_msg(name: str) -> list:
    msg = []
    msg.append("Hello, " + name)
    msg.append("Bye, " + name)
    return msg

def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg

res = greeting("python")

for message in res:
    print(message)"""
    
"""def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1)"""

"""def ploop(n) :
    if n == 0:
        print("end")
        return 1
    else :
        print(n, n-1, " = ", n + n-1)
        
print(ploop(5))"""

"""ef fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4)
print("res = ", res)"""

"""import calc

print(dir(calc))"""

"""import calc

# res = calc.add(8, 5)
# print(res)
print(calc.add(8, 4))
print(calc.sub(8, 4))
print(calc.mul(8, 4))
print(calc.div(8, 4))"""

"""import calc as cl

# res = calc.add(8, 5)
# print(res)
print(cl.add(6, 3))
print(cl.sub(6, 3))
print(cl.mul(6, 3))
print(cl.div(6, 3))"""

"""import mod.circle_mod as cm

print(cm.pi)

print(cm.cc_area(4))
print(cm.cc_len(5))"""

"""def curstr(st, wd, idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = curstr(url, "/", 3)
print(rs)"""

"""import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)
print(res)"""

"""import math

sq_res = math.sqrt(6)
print(sq_res)

sp_res = math.sin(math.pi /2)
print(sp_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

fc_res = math.factorial(4)
print(fc_res)"""

"""import mod.utils as mu

res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog()
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi)"""

"""import random as rd

res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres)"""