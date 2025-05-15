# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_9_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple de polimorfisme amb sistemes de missatgeria diversos.
# -----------------------------------------------------------------------------

class Missatger:
    def enviar(self, missatge):
        pass

class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant Email: {missatge}")

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")

def enviar_missatges(missatgers, missatge):
    for m in missatgers:
        m.enviar(missatge)
