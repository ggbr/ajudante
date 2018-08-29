import pyttsx3


def fala(texto):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'brazil')
    engine.say(str(texto))
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + -50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume - 1.50)
    engine.runAndWait()



def main():
    print(1)

    fala("Ola Gabriel")