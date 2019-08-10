# -*- encoding=utf8 -*-
__author__ = "j8245"

from airtest.core.api import *
import random

auto_setup(__file__)

# duration
yeyuanhuo_duration = 105

i = 0
while(1):
    wait(Template(r"./img/challenge.png"))
    print("Start for " + str(i) + " times...")
    while(1):
        if exists(Template(r"./img/qingming.png")):
            break
        click(Template(r"./img/challenge.png"))
        sleep(2)
        # check if in process
        if exists(Template(r"./img/qingming.png")):
            break
    # start
    # wait for finish
    sleep(yeyuanhuo_duration + random.randint(0, 5))
    wait(Template(r"./img/red_egg.png"))
    sleep(2 + random.randint(0, 5))
    while(1):
        click(Template(r"./img/red_egg.png"))
        sleep(2 + random.randint(0, 5))
        # check if clicked
        if not exists(Template("./img/red_egg.png")):
            break
    print("Finish.")
    i += 1
