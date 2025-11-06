from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass
    def get_bb(self):
        return 0, 0, 1600-1, 50

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
    
    def handle_collision(self, group, other):
        pass
