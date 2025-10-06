from pydub import AudioSegment
from pydub.effects import normalize, high_pass_filter
import librosa
import numpy as np

def apply_audio_operations(input_path: str, operations: list, output_path: str):
    # 加载音频
    audio = AudioSegment.from_file(input_path)
    
    for op in operations:
        if op['type'] == 'trim':
            audio = audio[op['start']:op['end']]
            
        elif op['type'] == 'fade_in':
            audio = audio.fade_in(op['duration'])
            
        elif op['type'] == 'fade_out':
            audio = audio.fade_out(op['duration'])
            
        elif op['type'] == 'volume':
            # 分贝增益计算
            gain_factor = 10 ** (op['gain'] / 20)
            audio = audio.apply_gain(gain_factor)
            
        elif op['type'] == 'normalize':
            audio = normalize(audio)
            
    # 导出
    audio.export(output_path, format=op['export_format'], 
                 bitrate=f"{op['bitrate']}k")