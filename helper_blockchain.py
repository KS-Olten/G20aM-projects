# Dieses Skript definiert die Helfer-Klasse. Sie enthält sämtliche Logik, welche nicht in das Streamlit Skript gehört.

from random import randint # Importiere randint um zufällige Zahlen zu erstellen

class Helper:

    def __init__(self, my_max):
        # Beim erstellen der Helferklasse muss ein Parameter my_max mitgegeben werden.
        # Der Parameter bestimmt das Maximum der Zufallszahlen, welche die Klasse generieren kann.
        self.my_max = my_max

    def magic_numer(self):
        # Diese Methode liefert eine Zufallszahl (Integer) zwischen 0 und my_max zurück
        new_magic_number = randint(0, self.my_max)
        return new_magic_number
