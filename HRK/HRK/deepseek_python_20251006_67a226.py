# tasks.py
from celery import Celery
import redis

celery_app = Celery(
    'audio_tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task
def process_audio_task(file_id, operations, export_format, bitrate):
    try:
        # 更新任务状态
        update_task_status(file_id, "processing")
        
        # 执行音频处理
        input_path = f"uploads/{file_id}"
        output_path = f"processed/{file_id}.{export_format}"
        
        apply_audio_operations(input_path, operations, output_path)
        
        # 上传到S3
        s3_url = upload_to_s3(output_path)
        
        update_task_status(file_id, "completed", s3_url)
        
    except Exception as e:
        update_task_status(file_id, "failed", str(e))

def update_task_status(file_id, status, result=None):
    # 通过Redis发布状态更新
    redis_client = redis.Redis()
    redis_client.publish(
        f"task_status:{file_id}",
        json.dumps({"status": status, "result": result})
    )