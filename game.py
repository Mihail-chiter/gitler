from pygame import *
init()

screen = display.set_mode((800, 600))
bg = image.load('images/bg.jpg')
player = image.load('images/player.jpg')
x = 0
y = 0
while True:
    screen.blit(bg, (0, 0))
    screen.blit(player, (x, y))

    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        QUIT()
    elif keys[K_d]:
        x += 0.3
    elif keys[K_a]:
        x -= 0.3
    elif keys[K_w]:
        y -= 0.4
    elif keys[K_s]:
        y += 0.4

    display.update()

    for even in event.get():
        if even.type == QUIT:
            QUIT()
