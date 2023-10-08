# pypiwin32
# pyttsx3

import pyttsx3


def voz(texto):
    sintetizador = pyttsx3.init('sapi5')

    sintetizador.say(texto)  # armazena a string
    sintetizador.runAndWait()  # execulta e espera


if __name__ == '__main__':
    voz('essa e a voz do modulo voz')
