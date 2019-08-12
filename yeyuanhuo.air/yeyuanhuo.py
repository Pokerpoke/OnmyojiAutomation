# -*- encoding=utf8 -*-
__author__ = "j8245"

from airtest.core.api import *
import random

auto_setup(__file__)

# 挑战耗时，我是咸鱼，要一分半，根据需要自行调整
yeyuanhuo_duration = 105

i = 0
while (1):
    # 等待挑战按钮
    wait(Template(r"./img/challenge.png"))
    print("Start for " + str(i) + " times...")
    while (1):
        # 判断是否开始打架
        if exists(Template(r"./img/qingming.png")):
            break
        click(Template(r"./img/challenge.png"))
        sleep(2)
        # 正在打架
        if exists(Template(r"./img/qingming.png")):
            break
    # 打架
    sleep(yeyuanhuo_duration + random.randint(0, 5))
    # 等待结算的红蛋
    wait(Template(r"./img/red_egg.png"))
    sleep(2 + random.randint(0, 5))
    while(1):
        click(Template(r"./img/red_egg.png"))
        sleep(2 + random.randint(0, 5))
        # 判断点击成功没有
        if not exists(Template("./img/red_egg.png")):
            break
    print("Finish.")
    i += 1
