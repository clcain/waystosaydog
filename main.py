from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def dog():
    ways_to_say_dog = ['woofer', 'pupper', 'doge', 'floof', 'doggo']
    return random.choice(ways_to_say_dog)


app.run(host='0.0.0.0', port=8003)
