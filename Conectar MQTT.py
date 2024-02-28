import json
import paho.mqtt.client as mqtt
import psutil
import platform
import datetime
import uuid
import time

mqtt_broker_address = "broker.hivemq.com"
mqtt_port = 1883
mqtt_topic = "Taller MQTT"

def obtener_info_sistema():
    info_sistema = {}

    info_sistema['temperatura'] = obtener_temperatura()
    info_sistema['rendimiento_cpu'] = psutil.cpu_percent(interval=1)
    info_sistema['rendimiento_memoria'] = psutil.virtual_memory().percent
    info_sistema['rendimiento_red'] = psutil.net_io_counters().bytes_sent

    return info_sistema

def obtener_temperatura():
    try:
        temperatures = psutil.sensors_temperatures()
        if "coretemp" in temperatures:
            return temperatures["coretemp"][0].current
        elif "cpu-thermal" in temperatures:
            return temperatures["cpu-thermal"][0].current
        else:
            return "Información no disponible"
    except Exception as e:
        return "Información no disponible"

def publicar_info_periodicamente():
    client = mqtt.Client()
    client.connect(mqtt_broker_address, mqtt_port, keepalive=60)
    
    while True:
        informacion = obtener_info_sistema()
        client.publish(mqtt_topic, json.dumps(informacion))
        time.sleep(10)  # Esperar 10 segundos antes de publicar nuevamente

if __name__ == "__main__":
    publicar_info_periodicamente()