import wave
import math
frequency = 4400  
amplitude = 400  
phase = 0         
duration = 1      
sample_rate = 44100 
num_samples = int(sample_rate * duration)
with wave.open('sine_wave.wav', 'w') as file:
    file.setnchannels(1)  
    file.setsampwidth(2)  
    file.setframerate(sample_rate)
    for i in range(num_samples):
        time = i / sample_rate
        sample = amplitude * math.sin(2 * math.pi * frequency * time + phase)
        normalized_sample = max(min(sample, 1.0), -1.0)
        sample_int = int(normalized_sample * 32767)
        sample_bytes = sample_int.to_bytes(2, byteorder='little', signed=True)
        file.writeframes(sample_bytes)
