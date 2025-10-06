@app.post("/upload")
async def upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    # 文件类型验证
    allowed_types = ['audio/mpeg', 'audio/wav', 'audio/ogg', 'audio/mp4']
    if file.content_type not in allowed_types:
        raise HTTPException(400, "不支持的音频格式")
    
    # 分块上传处理
    file_id = str(uuid.uuid4())
    file_path = f"uploads/{file_id}_{file.filename}"
    
    # 异步处理文件
    background_tasks.add_task(process_uploaded_file, file_path, file_id)
    
    return {"file_id": file_id, "status": "processing"}