import json
from datetime import date, timedelta

import attr

from .exceptions import CalcNotCalledYet


@attr.s
class SM2:  # sm-2 类
    """1,2,3分别代表上次测试，这次测试，下次测试"""
    __q2 = attr.ib(
        init=False,
        validator=[
            attr.validators.instance_of(int),
            attr.validators.in_(range(6))
        ],
        on_setattr=attr.setters.validate
    )  # 本次测试的得分。整数0,1,2,3,4,5中之一。
    __e23 = attr.ib(init=False)  # sm-2中的EF，1.3到2.5之间。
    __interval23 = attr.ib(init=False)  # 间隔天数，大于等于1的整数
    __index3 = attr.ib(init=False)  # 下一次是第几次复习，从1开始
    __plan_date3 = attr.ib(init=False)  # 应该在啥时候进行下一次复习
    __prev = attr.ib(init=False)  # Prev对象

    """
    用户学习完。
    立马进行第1次测试，得分q1。
    预测：用户应该在__interval=1天后的__review_date那天进行第__repetitions=2次复习。
    更新EF
    进行第2次测试，得分q2。
    预测：用户应该在__interval天后的__review_date那天进行第__repetitions=3次复习。
    """
    @property
    def q2(self):
        return self.__q2

    @property
    def e23(self):
        return self.__e23

    @property
    def interval23(self):
        return self.__interval23

    @property
    def index3(self):
        return self.__index3

    @property
    def plan_date3(self):
        return self.__plan_date3

    @property
    def prev(self):
        return self.__prev

    @attr.s
    class Prev:
        __e12 = attr.ib(validator=attr.validators.instance_of(float))
        __interval12 = attr.ib(validator=attr.validators.instance_of(int))
        __index2 = attr.ib(validator=attr.validators.instance_of(int))
        __plan_date2 = attr.ib(validator=attr.validators.instance_of(date))

        @__e12.validator
        def __check_valid_easiness(self, attribute, value):
            if value < 1.3:
                message = "easiness has a minimum value of 1.3"
                raise ValueError(message)

        @__interval12.validator
        def __check_valid_interval(self, attribute, value):
            if value < 1:
                message = "interval has a minimum value of 1"
                raise ValueError(message)

        @__index2.validator
        def __check_valid_repetitions(self, attribute, value):
            if value < 1:
                message = "repetitions has a minimum value of 1"
                raise ValueError(message)

        @property
        def interval12(self):
            return self.__interval12

        @property
        def e12(self):
            return self.__e12

        @property
        def index2(self):
            return self.__index2

        @property
        def plan_date2(self):
            return self.__plan_date2

    def calc(self, q2, e12, interval12, index2, plan_date2, real_date2=None):
        self.__q2 = q2
        self.__prev = self.Prev(e12, interval12, index2, plan_date2)

        if q2 < 3:  # 当q小于3的时候,从头再开始的循环.且EF不变.
            # 第一次复习在1天后
            self.__interval23 = 1
            self.__index3 = 1
        else:
            if index2 == 1:
                self.__interval23 = 1
            elif index2 == 2:
                self.__interval23 = 6
            else:
                self.__interval23 = round(interval12 * e12)

            self.__index3 = index2 + 1

        self.__e23 = e12 - 0.8 + 0.28 * q2 - 0.02 * q2 ** 2
        if self.__e23 < 1.3:
            self.__e23 = 1.3

        self.__plan_date3 = plan_date2 + timedelta(days=self.__interval23)
        # self.__plan_date3 = real_date2 + timedelta(days=self.__interval23)

    def dict(self, prev=None, curr=None):
        """

        :param prev: 只输出上次测试的信息，如果prev是True
        :param curr: 只输出这次测试的信息，如果curr是True
        :return: 以字典形式返回MS2对象中的信息。
        """
        try:
            attrs = {"q2": self.__q2}
            prev_attrs = {
                "e12": self.__prev.e12,
                "interval12": self.__prev.interval12,
                "index2": self.__prev.index2,
                "plan_date2": self.__prev.plan_date2
            }
            cur_attrs = {
                "e23": self.__e23,
                "interval23": self.__interval23,
                "index3": self.__index3,
                "plan_date3": self.__plan_date3
            }
        except AttributeError:
            raise CalcNotCalledYet

        if prev:
            attrs.update(prev_attrs)
        elif curr:
            attrs.update(cur_attrs)
        else:
            attrs.update(prev_attrs)
            attrs.update(cur_attrs)

        return attrs

    def json(self, prev=None, curr=None):
        attrs = self.dict(prev=prev, curr=curr)
        return json.dumps(attrs)
