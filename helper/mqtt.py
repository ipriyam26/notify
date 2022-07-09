
from paho.mqtt.client import Client
import json

class Mqtt:
    def __init__(self) -> None:
        self.client = Client()
        self.client.connect("public.mqtthq.com", 1883)
        self.client.loop_start()
        with open('config.json', 'r') as f:
            config:dict = json.load(f)
        self.topic = config['topic']
        
    def send(self,  data: str) -> None:
        self.client.publish(self.topic, data)
        self.client.loop_stop()
    


