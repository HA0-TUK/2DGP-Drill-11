
world = [[] for _ in range(4)]
collision_pairs = {}

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def add_object(o, depth = 0):
    world[depth].append(o)

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0][:]:
            for b in pairs[1][:]:
                # 객체가 아직 world에 존재하는지 확인 (이미 삭제되지 않았는지)
                a_exists = any(a in layer for layer in world)
                b_exists = any(b in layer for layer in world)
                if a_exists and b_exists and collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

def add_objects(ol, depth = 0):
    world[depth] += ol

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            return
    raise ValueError('Cannot delete non existing object')

def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def clear():
    global world

    for layer in world:
        layer.clear()




