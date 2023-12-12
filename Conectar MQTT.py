import json
import paho.mqtt.client as mqtt
import Rendimiento1
from Rendimiento1 import obtener_info_sistema

mqtt_broker_address = "broker.hivemq.com"
mqtt_port = 1883
mqtt_topic = "Taller MQTT"

informacion = obtener_info_sistema()

def on_connect(client, userdata, flags, rc):
    print(f"Conectado con el código de resultado: {rc}")
    client.subscribe(mqtt_topic)

def on_publish(client, userdata, mid):
    print(f"Mensaje publicado con éxito (ID: {mid})")

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(mqtt_broker_address, mqtt_port, keepalive=60)

client.publish(mqtt_topic, json.dumps(informacion, indent=4))

client.loop_start()
client.loop_stop()
client.disconnect()
 