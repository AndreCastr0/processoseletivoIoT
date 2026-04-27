from machine import Pin, PWM, time_pulse_us
from time import sleep_ms
from time import sleep_us
import random


obs_angulo = 0
obs_distancia = 0

TOLERANCIA = 10
ALCANCE_MAX = 400

TRIG_PIN = 5 
ECHO_PIN = 18
SERVO_PIN = 4

#configurando os pinos e quardando os pinos
trig = Pin(TRIG_PIN, Pin.OUT) #pulsa o sensor do HC
echo = Pin(ECHO_PIN, Pin.IN) #retorno um valor para a distância do objeto naquela direção
servo = PWM(Pin(SERVO_PIN), freq=50) #entrada pwm do servo espera um valor para rotação
#o sinal PWM vai repetir 50 vezes pois o servo espera um pulso a cada 20ms

def mover_servo(angulo): #servo faz movimento de 180°
    duty_min = 26
    duty_max = 123
    duty = int(duty_min + (angulo / 180) * (duty_max - duty_min))
    #valor que representa 0° + valor (0-1) que representa uma parte de 180°
    
    servo.duty(duty)


def medir_distancia_cm():
    trig.value(0) #garante que trig começe baixo
    sleep_ms(2)

    trig.value(1) #inicia
    sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000) #tempo o pino ECHO ficou em nível alto (HIGH)”

    if duracao < 0:
        return None

    distancia = (duracao * 0.0343) / 2 #calculo da distância baseado na velocidade do som
    
    return distancia

def detectar_objeto(angulo, distancia):
    if distancia is None:
        return False

    dentro_do_angulo = abs(angulo - obs_angulo) <= TOLERANCIA
    dentro_do_alcance = obs_distancia <= ALCANCE_MAX

    return dentro_do_angulo and dentro_do_alcance


def classificar_distancia(distancia):
    if distancia <= 20:
        return "CRITICO"
    elif distancia <= 50:
        return "PERTO"
    elif distancia <= 100:
        return "MEDIO"
    else:
        return "LONGE"

ANGULOS = [0, 30, 60, 90, 120, 150, 180, 150, 120, 90, 60, 30, 0]

obs_angulo = random.choice(ANGULOS)
obs_distancia = random.randint(1, 400)


# 0° = esquerda
# 90° = frente
# 180° = direita

#O sonar faz uma varredura frontal
for angulo in ANGULOS:
    mover_servo(angulo) #para cada ângulo, verifique aquela direção e faça a medição de distância que o objeto está.
    sleep_ms(300) #esperar o movimento acontecer

    distancia = medir_distancia_cm() # sonar mede por padrão até cerca de 400cm

    if distancia is None:
        print("Angulo:", angulo, "| Distancia: erro")
    else:
        estado = classificar_distancia(distancia)

        if detectar_objeto(angulo, distancia):
            estado_objeto = classificar_distancia(obs_distancia)

            print(
                "Angulo:", angulo,
                "| Objeto a:", obs_distancia, "cm",
                "| Estado:", estado_objeto,
                "| OBJETO DETECTADO"
            )
        else:
            print(
                "Angulo:", angulo,
                "| Distancia:", round(distancia, 1), "cm",
                "| Estado:", estado,
                "| nada detectado"
            )


print("SIMULATION_OK")