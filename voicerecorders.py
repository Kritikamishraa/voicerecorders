import sounddevice as sd
from scipy.io.wavfile import write

# Sample rate
fs = 44100

second = int(input("Enter the time duration in seconds: "))
# Enter your required time
print("Recording...\n")

record_voice = sd.rec(int(second * fs), samplerate=fs, channels=2)

sd.wait()

write("Hello.wav", fs, record_voice)
print("Finished...\nPlease check the file.")
