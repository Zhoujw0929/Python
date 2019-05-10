# 太乙钓鱼脚本
from venv.com.zjw.auto.BaseService import *
from venv.com.zjw.model.BaseModel import *


class DiaoYu:
    baseService = BaseService()
    baseModel = BaseModel()

    def __init__(self):
        print("准备开始执行太乙自动挂机钓鱼脚本，请[{}]秒内到达到坐标28,20处".format(self.baseModel.START_WAIT))
        self.baseService.sleep(self.baseModel.START_WAIT)

    def auto(self):
        self.baseService.click(self.baseModel.MENU_1, 1)
        self.baseService.click(self.baseModel.CHECK_3, 1)
        self.baseService.click(self.baseModel.CHECK_1, 1)
        self.baseService.sleep(10)

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
            print("当前执行第[{}]轮.".format(i + 1))
            self.auto()
