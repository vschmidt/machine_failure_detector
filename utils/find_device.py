import pyaudio

pa = pyaudio.PyAudio()

chosen_device_index = -1

for x in range(0,pa.get_device_count()):
    info = pa.get_device_info_by_index(x)
    print(pa.get_device_info_by_index(x), '\n')
