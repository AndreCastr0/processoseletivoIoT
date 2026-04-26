from machine import Pin, PWM, time_pulse_us
from time import sleep_ms

TRIG_PIN = 5
ECHO_PIN = 18
SERVO_PIN = 4

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)
servo = PWM(Pin(SERVO_PIN), freq=50)


def mover_servo(angulo):
    duty_min = 26
    duty_max = 123
    duty = int(duty_min + (angulo / 180) * (duty_max - duty_min))
    servo.duty(duty)


def medir_distancia_cm():
    trig.value(0)
    sleep_ms(2)

    trig.value(1)
    sleep_ms(1)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)

    if duracao < 0:
        return None

    distancia = (duracao * 0.0343) / 2
    return distancia


while True:
    distancia = medir_distancia_cm()

    if distancia is None:
        print("Distancia: erro")
    else:
        print("Distancia:", round(distancia, 1), "cm")

    sleep_ms(700)