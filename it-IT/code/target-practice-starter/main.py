# Importa la libreria di codice
from p5 import *
from random import randint

# La funzione mouse_pressed va qui

# La funzione shoot_arrow va qui

def setup():
    # Set up your game here
    size(400, 400)  # larghezza e altezza dello schermo

def draw():
    # Cose da fare in ogni fotogramma
    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250) # Disegna un rettangolo per il cielo con questi valori per x, y, larghezza, altezza

# Conserva questa parte per eseguire il codice
run(frame_rate=2)
