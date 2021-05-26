import os
from datetime import datetime
import pyaudio as pa
import wave

FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # Em Hz
CHUNK = 1024 * 2
RECORD_SECONDS = 10
BASE_PATH = os.path.dirname(os.path.realpath(__file__)) # Pasta base

OUTPUT_FOLDER_PATH = BASE_PATH + '/Saídas/1 - Som ambiente/' # Pasta onde serão armazenados os aúdios
TEST_TYPE = OUTPUT_FOLDER_PATH + '/0 - Regime Normal/' # Tipo de teste que será executado
WAVE_OUTPUT_FILENAME = TEST_TYPE + str(datetime.now()) + '.wav' # Nome do arquivo

# Criar uma instância do PyAudio
audio = pa.PyAudio()

stream = audio.open(format=FORMAT, 
                    channels=CHANNELS,
                    rate=RATE, 
                    input=True,
                    frames_per_buffer=CHUNK)

# Iniciando a gravação
input(f'Pressione enter para iniciar a gravação de {RECORD_SECONDS} segundos')
print("Gravando...")

Recordframes = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    Recordframes.append(data)

# Salvar o arquivo gravado
print("Fim da gravação, salvando arquivo...")

stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(Recordframes))
waveFile.close()