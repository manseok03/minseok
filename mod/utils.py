import math
import random
from datetime import datetime as dt

def ut_sqrt(x) :
    return math.sqrt(x)

def ut_sinpi(x) :
    return math.sin(math.pi/2)

def ut_elog(x) :
    return math.elog(math.e)

def ut_exp(x) :
    return math.exp(x)

def ut_pi() :
    return math.pi

def rd_int(x, y) :
    return random.randint(x,y)

def rd_list(this) :
    return random.choice(this)

def rd_rd() :
    return random.random()

def rd_nmvar() :
    return random.normalvariate(0,1)


def get_dtnow() :
    return dt.now()

def cvt_time2str(objtime) :
    return dt.strptime(objtime, "%Y-%m-%d")

def cvt_str2time() :
    obj = dt.now()
    return obj.strftime("%Y-%m-%d")

from datetime import datetime as dt

date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string)