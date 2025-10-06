import librosa

# 加载音频
y, sr = librosa.load("input.wav", sr=None)

# 时间伸缩，速率1.2
y_stretched = librosa.effects.time_stretch(y, rate=1.2)

# 保存音频
librosa.output.write_wav("output_stretched.wav", y_stretched, sr)