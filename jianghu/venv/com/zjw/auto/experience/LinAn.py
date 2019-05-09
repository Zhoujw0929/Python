# 临安练级脚本
from venv.com.zjw.auto.BaseService import *
from venv.com.zjw.model.BaseModel import *


class LinAn:
    baseService = BaseService()
    baseModel = BaseModel()

    def __init__(self):
        print("准备开始执行临安自动挂机刷经验脚本，请[{}]秒内到达到坐标26,28处".format(self.baseModel.START_WAIT))
        self.baseService.sleep(self.baseModel.START_WAIT)

    def auto(self):
        self.baseService.attack(self.baseModel.CENTER_RIGHT, 35)
        self.baseService.move(self.baseModel.CENTER_LEFT, 1)
        self.baseService.move(self.baseModel.CENTER_DOWN, 1)
        self.baseService.move(self.baseModel.CENTER_LEFT, 2)
        self.baseService.move(self.baseModel.CENTER_DOWN, 1)
        self.baseService.move(self.baseModel.CENTER_LEFT, 1)
        self.baseService.move(self.baseModel.CENTER_DOWN, 2)
        self.baseService.move(self.baseModel.CENTER_LEFT, 1)
        self.baseService.attack(self.baseModel.CENTER_DOWN, 40)
        self.baseService.move(self.baseModel.CENTER_UP, 1)
        self.baseService.move(self.baseModel.CENTER_RIGHT, 5)
        self.baseService.attack(self.baseModel.CENTER_UP, 45)
        self.baseService.move(self.baseModel.CENTER_DOWN, 1)
        self.baseService.move(self.baseModel.CENTER_LEFT, 4)
        self.baseService.move(self.baseModel.CENTER_UP, 2)
        self.baseService.move(self.baseModel.CENTER_RIGHT, 4)
        self.baseService.move(self.baseModel.CENTER_UP, 1)

    def start(self, num):
        if num == -1:
            print("脚本执行次数不限，已开始")
            i = 1
            while i:
                self.auto()
        print("脚本执行次数[{}]次,已开始".format(num))
        for i in range(0, num):
            self.auto()
