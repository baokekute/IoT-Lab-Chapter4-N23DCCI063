from machine import Pin, ADC
import time

pot = ADC(Pin(26))
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

while True:
    raw = pot.read_u16()              # 0 – 65535
    percent = raw / 65535 * 100

    if percent < 33:
        green.value(1); yellow.value(0); red.value(0)
        level = 'THẤP'
    elif percent < 66:
        green.value(1); yellow.value(1); red.value(0)
        level = 'TRUNG BÌNH'
    else:
        green.value(1); yellow.value(1); red.value(1)
        level = 'CAO'

    print(f'ADC: {raw:5d} | {percent:5.1f}% | {level}')
    time.sleep(0.5)
