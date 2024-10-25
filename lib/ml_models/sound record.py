import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Parameters
fs = 44100  # Sample rate (44.1 kHz is standard)
duration = 5 # Duration of the recording in seconds
filename = "output_audio.wav"  # Output filename

def record_audio(duration, fs, filename):
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    write(filename, fs, audio_data)  # Save as WAV file
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    record_audio(duration, fs, filename)
