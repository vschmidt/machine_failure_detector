import numpy as np
import pyaudio as pa
import struct
import matplotlib.pyplot as plt

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100  # Em Hz

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
fig, (ax1, ax2) = plt.subplots(2)

x = np.arange(0, 2*CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

line, = ax1.plot(x, np.random.rand(CHUNK), 'r')
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK))

ax1.set_ylim(-60000, 60000)
ax1.set_xlim(0, CHUNK)

ax2.set_ylim(0, 0.4)
ax2.set_xlim(20, RATE/2)

fig.show()

# Loop de leitura
while True:
    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    
    line.set_ydata(dataInt)
    line_fft.set_ydata(np.abs(np.fft.fft(dataInt))*2/(33000*CHUNK))

    fig.canvas.draw()
    fig.canvas.flush_events()