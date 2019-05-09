import os
import time
from venv.com.zjw.model.BaseModel import *


# 基础方法
class BaseService:
    baseModel = BaseModel()

    # 移动
    def move(self, position, num):
        for i in range(0, num):
            os.system(self.baseModel.MOVE + position)
            print("进行了移动操作，移动的坐标点为[{}]".format(position))

    # 点击
    def click(self, position, num):
        for i in range(0, num):
            os.system(self.baseModel.MOVE + position)
            print("进行了点击操作，点击的坐标点为[{}]".format(position))

    # 战斗
    def attack(self, position, second):
        print("开始进行攻击".format(second))
        self.move(position, 1)
        self.sleep(second)
        self.attack_close()

    # 关闭战斗按钮
    def attack_close(self):
        print("点击了关闭战斗界面按钮")
        self.move(self.baseModel.CLOSE, 1)
        self.sleep(0.5)

    # 等待
    def sleep(self, second):
        print("等待[{}]秒".format(second))
        time.sleep(second)

    # 任务背包选择
    def task_goods(self, num, goodsNum):
        # 选择背包中的第几个物品
        x = 600
        y = 750
        rangeX = 160
        rangeY = 200
        checkX = int(num % 3)
        checkY = int(num / 3) + 1
        if checkX == 0:
            checkX = 3
            checkY -= 1
        print("点击任务背包第[{}]排,第[{}]个".format(checkY, checkX))
        x = x + rangeX * (checkX - 1)
        y = y + rangeY * (checkY - 1)
        print("点击任务背包坐标[{}],[{}]".
              format(x, y))
        position = "{} {}".format(x, y)
        for i in range(0, goodsNum):
            self.click(position, 1)
