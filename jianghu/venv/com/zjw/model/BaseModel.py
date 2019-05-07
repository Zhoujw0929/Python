import os
import time
class BaseModel:
    # 基础命令以及位置
    MOVE = "adb shell input tap "

    CENTER_LEFT = "20 840"
    CENTER_RIGHT = "1030 840"
    CENTER_UP = "540 215"
    CENTER_DOWN = "540 1520"

    DOWN_RIGHT = "1030 1520"
    DOWN_LEFT = "20 1520"

    UP_RIGHT = "1030 230"
    UP_LEFT = "50 230"

    # 关闭战斗界面
    CLOSE = "560 1565"

    # 延迟执行脚本时间
    START_WAIT = 5

    #菜单选择
    MENU_1 = "200 1650"
    MENU_2 = "477 1650"
    MENU_3 = "785 1650"

    #对话按钮选择
    CHECK_1 ="850 580"
    CHECK_2 = "850 730"
    CHECK_3 = "850 850"

    TASK_GOODS_BTN_1 = "615 1420"
    TASK_GOODS_BTN_2 = "900 1420"




