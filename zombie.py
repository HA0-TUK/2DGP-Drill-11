import random
import math
import game_framework
import game_world

from pico2d import *

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0


class Zombie:
    def __init__(self):
        pass
    def get_bb(self):
        pass
    def handle_collision(self, group, other):
            pass
            # 땅에 떨어진 볼과는 충돌하지 않음

            # 첫번째 히트: 크기를 반으로 줄임

            # 두번째 히트: 좀비 제거


    def update(self):
         pass


    def handle_event(self, event):
        pass

    def draw(self):
         pass
