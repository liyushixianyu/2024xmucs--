from gpiozero import DistanceSensor,LineSensor
from time import sleep
from signal import pause
import time 
import sys
from datetime import datetime



# T1 = time.time()

sensor = LineSensor(4)
list = []

# list = [0,0]
def jstime():
    global cnt

    current_time = time.time()
    list.append(current_time)

    list[cnt] = current_time
    cnt = cnt + 1
    print('jstime')
    print(cnt)

    if cnt % 2 == 0:
        print("转速 %f round/s " % (1/(list[cnt - 1]-list[cnt - 2])) )
        #sys.exit() # 退出当前程序，但不重启shell


cnt = 0
sensor.when_line = jstime
# sensor.when_no_line = lambda:print('No line detected')
# 
# print('程序运行时间:%s秒' % ((T2 - T1)*1000000))
pause()
