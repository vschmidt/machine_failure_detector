import numpy as np
import os
import pickle as pkl
import pyaudio as pa
import struct
import matplotlib.pyplot as plt

from sklearn.svm import NuSVC

# Parâmetros
CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100  # Em Hz

# Carregar o modelo gerado
path = 'Análise dos dados/Preditores/'
file_name = 'classificador_som_indústrial.pkl'

print(os.path.isfile(path + file_name))

with open(path + file_name, 'rb') as file:
    clf = pkl.load(file)

# Funções auxiliares
def apply_fft(dataInt, CHUNK):
    """ Esta função retorna um array com a FFT"""    
    fft_value = np.fft.fft(dataInt)
    absolute_value = np.abs(fft_value)
    audio_freq_convert = absolute_value *2 / (33000*CHUNK) 
    return audio_freq_convert

# Configurações do gravador
p = pa.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

data = stream.read(CHUNK)

# Converter os binários para inteiros
dataInt = struct.unpack(str(CHUNK) + 'h', data)

# Configurações da figura
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.canvas.manager.set_window_title('Monitorador de equipamento')

x = np.arange(0, 2*CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

line, = ax1.plot(x, np.random.rand(CHUNK), 'r')
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK))

ax1.set_title("Amplitude")
ax2.set_title("Espectograma")
fig.tight_layout()

ax1.set_ylim(-60000, 60000)
ax1.set_xlim(0, CHUNK)

ax2.set_ylim(0, 0.4)
ax2.set_xlim(20, RATE/2)

ax3.text(0.5, 0.5, "CLASSE", size=25,
            ha='center', va='center',
            bbox=dict(boxstyle="square",
                    ec=(1., 0.5, 0.5),
                    fc=(1., 0.8, 0.8),
            )
)

ax3.axis('off')

fig.show()

# Loop de leitura
while True:
    data = stream.read(CHUNK) # Leitura do dados
    dataInt = struct.unpack(str(CHUNK) + 'h', data) # Conversão de binários para inteiros
    dataFFT = apply_fft(dataInt, CHUNK) # Aplicação da FFT

    # Predição da saída
    predict = clf.predict([dataFFT])

    # Encontrar a saída predita
    if(predict[0] == 0):
        ax3.texts[0].set_text('REGIME NORMAL')
    elif(predict[0] == 1):
        ax3.texts[0].set_text('FALTA DE TENSÃO')
    elif(predict[0] == 2):
        ax3.texts[0].set_text('SOBRECARGA')
    else:
        ax3.texts[0].set_text('EIXO DESBALANCEADO')
        
    # Exposição dos dados
    line.set_ydata(dataInt)
    line_fft.set_ydata(np.abs(np.fft.fft(dataInt))*2/(33000*CHUNK))

    fig.canvas.draw()
    fig.canvas.flush_events()