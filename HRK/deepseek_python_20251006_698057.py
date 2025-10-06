# 使用pydub调用ffmpeg滤镜
# 注意：pydub的AudioSegment对象可以通过`audio._data`获取原始数据，但滤镜操作需要直接使用ffmpeg命令行或通过pydub的`audio.apply_gain`等有限效果。

# 对于混响，我们可以使用ffmpeg的aecho滤镜，但pydub没有直接封装，我们可以通过自定义ffmpeg参数来实现：

from pydub import AudioSegment
import subprocess

# 首先将AudioSegment保存为临时文件，然后用ffmpeg处理
audio.export("temp_in.wav", format="wav")
cmd = [
    'ffmpeg',
    '-i', 'temp_in.wav',
    '-filter_complex', 'aecho=0.8:0.9:1000:0.3',
    'temp_out.wav'
]
subprocess.run(cmd)
processed_audio = AudioSegment.from_file("temp_out.wav")