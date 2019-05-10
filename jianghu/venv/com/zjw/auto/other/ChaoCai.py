# 临安练级脚本
from venv.com.zjw.auto.BaseService import *
from venv.com.zjw.model.BaseModel import *


class ChaoCai:
    baseService = BaseService()
    baseModel = BaseModel()

    def __init__(self):
        print("准备开始执行华山自动挂机炒菜脚本，请[{}]秒内到达到坐标10,1处".format(self.baseModel.START_WAIT))
        # self.baseService.sleep(self.baseModel.START_WAIT)
        self.baseService.click(self.baseModel.MENU_3, 1)

    def auto(self):
        self.baseService.click(self.baseModel.CHECK_2, 1)
        # self.baseService.task_goods(5, 3)
        # self.baseService.task_goods(8, 1)
        # self.baseService.task_goods(9, 1)
        self.baseService.task_goods(6, 3)
        self.baseService.task_goods(7, 2)
        self.baseService.click(self.baseModel.TASK_GOODS_BTN_1,1)
        self.baseService.click(self.baseModel.CHECK_1, 1)
        self.baseService.sleep(6)

    def start(self, num):
        if num == -1:
            print("脚本执行次数不限，已开始")
            i = 1
            while i:
                print("当前执行第[{}]轮.".format(i))
                i += 1
                self.auto()
        print("脚本执行次数[{}]次,已开始".format(num))
        for i in range(0, num):
            print("当前执行第[{}]轮.".format(i))
            self.auto()