import numpy as np
import soundfile as sf

# Constants
sampling_rate = 44100  # CD quality sampling rate
duration = 2.0          # Duration of each note in seconds

# Function to generate a piano note waveform
def generate_piano_note(freq):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    waveform = 0.5 * np.sin(2 * np.pi * freq * t)
    return waveform

# Define piano notes frequencies for a few keys
notes = {
    'C4': 261.63,   # Middle C
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25    # High C
}

# Generate and store each piano note
for note, freq in notes.items():
    waveform = generate_piano_note(freq)
    # Normalize waveform to avoid clipping
    waveform /= np.max(np.abs(waveform))
    # Write to file using soundfile
    filename = f"{note}.wav"
    sf.write(filename, waveform, sampling_rate)
    print(f"Generated and saved {note} to {filename}")
