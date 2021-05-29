import json
from datetime import date, timedelta


class SM2(list):  # sm-2 类
    LAWFUL_or_CHAOTIC = "CHAOTIC"
    INIT_INTERVAL = -1
    INIT_E = 2.5

    def __init__(self, item_id, log=None):
        """
        Init a SM2 obj.

        :param item_id: id of this item.
        :param log: test log of this item.
        :type log: list
        """
        # public: item_id
        if item_id is None:
            raise TypeError
        else:
            self.item_id = item_id

        #
        if log is None:
            self.append({
                "step": 0, "plan_time": None, "real_time": None, "q": None,
                "interval": SM2.INIT_INTERVAL, "e": SM2.INIT_E
            })
            self.append({
                "step": 1, "plan_time": None, "real_time": None, "q": None,
                "interval": None, "e": None
            })
        else:
            if not isinstance(log, list):
                raise TypeError
            else:
                self.extend(log)

    def calc(self):
        """
        如果当前测试信息self[-1]["step"、"plan_time"、"real_time"、"q"]存在时，
        计算下次测试的时间.

        :return: Non return, self.log is changed.
        """
        # 必须提供本次测试的信息，才能计算下次测试的时间
        if self[-1]["step"] is None:
            raise TypeError
        if self[-1]["plan_time"] is None and SM2.LAWFUL_or_CHAOTIC == "LAWFUL":
            raise TypeError
        if self[-1]["real_time"] is None and SM2.LAWFUL_or_CHAOTIC == "CHAOTIC":
            raise TypeError
        if self[-1]["q"] is None:
            raise TypeError

        # add info of next tests
        self.append({
            "step": None, "plan_time": None, "real_time": None, "q": None,
            "interval": None, "e": None
        })

        #
        if self[-2]["q"] < 3:  # 当q小于3的时候,从头再开始的循环.且EF不变.
            # 第一次复习在1天后
            self[-2]["interval"] = timedelta(days=1)
            self[-1]["step"] = 1
        else:
            if self[-2]["step"] == 1:
                self[-2]["interval"] = timedelta(days=1)
            elif self[-2]["step"] == 2:
                self[-2]["interval"] = timedelta(days=6)
            else:
                interval = round(self[-3]["interval"].days * self[-3]["e"])
                self[-2]["interval"] = timedelta(days=interval)

            self[-1]["step"] = self[-2]["step"] + 1

        self[-2]["e"] = self[-3]["e"] - 0.8 + 0.28 * self[-2]["q"] - 0.02 * self[-2]["q"] ** 2
        if self[-2]["e"] < 1.3:
            self[-2]["e"] = 1.3

        if SM2.LAWFUL_or_CHAOTIC == "LAWFUL":
            self[-1]["plan_time"] = self[-2]["plan_time"] + self[-2]["interval"]
        elif SM2.LAWFUL_or_CHAOTIC == "CHAOTIC":
            self[-1]["plan_time"] = self[-2]["real_time"] + self[-2]["interval"]

    # def dict(self, prev=None, curr=None):
    #     """
    #
    #     :param prev: 只输出上次测试的信息，如果prev是True
    #     :param curr: 只输出这次测试的信息，如果curr是True
    #     :return: 以字典形式返回MS2对象中的信息。
    #     """
    #     try:
    #         attrs = {"q2": self.__q2}
    #         prev_attrs = {
    #             "e12": self.__prev.e12,
    #             "interval12": self.__prev.interval12,
    #             "index2": self.__prev.index2,
    #             "plan_date2": self.__prev.plan_date2
    #         }
    #         cur_attrs = {
    #             "e23": self.__e23,
    #             "interval23": self.__interval23,
    #             "index3": self.__index3,
    #             "plan_date3": self.__plan_date3
    #         }
    #     except AttributeError:
    #         raise CalcNotCalledYet
    #
    #     if prev:
    #         attrs.update(prev_attrs)
    #     elif curr:
    #         attrs.update(cur_attrs)
    #     else:
    #         attrs.update(prev_attrs)
    #         attrs.update(cur_attrs)
    #
    #     return attrs
    #
    # def json(self, prev=None, curr=None):
    #     attrs = self.dict(prev=prev, curr=curr)
    #     return json.dumps(attrs)
