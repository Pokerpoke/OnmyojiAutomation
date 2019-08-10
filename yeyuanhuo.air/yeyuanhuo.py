# -*- encoding=utf8 -*-
__author__ = "j8245"

from airtest.core.api import *
import random

auto_setup(__file__)

i = 1

yeyuanhuo_duration = 90 + 15

while(1):
    wait(Template(r"./img/challenge.png",
                  record_pos=(1.226, 0.153), resolution=(1904, 1009)))
    print("Start for " + str(i) + " times...")
    sleep(1)
    touch(Template(r"./img/challenge.png",
                   record_pos=(1.226, 0.153), resolution=(1904, 1009)))
    sleep(yeyuanhuo_duration + random.randint(0, 5))
    wait(Template(r"./img/red_egg.png",
                  record_pos=(1.141, 0.174), resolution=(1904, 1009)))
    sleep(2 + random.randint(0, 5))
    while(1):
        touch(Template(r"./img/red_egg.png",
                       record_pos=(1.141, 0.174), resolution=(1904, 1009)))
        sleep(2 + random.randint(0, 5))
        if not exists(Template("./img/red_egg.png", record_pos=(1.141, 0.174), resolution=(1904, 1009))):
            break
    print("Finish.")
    i += 1
