import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os

os.environ["PATH"] += os.pathsep + r"C:\Users\ro_19\Downloads\ffmpeg\ffmpeg\bin"

def gravar_audio(nome_do_arquivo='audio.wav',duracao= 5,  fs=44100):
    print('Gravando audio...')
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()
    write(nome_do_arquivo, fs,audio)
    print('Audio gravado com sucesso!!!')
    return nome_do_arquivo

def transcrever_audio(nome_do_arquivo):
    print("🧠 Transcrevendo...")
    modelo = whisper.load_model("base")  # pode trocar para "tiny"
    resultado = modelo.transcribe(nome_do_arquivo)
    texto = resultado["text"]
    print(f"📄 Você disse: {texto}")
    return texto