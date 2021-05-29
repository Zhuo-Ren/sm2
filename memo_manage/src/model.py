from sm2 import SM2
from typing import Dict
from datetime import datetime


SM2.LAWFUL_or_CHAOTIC = "CHAOTIC"


class MemoUnit(object):
    INIT_PLAN_TIME = datetime(1949, 1, 10)

    def __init__(self, unit_id, log=None):
        # public: unit_id
        if unit_id is None:
            raise TypeError
        else:
            self.unit_id = unit_id

        # public: center
        if log:
            self.center = SM2(item_id=self.unit_id, log=log)
        else:
            self.center = SM2(item_id=self.unit_id)

    def state(self):
        if self.center[1]["plan_time"] is None:
            return "sleep"
        else:
            return "active"

    def active(self):
        self.center[1]["plan_time"]=MemoUnit.INIT_PLAN_TIME

    def repo_a_test(self, q, real_time=datetime.now(), calc=True):
        self.center[-1]["real_time"] = real_time
        self.center[-1]["q"] = q
        if calc:
            self.calc()

    def calc(self):
        self.center.calc()
        return self.center[-1]["plan_time"]


class MemoGroup(Dict[str, MemoUnit]):
    TASK_TYPE = [
        "reading",  # 读
        "listening",  # 听
        "usage",  # 用
        "recognizing",  # 认
        "spelling",  # 拼
    ]

    def __init__(self, from_info=None):
        if isinstance(from_info, dict):
            for k, v in from_info.items():
                self.append(MemoUnit(unit_id=k, log=v))

    def append(self, a_memo_unit: MemoUnit):
        self[a_memo_unit.unit_id] = a_memo_unit

    def all_keys(self):
        return list(self.keys())

    def sleep_keys(self):
        r = []
        for k, v in self.items():
            if v.center[1]["plan_time"] is None:
                r.append(k)
        return r

    def active_keys(self):
        r = []
        for k, v in self.items():
            if v.center[1]["plan_time"] is not None:
                r.append(k)
        return r

    def on_test_keys(self, deadline=datetime.now()):
        r = []
        for k, v in self.items():
            if v.center[-1]["plan_time"] is not None:
                if v.center[-1]["plan_time"] < deadline:
                    r.append(k)
        return r

    def item_keys(self, item, deadline=datetime.now()):
        """
        One item can have multi tasks.
        This function returns all tasks of given item.
        For example::
            >>> a = MemoGroup()
            >>> a.item_keys("apple")
            {
                "apple_reading": "none",
                "apple_listening": "active",
                ...
            }

        :param item:
        :type item: str
        :return:
        :rtype: dict
        """
        r = {}
        for task_type in self.TASK_TYPE:
            task_name = item + "_" + task_type
            if task_name not in self:
                r[task_name] = "none"
            elif self[task_name].center[1]["plan_time"] is None:
                r[task_name] = "sleep"
            elif self[task_name].center[-1]["plan_time"] >= deadline:
                r[task_name] = "active"
            else:
                r[task_name] = "test"
        return r



