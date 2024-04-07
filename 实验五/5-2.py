import time
import sys
from gpiozero import OutputDevice as stepper

# GPIO引脚定义部分
A_plus = stepper(5)
A_minus = stepper(12)
B_plus = stepper(6)
B_minus = stepper(13)

step_pins = [A_plus, A_minus, B_plus, B_minus]  # 创建一个包含四个GPIO引脚的列表，用于控制步进电机的步进。
step_dir = 1  # 设定步进电机的旋转方向，1代表顺时针，-1代表逆时针。

# 步进序列的定义
seq = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]

step_count = len(seq)  # 获取步进序列中的步进数量。

# 定义向前移动的函数
def move_forward(step_counter):
    for pin in range(0, 4):
        x_pin = step_pins[pin]
        if seq[step_counter][pin] != 0:
            x_pin.on()
        else:
            x_pin.off()

# 定义旋转步进电机的函数
def rotate_stepper(degrees):
    steps_per_revolution = 360 / step_count
    steps = int(degrees / steps_per_revolution)
    
    for _ in range(steps):
        for step_counter in range(step_count):
            move_forward(step_counter)
            time.sleep(0.01)  # 调整此值以控制旋转速度

# 定义旋转到指定角度并停止的函数
def rotate_to_angle(angle):
    print("Rotating to {} degrees".format(angle))
    rotate_stepper(angle)
    time.sleep(1)  # 等待一段时间以确保电机停止

# 测试函数部分
if __name__ == "__main__":
    try:
        # # 正转5圈
        # for _ in range(5):
        #     rotate_to_angle(360)
        # print("正转5次")
        
        # step_dir = -1
        # # 反转5圈
        # for _ in range(5):
        #     rotate_to_angle(360)
        # print("反转5次")

        step_dir = 1
        # 正旋转四个角度
        rotate_to_angle(45)
        # 停止
        print("Stopping motor")
        rotate_to_angle(90)
        # 停止
        print("Stopping motor")
        rotate_to_angle(180)
        # 停止
        print("Stopping motor")
        rotate_to_angle(360)  # 回到初始位置
        # 停止
        print("Stopping motor")
        

        step_dir = -1
        # 反旋转四个角度
        rotate_to_angle(45)
        # 停止
        print("Stopping motor")
        rotate_to_angle(90)
        # 停止
        print("Stopping motor")
        rotate_to_angle(180)
        # 停止
        print("Stopping motor")
        rotate_to_angle(360)  # 回到初始位置
        # 停止
        print("Stopping motor")
    except KeyboardInterrupt:
        print("Stopping motor")
