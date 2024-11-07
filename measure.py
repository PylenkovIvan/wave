import RPi.GPIO as GPIO
from time import sleep, time


def dec_to_bin(number):
    return [int(x) for x in bin(number)[2:].zfill(8)]

arr = range(7, -1, -1)

def adc():
    global arr
    summ = 0
    for i in arr:
        summ += (2 ** i)
        GPIO.output(dac, [int(x) for x in bin(summ)[2:].zfill(8)])
        sleep(0.002)
        if GPIO.input(comp)== 1:
            summ -= (2 ** i)
    return summ


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
pin = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(pin, GPIO.IN)

try:
    data = list()
    fl = False
    t_s = time()
    while True:
        if GPIO.input(pin) == 1 and not fl:
            t_o = time()
            fl = True
        v = adc()
        if v != 0 and v:
            data.append(v)
finally:
    t_e = time()
    with open('measure_120.csv', 'w') as file:
        file.write(",".join([str(x) for x in data]) + '\n' + str(t_e - t_s) + '\n' + 
        str(t_o - t_s))
    GPIO.output(dac, 0)
    GPIO.cleanup()