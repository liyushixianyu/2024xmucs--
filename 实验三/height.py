from gpiozero import DistanceSensor,LED,LineSensor
#from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from signal import pause

#factory = PiGPIOFactory()
sensor = DistanceSensor(echo=23,trigger=24,threshold_distance=0.08)
led =LED(3)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off



while True:
    print('距离液面：',sensor.distance*100,'cm\n')
    print('液面高度=%f cm\n'%((0.155-sensor.distance)*100))
    sleep(5)
    #pause()