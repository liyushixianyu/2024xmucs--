from gpiozero import MCP3008
from time import sleep
import Adafruit_DHT,time

sensor=Adafruit_DHT.DHT11

gpio=2

def convert_temp(gen):
    for value in gen:
        yield (value*3.3-0.5)*100

adc =MCP3008(channel=0)

for temp in convert_temp(adc.values):
    print('The temperature is',temp,'℃')
    sleep(1)



while True:
    hum,tem = Adafruit_DHT.read_retry(sensor,gpio)
    if hum is not None and tem is not None:
        print('Temp={0:0.1f}*C Humi={1:0.1f}%',format(tem,hum))
    else:
        print('Faile')
    time.sleep(1)