# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

---

### 👤 Identificação do Candidato

- **Nome completo:André Castro Saraiva Leite**  
- **GitHub: AndreCastr0 link: https://github.com/AndreCastr0**  

---

## 1️⃣ Visão Geral da Solução

Este projeto tem como objetivo implementar um sistema embarcado que simula o funcionamento de um sonar, utilizando um microcontrolador ESP32, sensor ultrassônico, servomotor e uma matriz de LEDs NeoPixel.

O sistema realiza uma varredura angular de 180°, detecta um obstáculo e exibe sua posição de forma simplificada por meio de uma matriz de LEDs, além de imprimir no terminal sua distância e nível de criticidade.

Devido às limitações do ambiente de simulação (Wokwi), não é possível detectar obstáculos físicos reais. Por isso, a posição do obstáculo é definida diretamente no código. O usuário pode ajustar manualmente essa posição ou habilitar a geração aleatória.

---

## 2️⃣ Arquitetura do Sistema Embarcado

A arquitetura do sistema foi organizada em três blocos principais: aquisição de dados, processamento lógico e exibição do resultado.

**Aquisição de dados**  
O ESP32 controla o servomotor por meio de sinal PWM, posicionando o sensor ultrassônico em diferentes ângulos da varredura frontal. A varredura ocorre em intervalos de 30°, cobrindo as posições 0°, 30°, 60°, 90°, 120°, 150° e 180°. Em cada posição, o sensor HC-SR04 realiza a medição de distância.

**Processamento lógico**  
O sistema verifica se o ângulo atual corresponde à posição do obstáculo definido e se a distância está dentro do alcance máximo. Quando essas condições são atendidas, a distância é classificada em um dos níveis: CRÍTICO, PERTO, MÉDIO ou LONGE.

**Exibição do resultado**  
Os resultados são apresentados de duas formas:
- No terminal: exibindo ângulo, distância e estado
- Na matriz NeoPixel (4x7): representando o mapa do sonar

Na matriz:
- Colunas representam os ângulos
- Linhas representam a distância

As cores indicam o nível de proximidade:
- Vermelho → crítico  
- Laranja → perto  
- Amarelo → médio  
- Verde → longe  

**Temporização**  
A temporização é feita com `sleep_us(10)` para disparo do sensor e `sleep_ms(300)` para permitir a estabilização do servomotor antes da leitura.

---

## 3️⃣ Componentes Utilizados na Simulação

- **ESP32**: responsável pelo controle geral do sistema  
- **Sensor HC-SR04**: realiza medições de distância (simuladas)  
- **Servomotor**: executa a varredura angular  
- **Matriz NeoPixel (4x7)**: exibe o mapa do ambiente  

## 4️⃣ Decisões Técnicas Relevantes

**Organização do código**  
O código foi dividido em funções para separar responsabilidades, como movimentar o servo, medir distância e exibir o resultado. Isso melhora a legibilidade e manutenção.

**Uso de funções e constantes**  
Funções foram utilizadas para evitar repetição de código, enquanto constantes foram usadas para definir pinos, ângulos e limites, facilitando ajustes futuros.

**Temporização e controle lógico**  
Foram usados `sleep_ms()` e `sleep_us()` para garantir o funcionamento correto do sensor e do servo.  
O sistema executa apenas uma varredura (sem loop infinito), permitindo compatibilidade com o GitHub Actions e finalizando com `SIMULATION_OK`.

---

## 5️⃣ Resultados Obtidos

O sistema apresenta os seguintes resultados:

- Varredura correta de 180°
- Movimentação adequada do servomotor
- Leitura de distância simulada
- Classificação correta dos níveis de proximidade
- Exibição no terminal funcionando corretamente
- Representação visual do objeto na matriz de LEDs

Na simulação do Wokwi:
- O sistema executa sem erros
- O mapa é exibido corretamente
- O comportamento é consistente com a lógica implementada

---
## 6️⃣ Comentários Adicionais

**Dificuldades**  
Foram encontrados pequenos desafios na configuração do ambiente e na integração com o GitHub Actions.

**Limitações do protótipo**  
O Wokwi não simula obstáculos físicos reais. Assim, a detecção do objeto é feita por comparação lógica entre o ângulo atual e a posição definida no código. Em um sistema real, o sensor detectaria diretamente o obstáculo.

**Possíveis melhorias**
- Aumentar a quantidade de ângulos para maior precisão  
- Expandir o tamanho da matriz  
- Utilizar display OLED para um radar gráfico  
- Implementar varredura 360°  
- Melhorar a temporização (evitar delays bloqueantes)  

**Principais aprendizados**
- Desenvolvimento de sistemas embarcados  
- Integração de sensores e atuadores  
- Uso do Wokwi para simulação  
- Automação com GitHub Actions  
- Organização e versionamento de código  

---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
