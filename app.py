from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import threading
import time

app = Flask(__name__)

PULSE_PIN = 17
PULSE_LENGTH_CM = 30.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(PULSE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pulse_count = 0
measuring = False

def pulse_callback(channel):
    global pulse_count
    if measuring:
        pulse_count += 1

GPIO.add_event_detect(PULSE_PIN, GPIO.FALLING, callback=pulse_callback, bouncetime=10)

def calibrar():
    global pulse_count, measuring
    pulse_count = 0
    measuring = True
    time.sleep(60)
    measuring = False
    distance_m = pulse_count * (PULSE_LENGTH_CM / 100)
    speed_mps = distance_m / 60
    return round(distance_m, 2), round(speed_mps, 2), round(distance_m * 2, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calibrar', methods=['POST'])
def handle_calibrar():
    distance, speed, valor = calibrar()
    return jsonify({
        'distancia': f'{distance:.2f} m',
        'velocidade': f'{speed:.2f} m/s',
        'valor': f'R$ {valor:.2f}'
    })

@app.route('/zerar', methods=['POST'])
def handle_zerar():
    global pulse_count
    pulse_count = 0
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
