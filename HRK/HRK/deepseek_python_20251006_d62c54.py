from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/upload")
@limiter.limit("10/minute")
async def upload_file(request: Request, file: UploadFile):
    # 上传逻辑
    pass