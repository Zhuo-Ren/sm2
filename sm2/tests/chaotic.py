from sm2 import SM2
import datetime

SM2.LAWFUL_or_CHAOTIC = "CHAOTIC"

if 1:  # 按时复习
    print("#" * 30)
    a_instance = SM2()
    # 学习
    # 1st tests
    a_instance[-1]["real_time"] = datetime.datetime(2021, 2, 7, 22, 10, 3)  # 或datetime.date(2021, 2, 7)
    a_instance[-1]["q"] = 3
    # 计算下一次测试的时间
    a_instance.calc()
    print(a_instance[-1]["plan_time"])
    # 2nd tests
    a_instance[-1]["real_time"] = datetime.datetime(2021, 2, 8, 22, 10, 3)
    a_instance[-1]["q"] = 5
    # 计算下一次测试的时间
    a_instance.calc()
    print(a_instance[-1]["plan_time"])
    # 3th tests
    a_instance[-1]["real_time"] = datetime.datetime(2021, 2, 14, 22, 10, 3)
    a_instance[-1]["q"] = 4
    # 计算下一次测试的时间
    a_instance.calc()
    print(a_instance[-1]["plan_time"])

if 1:  # 没有按时复习
    print("#" * 30)
    a_instance = SM2()
    # 学习
    # 1st tests
    a_instance[-1]["real_time"] = datetime.datetime(2021, 2, 7, 2, 22, 22)
    a_instance[-1]["q"] = 3
    # 计算下一次测试的时间
    a_instance.calc()
    print(a_instance[-1]["plan_time"])
    # 2nd tests
    a_instance[-1]["real_time"] = datetime.datetime(2021, 2, 9, 3, 33, 33)
    a_instance[-1]["q"] = 5
    # 计算下一次测试的时间
    a_instance.calc()
    print(a_instance[-1]["plan_time"])
    # 3th tests
    a_instance[-1]["real_time"] = datetime.datetime(2021, 2, 16, 4, 44, 44)
    a_instance[-1]["q"] = 4
    # 计算下一次测试的时间
    a_instance.calc()
    print(a_instance[-1]["plan_time"])

# supermemo2包的效果
print("#"*30)
from supermemo2 import first_review, SMTwo
smtwo = SMTwo()
smtwo.calc(3, 2.5, 1, 1, datetime.date(2021, 2, 7))
print(smtwo.review_date)
record = smtwo.dict(curr=True)
record["quality"] = 5
smtwo.calc(**record)
print(smtwo.review_date)
record = smtwo.dict(curr=True)
record["quality"] = 4
smtwo.calc(**record)
print(smtwo.review_date)

