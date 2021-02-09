# Introduction
This is a Python implement of SM-2 arithmetic.
You can get a introduction of this arithmetic from
 `https://www.supermemo.com/en/archives1990-2015/english/ol/sm2` 
 or `./sm2-intro` (in Chinese).

# Example
## Init
Import the package.

    from sm2 import SM2
    import datetime

Config the package. "LAWFUL" means user will test the item
at the plan time that given by the SM-2 arithmetic each time.
就是说用户严格按照算法计算的时间进行测试(复习)，不会提前，也不会更晚。

    SM2.LAWFUL_or_CHAOTIC = "LAWFUL"

Create a item obj.
    
    a_instance = SM2()
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=None, real_time=None, q=None, interval=None, e=None

# 1th test
In 2021.2.7, user test the item for the 1st time and get 3 points.

    a_instance[-1]["plan_time"] = datetime.date(2021, 2, 7)
    a_instance[-1]["q"] = 3
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=None, e=None

Calc the plan time for the next test.

    a_instance.calc()
    print(a_instance[-1]["plan_time"])  # 2021-02-08
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=1, e=2.36
- 2: step=2, plan_time=2021-2-8, real_time=None, q=None, interval=None, e=None

# 2nd test
In the return day (2021.2.8), user test the item for the 2nd time and get 5 points.
    a_instance[-1]["q"] = 5
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=1, e=2.36
- 2: step=2, plan_time=2021-2-8, real_time=None, q=5, interval=None, e=None

Calc the plan time for the next test.

    a_instance.calc()
    print(a_instance[-1]["plan_time"])  # 2021-02-14
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=1, e=2.36
- 2: step=2, plan_time=2021-2-8, real_time=None, q=5, interval=6, e=2.46
- 3: step=3, plan_time=2021-2-14, real_time=None, q=None, interval=None, e=None

# 3th tests
In the return day (2021.2.14), user test the item for the 3th time and get 4 points.
    
    a_instance[-1]["q"] = 4
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=1, e=2.36
- 2: step=2, plan_time=2021-2-8, real_time=None, q=5, interval=6, e=2.46
- 3: step=3, plan_time=2021-2-14, real_time=None, q=4, interval=None, e=None

Calc the plan time for the next test.

    a_instance.calc()
    print(a_instance[-1]["plan_time"])  # 2021-03-01
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=1, e=2.36
- 2: step=2, plan_time=2021-2-8, real_time=None, q=5, interval=6, e=2.46
- 3: step=3, plan_time=2021-2-14, real_time=None, q=4, interval=15, e=2.46
- 4: step=4, plan_time=2021-3-1, real_time=None, q=None, interval=None, e=None

# 4th tests
In the return day (2021.3.1), user test the item for the 4th time and get 2 points.

**If user get a score less than 3, 
the arithmetic will return to step 1 without update the e.**

    a_instance[-1]["q"] = 2
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=1, e=2.36
- 2: step=2, plan_time=2021-2-8, real_time=None, q=5, interval=6, e=2.46
- 3: step=3, plan_time=2021-2-14, real_time=None, q=4, interval=15, e=2.46
- 4: step=4, plan_time=2021-3-1, real_time=None, q=2, interval=None, e=None

Calc the plan time for the next test.

    a_instance.calc()
    print(a_instance[-1]["plan_time"])  # 2021-03-02
    
After the above commend, the item obj maintain a log as:
- 0: step=0, plan_time=None, real_time=None, q=None, interval=-1, e=2.5
- 1: step=1, plan_time=2021-2-7, real_time=None, q=3, interval=1, e=2.36
- 2: step=2, plan_time=2021-2-8, real_time=None, q=5, interval=6, e=2.46
- 3: step=3, plan_time=2021-2-14, real_time=None, q=4, interval=15, e=2.46
- 4: step=4, plan_time=2021-3-1, real_time=None, q=2, interval=1, e=2.14
- 5: step=1, plan_time=2021-3-2, real_time=None, q=None, interval=None, e=????







