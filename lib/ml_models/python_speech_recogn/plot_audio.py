'''import wave
import matplotlib.pyplot as plt

import numpy as np

obj = wave.open("hello.wav", "rb")
sample_freq = obj.getframerate() 
n_samples =  obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()

t_audio = n_samples / sample_freq
print(t_audio)

# Convert the byte data to a NumPy array
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, num = n_samples)

plt.figure(figsize= (15,5))
plt.plot(times, signal_array)
plt.title("audio signal")
plt.ylabel("signal wave")
plt.xlabel("time in sec")
plt.xlim(0, t_audio)
plt.show()
'''

import wave
import matplotlib.pyplot as plt
import numpy as np

# Open the wave file
obj = wave.open("hello.wav", "rb")

# Extract sample frequency and number of frames
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
n_channels = obj.getnchannels()  # Get number of channels

# Read the signal wave data
signal_wave = obj.readframes(-1)
obj.close()

# Calculate the duration of the audio
t_audio = n_samples / sample_freq
print("Audio duration in seconds:", t_audio)

# Convert the byte data to a NumPy array
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# If stereo (2 channels), average the two channels
if n_channels == 2:
    signal_array = signal_array.reshape(-1, 2)  # Reshape to separate channels
    signal_array = signal_array.mean(axis=1)  # Average the channels

# Create an array of time values for the x-axis
times = np.linspace(0, t_audio, num=len(signal_array))

# Plot the audio signal
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()



'''we have averaged both the channels of the given stereo audio into one channel to get a mono audio - which is most suitble approach
for transcribing the audio in further steps
'''