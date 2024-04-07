from gpiozero import OutputDevice
import time

# 定义直流电机的引脚
motor_forward_pin = OutputDevice(17)
motor_backward_pin = OutputDevice(18)

# 定义函数控制电机的方向和速度
def control_motor(speed):
    
    motor_forward_pin.on()
    motor_backward_pin.off()
    
    
    # 设置PWM的占空比来控制速度
    motor_forward_pin.value = abs(speed)
    motor_backward_pin.value = abs(speed)

# 测试函数部分
if __name__ == "__main__":
    try:
        
        print("Motor forward")
        control_motor(0.5)  # 50% 的速度
        time.sleep(2)
        
        print("Stop motor")
        control_motor(0)  # 停止电机
    except KeyboardInterrupt:
        print("Stopping motor")
    finally:
        motor_forward_pin.close()
        motor_backward_pin.close()
