#audio file formats
'''
.mp3
.flac
.wav
'''


import wave

'''
audio signal parameters
num of channels
sample width
framerate/sample_rate: 44,000Hz (values in each sec)
num of frames
values of a frame

'''


obj = wave.open("hello.wav", "rb")

print("num of channels:", obj.getnchannels())
print("sample width:", obj.getsampwidth())
print("frame rate:", obj.getframerate())
print("number of frames:", obj.getnframes())
print("parameters:", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print("t_audio:", t_audio)

frames = obj.readframes(-1)
print(type(frames))
print(len(frames)/2)
obj.close() #
'''
obj_new = wave.open("hello_new.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames) 
obj_new.close()
'''
'''
import struct

# Open the original wave file
obj = wave.open("hello.wav", "rb")

# Extract parameters
n_channels = obj.getnchannels()
samp_width = obj.getsampwidth()
frame_rate = obj.getframerate()
n_frames = obj.getnframes()

print("Original audio parameters:")
print("Channels:", n_channels)
print("Sample width:", samp_width)
print("Frame rate:", frame_rate)
print("Number of frames:", n_frames)

# Read frames
frames = obj.readframes(n_frames)

# Convert stereo to mono if needed
if n_channels == 2:
    # Unpack the stereo frames (2 channels) into samples
    stereo_samples = struct.iter_unpack("<hh", frames)
    
    # Average the two channels to create mono samples
    mono_samples = [(left + right) // 2 for left, right in stereo_samples]

    # Pack the mono samples back into bytes
    frames = struct.pack("<" + "h" * len(mono_samples), *mono_samples)

# Close the original file
obj.close()

# Create a new wave file with the modified parameters
obj_new = wave.open("hello_new.wav", "wb")
obj_new.setnchannels(1)  # Mono
obj_new.setsampwidth(2)  # 16-bit
obj_new.setframerate(16000)  # 16 kHz

# Write the frames to the new file
obj_new.writeframes(frames)
obj_new.close()

print("New audio file 'hello_new.wav' created with mono channel and 16 kHz sample rate.")
'''

import struct
import numpy as np
from scipy.signal import resample

# Open the original wave file
obj = wave.open("hello.wav", "rb")

# Extract parameters
n_channels = obj.getnchannels()
samp_width = obj.getsampwidth()
frame_rate = obj.getframerate()
n_frames = obj.getnframes()

print("Original audio parameters:")
print("Channels:", n_channels)
print("Sample width:", samp_width)
print("Frame rate:", frame_rate)
print("Number of frames:", n_frames)

# Read frames
frames = obj.readframes(n_frames)

# Convert stereo to mono if needed
if n_channels == 2:
    # Unpack the stereo frames (2 channels) into samples
    stereo_samples = struct.iter_unpack("<hh", frames)
    
    # Average the two channels to create mono samples
    mono_samples = [(left + right) // 2 for left, right in stereo_samples]

    # Convert the list of mono samples into a NumPy array
    mono_samples = np.array(mono_samples, dtype=np.int16)
else:
    # If already mono, unpack the data as int16
    mono_samples = np.frombuffer(frames, dtype=np.int16)

# Resample the audio to the target sample rate (16,000 Hz)
new_rate = 16000
num_samples = int(len(mono_samples) * new_rate / frame_rate)
resampled_samples = resample(mono_samples, num_samples).astype(np.int16)

# Pack the resampled samples back into bytes
resampled_frames = struct.pack("<" + "h" * len(resampled_samples), *resampled_samples)

# Close the original file
obj.close()

# Create a new wave file with the modified parameters
obj_new = wave.open("hello_new.wav", "wb")
obj_new.setnchannels(1)  # Mono
obj_new.setsampwidth(2)  # 16-bit
obj_new.setframerate(32000.0)  # 16 kHz

# Write the frames to the new file
obj_new.writeframes(resampled_frames)
obj_new.close()

print("New audio file 'hello_new.wav' created with mono channel and 16 kHz sample rate.")