from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self): pass

class Player:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0,7)
        self.x,self.y = random.randint(100,700),90
        self.dir = 0
        self.idle = True
    def draw(self):
        if self.idle:
            self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        else:
            self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += (self.dir * 5)

class Ball:
    def __init__(self):
        self.is_small = random.randint(0,1)
        if self.is_small:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.x,self.y = random.randint(100,700),599
        self.speed = random.randint(1,10)
        self.dir = -1
    def update(self):
        self.y += self.speed * self.dir

        if self.is_small:
            if self.y <= (90 - 25):
                self.speed = 0
        else:
            if self.y <= (90 - 35):
                self.speed = 0
    def draw(self):
        if self.is_small:
            self.image.draw(self.x,self.y,20,20)
        else:
            self.image.draw(self.x,self.y,40,40)


# func
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                player.dir -= 1
                player.idle = False
            elif event.key == SDLK_RIGHT:
                player.dir += 1
                player.idle = False
            elif event.key == SDLK_UP:
                pass
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                player.idle = True
                player.dir += 1
            elif event.key == SDLK_RIGHT:
                player.idle = True
                player.dir -= 1
            elif event.key == SDLK_UP:
                pass

def reset_world():
    global running
    global grass
    global player
    global team
    global world
    global balls

    running = True
    world = []

    grass = Grass() # 잔디 생성
    world.append(grass)

    balls = [Ball() for i in range(20)]
    world += balls

    player = Player() # 플레이어 생성
    world.append(player)

    team = [Player() for i in range(11)]
    world += team

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


# initialization code
open_canvas()
reset_world()

# game main loop code
while running:
    #game logic
    handle_events()
    update_world() #상호작용 시뮬레이션
    render_world() #그 결과를 보여준다(Drawing)
    delay(0.05)

# finalization code
close_canvas()
