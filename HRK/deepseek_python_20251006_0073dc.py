def time_stretch_preserve_pitch(input_path: str, rate: float, output_path: str):
    """
    时间伸缩并保留音高
    """
    y, sr = librosa.load(input_path, sr=None)
    
    # 时间伸缩
    y_stretched = librosa.effects.time_stretch(y, rate=rate)
    
    # 音高校正（保留原始音高）
    y_shifted = librosa.effects.pitch_shift(
        y_stretched, sr=sr, n_steps=0)  # 不改变音高
    
    librosa.output.write_wav(output_path, y_shifted, sr)