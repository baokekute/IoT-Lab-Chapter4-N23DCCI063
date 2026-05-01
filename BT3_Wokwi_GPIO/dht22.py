from machine import Pin
import dht
import time

sensor = dht.DHT22(Pin(16))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        t = time.localtime()
        ts = f'{t[3]:02d}:{t[4]:02d}:{t[5]:02d}'
        print(f'[{ts}] Temp: {temp:.1f}°C | Humidity: {hum:.1f}%')
    except Exception as e:
        print(f'Lỗi: {e}')
    time.sleep(2)
