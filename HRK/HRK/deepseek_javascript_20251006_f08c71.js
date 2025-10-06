// 假设我们有一个选区，然后点击裁剪按钮
document.getElementById('trim-btn').onclick = function() {
    var region = wavesurfer.regions.list[Object.keys(wavesurfer.regions.list)[0]];
    if (region) {
        var start = region.start;
        var end = region.end;
        // 调用后端处理接口，提交裁剪任务
        fetch('/process', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                file_id: fileId,
                operations: [{type: 'trim', start: start*1000, end: end*1000}],
                export_format: 'mp3',
                bitrate: 192
            })
        }).then(response => response.json()).then(data => {
            // 获取任务ID，然后轮询状态
            var jobId = data.job_id;
            checkProgress(jobId);
        });
    }
};