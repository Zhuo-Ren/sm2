from memo_manage import MemoUnit
from datetime import datetime, date


if 1:  # 按时复习
    print("#" * 30)
    a_memo_unit = MemoUnit(unit_id="apple_listen")
    # 学习
    # 1st tests
    a_memo_unit.repo_a_test(q=3, real_time=datetime(2021, 2, 7, 22, 10, 3))
    # 计算下一次测试的时间
    print(a_memo_unit.center[-1]["plan_time"])
    # 2nd tests
    a_memo_unit.repo_a_test(q=5, real_time=datetime(2021, 2, 8, 22, 10, 3))
    # 计算下一次测试的时间
    print(a_memo_unit.center[-1]["plan_time"])
    # 3th tests
    a_memo_unit.repo_a_test(q=4, real_time=datetime(2021, 2, 14, 22, 10, 3))
    # 计算下一次测试的时间
    print(a_memo_unit.center[-1]["plan_time"])

if 1:  # 没有按时复习
    print("#" * 30)
    a_memo_unit = MemoUnit(unit_id="apple_listen")
    # 学习
    # 1st tests
    a_memo_unit.repo_a_test(q=3, real_time=datetime(2021, 2, 7, 2, 22, 22))
    # 计算下一次测试的时间
    print(a_memo_unit.center[-1]["plan_time"])
    # 2nd tests
    a_memo_unit.repo_a_test(q=5, real_time=datetime(2021, 2, 9, 3, 33, 33))
    # 计算下一次测试的时间
    print(a_memo_unit.center[-1]["plan_time"])
    # 3th tests
    a_memo_unit.repo_a_test(q=4, real_time=datetime(2021, 2, 16, 4, 44, 44))
    # 计算下一次测试的时间
    print(a_memo_unit.center[-1]["plan_time"])

# supermemo2包的效果
print("#"*30)
from supermemo2 import first_review, SMTwo
smtwo = SMTwo()
smtwo.calc(3, 2.5, 1, 1, date(2021, 2, 7))
print(smtwo.review_date)
record = smtwo.dict(curr=True)
record["quality"] = 5
smtwo.calc(**record)
print(smtwo.review_date)
record = smtwo.dict(curr=True)
record["quality"] = 4
smtwo.calc(**record)
print(smtwo.review_date)

