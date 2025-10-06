from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range

@app.post("/process")
async def process_audio(request: AudioProcessRequest):
    """
    AudioProcessRequest 结构:
    {
        "file_id": "string",
        "operations": [
            {
                "type": "trim",
                "start": 1000,  # 毫秒
                "end": 5000
            },
            {
                "type": "fade_in",
                "duration": 500  # 毫秒
            },
            {
                "type": "volume",
                "gain": 3  # dB
            },
            {
                "type": "time_stretch", 
                "rate": 1.2,
                "preserve_pitch": true
            },
            {
                "type": "equalizer",
                "low": 2,
                "mid": 0, 
                "high": -1
            },
            {
                "type": "reverb",
                "reverberance": 50,
                "damping": 50,
                "room_scale": 50
            }
        ],
        "export_format": "mp3",
        "bitrate": 192
    }
    """
    task = process_audio_task.delay(request.dict())
    return {"job_id": task.id}