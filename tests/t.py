from supermemo2 import SM2
import datetime

a_instance = SM2()
# 学习
# 第一次测试,得3分
real_date1 = datetime.date(2021, 2, 7)
q1 = 3
# 计算下一次测试的时间
a_instance.calc(
    q2=q1,
    e12=2.5,  # 第一次测试，没有e12，默认初始值为2.5
    interval12=36500,  # 第一次测试，没有interval12，可以随便写，反正这个值只是被记录而不参与运算。
    index2=1,
    plan_date2=real_date1,  # datetime.date(1992,1,10),
    real_date2=real_date1)
print(a_instance.plan_date3)
# 第二次测试，得5分
real_date2 = datetime.date(2021, 2, 9)
q2 = 5
# 计算下一次测试的时间
a_instance.calc(
    q2=q2,
    e12=a_instance.e23,
    interval12=a_instance.interval23,
    index2=a_instance.index3,
    plan_date2=a_instance.plan_date3,
    real_date2=real_date2
)
print(a_instance.plan_date3)

