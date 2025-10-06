def validate_audio_file(file: UploadFile):
    # 文件大小限制 (200MB)
    max_size = 200 * 1024 * 1024
    if file.size > max_size:
        raise HTTPException(413, "文件大小超过限制")
    
    # 文件类型验证
    signature = file.file.read(12)
    file.file.seek(0)
    
    if not is_valid_audio_signature(signature):
        raise HTTPException(400, "无效的音频文件")