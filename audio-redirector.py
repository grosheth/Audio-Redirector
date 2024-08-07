"""PyAudio Example: Record a few seconds of audio and save to a wave file."""
import pyaudio
import numpy as np
from matplotlib import pyplot as plt

CHUNKSIZE = 1024 # fixed chunk size

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNKSIZE)

# do this as long as you want fresh samples
data = stream.read(CHUNKSIZE)
numpydata = np.frombuffer(data, dtype=np.int16)

# plot data
plt.plot(numpydata)
plt.show()

# close stream
stream.stop_stream()
stream.close()
p.terminate()

# def generate_sample(ob, preview):
#     print("* Generating sample...")
#     tone_out = array(ob, dtype=int16)
#
#     if preview:
#         print("* Previewing audio file...")
#
#         bytestream = tone_out.tobytes()
#         pya = pyaudio.PyAudio()
#         stream = pya.open(format=pya.get_format_from_width(width=2), channels=1, rate=OUTPUT_SAMPLE_RATE, output=True)
#         stream.write(bytestream)
#         stream.stop_stream()
#         stream.close()
#
#         pya.terminate()
#         print("* Preview completed!")
#     else:
#         write('sound.wav', SAMPLE_RATE, tone_out)
#         print("* Wrote audio file!")
#
# generate_sample()
