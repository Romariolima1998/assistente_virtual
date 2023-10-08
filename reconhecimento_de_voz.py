import speech_recognition as sr
from speech_recognition import exceptions
from sintetizador_de_voz import voz


def microfone(idioma) -> any:
    # abilitar microfone
    microfone = sr.Recognizer()

    # usar microfone
    with sr.Microphone() as source:
        # reduçao de ruidos
        microfone.adjust_for_ambient_noise(source)

        print('ouvindo')

        audio = microfone.listen(source)

    if idioma == 'pt-br':
        try:
            frase: str | None | any = microfone.recognize_google(
                audio, language=idioma)

        except exceptions.UnknownValueError:
            frase = None

        except exceptions.RequestError:
            voz('falha na conexão com a internet')
            frase = None
        except exceptions.SetupError or exceptions.TranscriptionFailed or\
                exceptions.TranscriptionNotReady or exceptions.WaitTimeoutError:
            voz('ocorreu um erro')
            frase = None
        return frase
    elif idioma == 'en-US':
        try:
            frase = microfone.recognize_google(audio, language=idioma)

        except exceptions.UnknownValueError:
            frase = None

        except exceptions.RequestError:
            voz('falha na conexão com a internet')
            frase = None
        except exceptions.SetupError or exceptions.TranscriptionFailed or exceptions.TranscriptionNotReady or exceptions.WaitTimeoutError:
            voz('ocorreu um erro')
            frase = None
        return frase
