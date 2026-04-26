from machine import Pin, PWM
from time import sleep_ms

SERVO_PIN = 4

servo = PWM(Pin(SERVO_PIN), freq=50)


def mover_servo(angulo):
    duty_min = 26
    duty_max = 123
    duty = int(duty_min + (angulo / 180) * (duty_max - duty_min))
    servo.duty(duty)


while True:
    for angulo in [0, 45, 90, 135, 180]:
        mover_servo(angulo)
        print("Servo no angulo:", angulo)
        sleep_ms(700)

    for angulo in [135, 90, 45]:
        mover_servo(angulo)
        print("Servo no angulo:", angulo)
        sleep_ms(700)