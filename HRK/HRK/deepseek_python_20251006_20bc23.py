import subprocess

def apply_ffmpeg_effects(input_path: str, effects: dict, output_path: str):
    """
    应用FFmpeg音频特效
    """
    cmd = ['ffmpeg', '-i', input_path]
    
    if 'reverb' in effects:
        reverb = effects['reverb']
        cmd.extend([
            '-af', 
            f'aecho={reverb["in_gain"]}:{reverb["out_gain"]}:{reverb["delays"]}:{reverb["decays"]}'
        ])
    
    if 'equalizer' in effects:
        eq = effects['equalizer']
        cmd.extend([
            '-af',
            f'equalizer=f=100:width_type=o:width=2:g={eq["low"]},'
            f'equalizer=f=1000:width_type=o:width=2:g={eq["mid"]},'
            f'equalizer=f=10000:width_type=o:width=2:g={eq["high"]}'
        ])
    
    cmd.append(output_path)
    subprocess.run(cmd, check=True)