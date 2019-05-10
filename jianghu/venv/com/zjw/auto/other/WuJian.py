# 华山悟剑脚本
from venv.com.zjw.auto.BaseService import *
from venv.com.zjw.model.BaseModel import *


class WuJian:
    baseService = BaseService()
    baseModel = BaseModel()

    def __init__(self):
        print("准备开始执行悟剑自动挂机脚本，请[{}]秒内到达华山坐标24,15处".format(self.baseModel.START_WAIT))
        self.baseService.sleep(self.baseModel.START_WAIT)

    def auto(self):
        self.baseService.task_goods(1,1)
        self.baseService.click(self.baseModel.TASK_GOODS_BTN_2, 1)
        self.baseService.click(self.baseModel.CLOSE,1)
        self.baseService.sleep(2)
        self.baseService.move(self.baseModel.CLOSE,1)

    def start(self, num):
        self.baseService.click(self.baseModel.MENU_1, 1)
        self.baseService.click(self.baseModel.CHECK_3, 1)
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