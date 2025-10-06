from pydub import AudioSegment
from pydub.effects import normalize

# 加载音频
audio = AudioSegment.from_file("input.wav")

# 裁剪（毫秒）
start = 1000
end = 5000
trimmed = audio[start:end]

# 淡入淡出
faded = trimmed.fade_in(500).fade_out(500)

# 音量增益（dB）
louder = faded + 3  # 提高3dB

# 归一化
normalized = normalize(louder)

# 导出
normalized.export("output.wav", format="wav")