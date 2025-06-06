import os
from glob import glob
import librosa
import librosa.effects as lbe
import soundfile as sf
import numpy as np

def time_stretch(audio, rate=1.0):
    return lbe.time_stretch(y=audio, rate=rate)

def add_noise(audio, noise_factor=0.005):
    noise = np.random.randn(len(audio))
    return audio + noise_factor * noise

def augment_audio_file(y, sr, save_path, base_name):
    # Simpan original (opsional)
    sf.write(os.path.join(save_path, f"{base_name}_original.wav"), y, sr)

    # 1. pitch naik
    aug1 = lbe.pitch_shift(y=y, sr=sr, n_steps=2)
    sf.write(os.path.join(save_path, f"{base_name}_pitchup.wav"), aug1, sr)

    # 2. slow + pitch turun
    y_stretch = lbe.time_stretch(y=y, rate=0.9)
    aug2 = lbe.pitch_shift(y=y_stretch, sr=sr, n_steps=-2)
    sf.write(os.path.join(save_path, f"{base_name}_slow_pitchdown.wav"), aug2, sr)

    # 3. tambah noise
    aug3 = add_noise(y)
    sf.write(os.path.join(save_path, f"{base_name}_noise.wav"), aug3, sr)

def batch_augment_single_folder(source_folder, output_folder, sr_target=16000):
    os.makedirs(output_folder, exist_ok=True)
    audio_files = sorted(glob(os.path.join(source_folder, '*.wav')))

    if not audio_files:
        print(f"[WARNING] Tidak ada file .wav ditemukan di {source_folder}")
        return

    for wav_file in audio_files:
        base_name = os.path.splitext(os.path.basename(wav_file))[0]
        y, sr = librosa.load(wav_file, sr=sr_target)
        augment_audio_file(y, sr, output_folder, base_name)

    print(f"[DONE] Augmentasi selesai. Total file output: {len(audio_files) * 4}")

# Jalankan untuk folder spesifik
batch_augment_single_folder(
    source_folder='Audio/All/Seno/Warna',
    output_folder='Audio/Augmented/Seno/Warna'
)
