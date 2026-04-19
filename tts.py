from gtts import gTTS
import os

def falar(texto):
    print("🔊 Respondendo...")
    tts = gTTS(text=texto, lang="pt-br")
    tts.save("resposta.mp3")

    # Windows
    os.system("start resposta.mp3")