# SmartGauge

**Integrantes do Grupo:**
- Ana Silva
- Bruno Oliveira
- Carla Mendes
- Diego Souza

**Instituição:**
Universidade Federal de Tecnologia Aplicada

## Descrição
O projeto **SmartGauge** é um sistema embarcado utilizando Raspberry Pi para medir a velocidade, distância percorrida e calcular um valor com base em pulsos digitais recebidos. A cada pulso lido de um sensor digital, considera-se 30 cm percorridos. A medição é realizada durante 1 minuto ao pressionar o botão "Calibrar" na interface web.

## Requisitos
- Raspberry Pi com acesso à internet e GPIO ativo
- Python 3
- Biblioteca Flask
- Sensor digital conectado ao GPIO 17

## Instalação
1. Clone o repositório ou copie os arquivos para uma pasta no Raspberry Pi.
2. Instale o Flask:
   ```bash
   pip install flask
   ```
3. Certifique-se de que a imagem `medidor.png` esteja na pasta `static/`.

## Estrutura de Pastas
```
smartgauge/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── medidor.png
└── README.md
```

## Executando o Projeto
1. No terminal, navegue até a pasta `smartgauge`:
   ```bash
   cd smartgauge
   ```
2. Execute o servidor Flask:
   ```bash
   python app.py
   ```
3. Acesse a interface web no navegador pelo IP do Raspberry Pi, porta 5000:
   ```
   http://<IP_DO_RASPBERRY>:5000
   ```

## Funcionalidades
- Botão **Calibrar** inicia a contagem de pulsos por 60 segundos.
- Cálculo automático de:
  - Velocidade (m/s)
  - Distância (m)
  - Valor cobrado (baseado na distância)
- Botão **Zerar Sistema** limpa os valores exibidos.

## Observação
- Cada pulso representa 30 cm percorridos.
- Certifique-se de que o sensor digital esteja funcionando corretamente e ligado ao pino GPIO 17 (BCM).

---
Desenvolvido como parte do projeto de sistemas embarcados.
