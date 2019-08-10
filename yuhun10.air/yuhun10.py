# -*- encoding=utf8 -*-
__author__ = "j8245"

from airtest.core.api import *
import random

auto_setup(__file__)

i = 1
while(1):
    wait(Template(r"./img/challenge.png",
                  record_pos=(1.172, 0.121), resolution=(1904, 1009)))
    print("Start challenge for " + str(i) + " times.")
    touch(Template(r"./img/challenge.png",
                   record_pos=(1.172, 0.121), resolution=(1904, 1009)))
    sleep(40 + random.randint(0, 5))
    wait(Template(r"./img/red_egg.png",
                  record_pos=(1.02, 0.125), resolution=(1904, 1009)))
    sleep(2 + random.randint(0, 5))
    touch(Template(r"./img/red_egg.png",
                   record_pos=(1.02, 0.125), resolution=(1904, 1009)))
    print("Finish")
    sleep(2 + random.randint(0, 5))
    i += 1
