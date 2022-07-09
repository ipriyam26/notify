import random
from time import time

#generate a random patter of alphanumeric characters of 16 characters
def generate_topic()->str:
    random.seed = time()
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(16))

topic = generate_topic()
import json
config = {
    "topic": topic,
}
with open('config.json', 'w') as f:
    json.dump(config, f)