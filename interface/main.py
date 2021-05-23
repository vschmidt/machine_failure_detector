import numpy as np
import pyaudio as pa
import struct
import matplotlib.pyplot as plt

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
DEVICE = 6
RATE = 44100  # Em Hz


p = pa.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
    input_device_index=DEVICE
)

data = stream.read(CHUNK)

# Converter os binários para inteiros
dataInt = struct.unpack(str(CHUNK) + 'h', data)

# Plotar o resultado
# fig, ax = plt.subplots()
# x = np.arange(0, 2*CHUNK, 2)
# line, = ax.plot(x, np.random.rand(CHUNK), 'r')

# fig.show()


