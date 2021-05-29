from memo_manage import MemoGroup, MemoUnit
import datetime


cet4_tasks = MemoGroup()

cet4_tasks.append(MemoUnit(unit_id="apple_pronunciation"))
cet4_tasks.append(MemoUnit(unit_id="apple_recognition"))
cet4_tasks.append(MemoUnit(unit_id="apple_using"))
cet4_tasks.append(MemoUnit(unit_id="apple_listen"))
cet4_tasks.append(MemoUnit(unit_id="dog_pronunciation"))
cet4_tasks.append(MemoUnit(unit_id="dog_recognition"))
cet4_tasks.append(MemoUnit(unit_id="dog_using"))
cet4_tasks.append(MemoUnit(unit_id="dog_listen"))

print("所有:", cet4_tasks.all_keys())
print("睡眠:", cet4_tasks.sleep_keys())
print("激活:", cet4_tasks.active_keys())
print("待测:", cet4_tasks.on_test_keys())

cet4_tasks["apple_recognition"].active()
cet4_tasks["apple_using"].active()
cet4_tasks["apple_listen"].active()
cet4_tasks["dog_pronunciation"].active()
cet4_tasks["dog_recognition"].active()
cet4_tasks["dog_using"].active()
cet4_tasks["dog_listen"].active()

print("所有:", cet4_tasks.all_keys())
print("睡眠:", cet4_tasks.sleep_keys())
print("激活:", cet4_tasks.active_keys())
print("待测:", cet4_tasks.on_test_keys())

cet4_tasks["apple_recognition"].repo_a_test(q=1, real_time=datetime.datetime(2020,1,10,12,2,2))
cet4_tasks["apple_using"].repo_a_test(q=2, real_time=datetime.datetime(2020,1,10,12,2,2))
cet4_tasks["apple_listen"].repo_a_test(q=3, real_time=datetime.datetime(2020,1,10,12,2,2))
cet4_tasks["dog_pronunciation"].repo_a_test(q=4, real_time=datetime.datetime(2020,1,10,12,2,2))
cet4_tasks["dog_recognition"].repo_a_test(q=5, real_time=datetime.datetime(2020,1,10,12,2,2))
cet4_tasks["dog_using"].repo_a_test(q=4, real_time=datetime.datetime(2020,1,10,12,2,2))
cet4_tasks["dog_listen"].repo_a_test(q=3, real_time=datetime.datetime(2020,1,10,12,2,2))

cet4_tasks["apple_recognition"].repo_a_test(q=1, real_time=datetime.datetime(2020,1,11,12,2,2))
cet4_tasks["apple_using"].repo_a_test(q=2, real_time=datetime.datetime(2020,1,11,12,2,2))
cet4_tasks["apple_listen"].repo_a_test(q=3, real_time=datetime.datetime(2020,1,12,12,2,2))
cet4_tasks["dog_pronunciation"].repo_a_test(q=4, real_time=datetime.datetime(2020,1,11,12,2,2))
cet4_tasks["dog_recognition"].repo_a_test(q=5, real_time=datetime.datetime(2020,1,11,12,2,2))
cet4_tasks["dog_using"].repo_a_test(q=4, real_time=datetime.datetime(2020,1,13,12,2,2))
cet4_tasks["dog_listen"].repo_a_test(q=3, real_time=datetime.datetime(2020,1,13,12,2,2))

print(cet4_tasks["apple_recognition"].center[-1]["plan_time"])
print(cet4_tasks["apple_using"].center[-1]["plan_time"])
print(cet4_tasks["apple_listen"].center[-1]["plan_time"])
print(cet4_tasks["dog_pronunciation"].center[-1]["plan_time"])
print(cet4_tasks["dog_recognition"].center[-1]["plan_time"])
print(cet4_tasks["dog_using"].center[-1]["plan_time"])
print(cet4_tasks["dog_listen"].center[-1]["plan_time"])

cet4_tasks_dict = {}
for k,v in cet4_tasks.items():
    log = []
    log.extend(v.center)
    cet4_tasks_dict[k] = log
print(cet4_tasks_dict)
cet4_tasks_2 = MemoGroup(from_info=cet4_tasks_dict)

print(cet4_tasks_2["apple_recognition"].center[-1]["plan_time"])
print(cet4_tasks_2["apple_using"].center[-1]["plan_time"])
print(cet4_tasks_2["apple_listen"].center[-1]["plan_time"])
print(cet4_tasks_2["dog_pronunciation"].center[-1]["plan_time"])
print(cet4_tasks_2["dog_recognition"].center[-1]["plan_time"])
print(cet4_tasks_2["dog_using"].center[-1]["plan_time"])
print(cet4_tasks_2["dog_listen"].center[-1]["plan_time"])



