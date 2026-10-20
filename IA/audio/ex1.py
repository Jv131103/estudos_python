import librosa
# Plotar o áudio no aspectro do tempo
import matplotlib.pyplot as plt
import numpy as np
import pygame

# Carregar o arquivo
AUDIO_FILE = "IA/audio/audio_file.wav"

samples, sample_rate = librosa.load(AUDIO_FILE, sr=None)  # SR: sample rate

print(sample_rate)

plt.figure(figsize=(14, 5))
librosa.display.waveshow(samples, sr=sample_rate)
plt.show()

# (Opcional) Tocar o áudio via script .py:
# Inicializar o mixer do Pygame
pygame.mixer.init()

# Carregar o arquivo de áudio
pygame.mixer.music.load(AUDIO_FILE)

print("Reproduzindo áudio...")
pygame.mixer.music.play()

rodando = True
is_paused = False

# Exemplo de controle interativo simples via terminal:
# (Você pode adaptar para criar botões se estiver usando uma interface gráfica)
try:
    while rodando:
        comando = (
            input("Comandos -> [p]ausar | [r]etomar | [s]air: ").strip().lower()
        )

        if comando == "p":
            if not is_paused:
                pygame.mixer.music.pause()
                is_paused = True
                print("-> Áudio pausado.")
            else:
                print("-> O áudio já está pausado.")

        elif comando == "r":
            if is_paused:
                pygame.mixer.music.unpause()
                is_paused = False
                print("-> Áudio retomado.")
            else:
                print("-> O áudio não está pausado.")

        elif comando == "s":
            pygame.mixer.music.stop()
            rodando = False
            print("-> Reprodução encerrada.")

        else:
            print("-> Comando inválido. Use 'p', 'r' ou 's'.")

        # Opcional: se o áudio acabou de tocar até o fim naturalmente (e não estava pausado)
        if not pygame.mixer.music.get_busy() and not is_paused and rodando:
            print("-> Fim do arquivo de áudio.")
            rodando = False
except KeyboardInterrupt:
    # Permite interromper com Ctrl+C de forma limpa
    pygame.mixer.music.stop()
    print("\nReprodução interrompida.")

# Extrair o espectrograma
sgram = librosa.stft(samples)
librosa.display.specshow(sgram)
plt.show()

# Valorizar o espectro percebido pelo humano
# 1. Calcular a Transformada de Fourier de Curta Duração (STFT) e a magnitude
stft_result = librosa.stft(samples)
sgram_mag, _ = librosa.magphase(stft_result)

# 2. Gerar o Mel-Spectrograma
mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)

# 3. Converter para a escala de Decibéis (Essencial para visualização humana)
mel_sgram_db = librosa.power_to_db(mel_scale_sgram, ref=np.max)

# 4. Plotar o Mel-Spectrograma formatado profissionalmente
plt.figure(figsize=(12, 5))
librosa.display.specshow(
    mel_sgram_db,
    sr=sample_rate,
    x_axis="time",  # Mostra o tempo em segundos no eixo X
    y_axis="mel",  # Mostra a escala Mel no eixo Y
    cmap="magma",  # Mapa de cores visualmente rico (pode usar 'viridis', 'coolwarm', etc.)
)

plt.colorbar(
    format="%+2.0f dB"
)  # Adiciona a legenda de intensidade em decibéis
plt.title("Mel-Spectrograma (Percepção Humana)")
plt.tight_layout()
plt.show()
