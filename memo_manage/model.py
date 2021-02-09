from sm2 import SM2
from typing import Dict
from datetime import datetime


SM2.LAWFUL_or_CHAOTIC = "CHAOTIC"


class MemoUnit(object):
    INIT_PLAN_TIME = datetime(1949, 1, 10)

    def __init__(self, unit_id):
        self.unit_id = unit_id
        self.center = SM2()

    def state(self):
        if self.center.log[1]["plan_time"] is None:
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
    def __init__(self):
        pass

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
