from machine import Pin, PWM, time_pulse_us
from time import sleep_ms
from time import sleep_us
import random
from neopixel import NeoPixel

#PARA SELECIONAR POSIÇÃO O OBSTACULO MODIFIQUE SOS VALORES ABAIXO OU DESCOMENTE
# O MODO ALEATÓRIO NA LINHA 172 e 173

obs_angulo = 0
obs_distancia = 87



#EXIBIÇÃO DO MAPA

# linha 0 = crítico, linha 1 = perto, linha 2 = médio, linha 3 = longe

LINHAS = 4

# 0°, 30°, 60°, 90°, 120°, 150° e 180°

COLUNAS = 7

NUM_LEDS = LINHAS * COLUNAS
MATRIX_PIN = 14
matrix = NeoPixel(Pin(MATRIX_PIN), NUM_LEDS)


def limpar_matriz(): 
    for i in range(NUM_LEDS): #percorre todos os LEDs
        matrix[i] = (0, 0, 0)
    matrix.write()


def coordenada_para_indice(x, y):
    # Converte uma posição da matriz, dada por coluna x e linha y,
    # para o índice linear

    return y * COLUNAS + x 


def angulo_para_coluna(angulo):
    # Converte o ângulo da varredura para uma coluna da matriz.

    # Como os ângulos variam de 30 em 30 graus:
    # 0°   -> coluna 0
    # 30°  -> coluna 1
    # 60°  -> coluna 2
    # 90°  -> coluna 3
    # 120° -> coluna 4
    # 150° -> coluna 5
    # 180° -> coluna 6

    return angulo // 30


def distancia_para_linha(distancia):
    if distancia <= 20:
        return 0  # crítico
    elif distancia <= 50:
        return 1  # perto
    elif distancia <= 100:
        return 2  # médio
    else:
        return 3  # longe


def cor_por_estado(distancia):
    if distancia <= 20:
        return (255, 0, 0)      # vermelho
    elif distancia <= 50:
        return (255, 80, 0)     # laranja/amarelo
    elif distancia <= 100:
        return (255, 255, 0)    # amarelo
    else:
        return (0, 255, 0)      # verde


def mostrar_objeto_na_matriz(angulo, distancia):
    limpar_matriz()

    # Descobre em qual coluna o objeto deve aparecer, com base no ângulo
    
    coluna = angulo_para_coluna(angulo)

    # Descobre em qual linha o objeto deve aparecer, com base na distância
    
    linha = distancia_para_linha(distancia)
    
    # Escolhe a cor do LED com base na distância

    cor = cor_por_estado(distancia)

    indice = coordenada_para_indice(coluna, linha)
    
    # Acende o LED correspondente à posição do objeto no "mapa"
    
    matrix[indice] = cor

    matrix.write() #Ele envia os dados para os LEDs


    

#CRIAÇÃO E PROCESSAMENTO DOS DADOS

TOLERANCIA = 10
ALCANCE_MAX = 400

TRIG_PIN = 5 
ECHO_PIN = 18
SERVO_PIN = 4


trig = Pin(TRIG_PIN, Pin.OUT) #pulsa o sensor do HC
echo = Pin(ECHO_PIN, Pin.IN) #retorno um valor para a distância do objeto naquela direção
servo = PWM(Pin(SERVO_PIN), freq=50) #entrada pwm do servo espera um valor para rotação

#o sinal PWM vai repetir 50 vezes pois o servo espera um pulso a cada 20ms

#contempla 180° frontais
def mover_servo(angulo): 
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

#obs_angulo = random.choice(ANGULOS) #gerando uma posição aleatória para o obstáculo
#obs_distancia = random.randint(1, 400)



# 0° = esquerda
# 90° = frente
# 180° = direita


#O sonar faz uma varredura frontal

def executar_varredura():

    for angulo in ANGULOS:
        mover_servo(angulo) #para cada ângulo, verifique aquela direção e faça a medição de distância que o objeto está.
        sleep_ms(300) #esperar o movimento acontecer

        distancia = medir_distancia_cm() # sonar mede por padrão até cerca de 400cm

        if distancia is None:
            limpar_matriz()
            print("Angulo:", angulo, "| Distancia: erro")
        else:
            estado = classificar_distancia(distancia)

            if detectar_objeto(angulo, distancia):
                estado_objeto = classificar_distancia(obs_distancia)

                mostrar_objeto_na_matriz(angulo, obs_distancia)

                print(
                    "Angulo:", angulo,
                    "| Objeto a:", obs_distancia, "cm",
                    "| Estado:", estado_objeto,
                    "| OBJETO DETECTADO"
                )
            else:
                limpar_matriz()
                print(
                    "Angulo:", angulo,
                    "| Distancia:", round(distancia, 1), "cm",
                    "| Estado:", estado,
                    "| nada detectado"
                )

executar_varredura()

print("SIMULATION_OK")