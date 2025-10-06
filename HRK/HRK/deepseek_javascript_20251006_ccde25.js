// 波形显示配置
const wavesurfer = WaveSurfer.create({
  container: '#waveform',
  waveColor: '#4a90e2',
  progressColor: '#357abd',
  cursorColor: '#ffffff',
  barWidth: 2,
  barHeight: 1,
  responsive: true,
  normalize: true,
  plugins: [
    WaveSurfer.spectrogram.create({
      container: '#spectrogram',
      labels: true,
      colorMap: 'viridis'
    }),
    WaveSurfer.regions.create(),
    WaveSurfer.timeline.create()
  ]
});