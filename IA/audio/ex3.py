import numpy as np
import sounddevice as sd
import speech_recognition as speechRecog
from scipy.io.wavfile import write


def get_audio(duration=5, sr=44100):
    """Substituta local da função do Colab para gravar áudio

    diretamente do microfone do seu computador no VS Code.
    """
    print(f"🎤 Gravando por {duration} segundos... Pode falar!")

    # Grava o áudio do microfone padrão
    audio = sd.rec(
        int(duration * sr),
        samplerate=sr,
        channels=1,
        dtype="float32",  # Formato padrão ideal para processamento em ML/Librosa
    )
    sd.wait()  # Aguarda o término da gravação

    print("✅ Gravação concluída com sucesso!")

    # Achata o array para ficar em 1D (formato padrão de áudio mono)
    audio = audio.flatten()

    return audio, sr


# Normalizar o retorno do microfone e salvar num ".wav" (usando o sr dinâmico)
def mic2wav(audio, wav_file, sr=44100):
    # Evita divisão por zero caso o áudio esteja totalmente mudo
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        scaled = np.int16(audio / max_val * 32767)
    else:
        scaled = np.int16(audio)

    write(wav_file, sr, scaled)


# Transcreve o áudio
def transcreve_audio(wav_file):
    recon = speechRecog.Recognizer()
    audioFile = speechRecog.AudioFile(wav_file)

    with audioFile as source:
        audioData = recon.record(audioFile)

    try:
        texto = recon.recognize_google(audioData, language="pt-BR")
        return texto
    except speechRecog.UnknownValueError:
        return "⚠️ O Google Speech Recognition não conseguiu entender o áudio."
    except speechRecog.RequestError as e:
        return f"⚠️ Erro ao se conectar com o serviço de reconhecimento: {e}"


# --- Exemplo de como usar no seu código principal ---
if __name__ == "__main__":
    # 1. Definir taxa de amostragem padrão (44100 ou 22050)
    TAXA_AMOSTRAGEM = 44100
    NOME_ARQUIVO = "IA/audio/teste.wav"

    # 2. Gravar o áudio
    audio, sr = get_audio(duration=5, sr=TAXA_AMOSTRAGEM)

    print(f"Taxa de amostragem (sr): {sr}")
    print(f"Tamanho do array de áudio: {len(audio)}")

    # 3. Salvar em WAV
    print(f"💾 Salvando o arquivo em {NOME_ARQUIVO}...")
    mic2wav(audio, NOME_ARQUIVO, sr=sr)

    # 4. Transcrever o áudio salvo
    print("📝 Transcrevendo áudio...")
    texto_transcrito = transcreve_audio(NOME_ARQUIVO)

    print("\n--- RESULTADO DA TRANSCRIÇÃO ---")
    print(texto_transcrito)

    texto = ""
    while texto != "pare":
        audio, _ = get_audio()
        mic2wav(audio, "IA/audio/som.wav")
        texto = transcreve_audio("IA/audio/som.wav")
        print("Você disse: ", texto)
