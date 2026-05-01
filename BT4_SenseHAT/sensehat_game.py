from sense_emu import SenseHat
import random, time

sense = SenseHat()
sense.clear()

px, py = 3, 3
tx, ty = random.randint(0,7), random.randint(0,7)
score = 0

def draw():
    sense.clear()
    sense.set_pixel(tx, ty, [0, 255, 0])   
    sense.set_pixel(px, py, [255, 255, 255])  

draw()

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'up' and py > 0:
                py -= 1
            elif event.direction == 'down' and py < 7:
                py += 1
            elif event.direction == 'left' and px > 0:
                px -= 1
            elif event.direction == 'right' and px < 7:
                px += 1
            elif event.direction == 'middle':
                sense.show_message(str(score), text_colour=[255,255,0])

            if px == tx and py == ty:
                score += 1
                print(f'Ghi bàn! Điểm: {score}')
                sense.clear([255, 255, 0])
                time.sleep(0.3)
                tx, ty = random.randint(0, 7), random.randint(0, 7)

            draw()
    time.sleep(0.05)
