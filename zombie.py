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
        # 왼편까지 포함해서 생성하니까 시작하자마자 게임 오버되는 현상 발생
        self.x, self.y = random.randint(800, 1600), 150
        self.frame = random.randint(0, 9)
        self.dir = random.choice([-1,1])
        self.hit_count = 0  # 공에 맞은 횟수
        self.size = 200  # 초기 크기
        self.images = [load_image("./zombie/Walk (%d).png" % i) for i in range(1, 11)]
    
    def get_bb(self):
        size_ratio = self.size / 200.0  # 원래 크기 대비 비율
        return self.x - 100 * size_ratio, self.y - 100 * size_ratio, self.x + 100 * size_ratio, self.y + 100 * size_ratio

    def handle_collision(self, group, other):
        if group == 'ball:zombie':
            # 땅에 떨어진 볼과는 충돌하지 않음
            if not other.stopped:
                self.hit_count += 1
                if self.hit_count == 1:
                    # 첫번째 히트: 크기를 반으로 줄임
                    self.size = 100
                elif self.hit_count >= 2:
                    # 두번째 히트: 좀비 제거
                    game_world.remove_object(self)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        self.x = clamp(800, self.x, 1600)


    def handle_event(self, event):
        pass

    def draw(self):
        if self.dir < 0:
            self.images[int(self.frame)].composite_draw(0, 'h', self.x, self.y, self.size, self.size)
        else:
            self.images[int(self.frame)].draw(self.x, self.y, self.size, self.size)
        draw_rectangle(*self.get_bb())

