from gpiozero import TrafficLights,Button
from time import sleep

lights = TrafficLights(2, 3, 4)

#lights.green.on()
button = Button(12,pull_up=False)
def breath():
    # while True:
        sleep(1)
        lights.green.off()
        lights.amber.on()
        sleep(1)
        lights.amber.off()
        lights.red.on()
        sleep(1)
        lights.red.off()
        lights.green.on()
        # sleep(1)
        # lights.green.off()
        # lights.amber.on()
def stop():
    lights.green.off()
    lights.amber.off()
    lights.red.off()
# button.when_pressed = breath
# button.when_released = stop

# 定义按键事件处理函数
def button_pressed() :
     print("button is pressed")
     global running
     if running :
          running = False 
          print("关灯")
          
     else :
          running = True
          print("开灯")
          

running = True
flag = True
while True:
    if flag :
        print("默认开灯")
        breath()
        flag = False
    if running :
         print("主函数：breath")
         breath()
    else :
         print("主函数：stop")
         stop()
    button.when_activated = button_pressed


         