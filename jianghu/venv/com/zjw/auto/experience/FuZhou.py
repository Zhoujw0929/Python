# 福州练级脚本
from venv.com.zjw.auto.BaseService import *
from venv.com.zjw.model.BaseModel import *


class FuZhou:
    baseService = BaseService()
    baseModel = BaseModel()

    def __init__(self):
        print("准备开始执行福州自动挂机刷经验脚本，请[{}]秒内到达到坐标12,5处".format(self.baseModel.START_WAIT))
        self.baseService.sleep(self.baseModel.START_WAIT)
        self.baseService.attack(self.baseModel.CENTER_LEFT, 55)

    def auto(self):
        self.baseService.move(self.baseModel.CENTER_LEFT, 2)
        self.baseService.move(self.baseModel.CENTER_DOWN, 1)
        self.baseService.move(self.baseModel.CENTER_LEFT, 4)
        self.baseService.move(self.baseModel.CENTER_UP, 5)
        self.baseService.attack(self.baseModel.UP_LEFT, 55)
        self.baseService.move(self.baseModel.UP_LEFT, 2)
        self.baseService.move(self.baseModel.CENTER_DOWN, 7)
        self.baseService.move(self.baseModel.DOWN_RIGHT, 2)
        self.baseService.attack(self.baseModel.DOWN_RIGHT, 55)
        self.baseService.move(self.baseModel.DOWN_LEFT, 3)
        self.baseService.move(self.baseModel.CENTER_UP, 7)
        self.baseService.move(self.baseModel.UP_RIGHT, 3)
        self.baseService.move(self.baseModel.CENTER_DOWN, 5)
        self.baseService.move(self.baseModel.CENTER_RIGHT, 4)
        self.baseService.move(self.baseModel.CENTER_UP, 1)
        self.baseService.move(self.baseModel.CENTER_RIGHT, 2)
        self.baseService.attack(self.baseModel.CENTER_RIGHT, 55)

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
