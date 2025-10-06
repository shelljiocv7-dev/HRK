var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    scrollParent: true,
    backend: 'WebAudio',
    plugins: [
        WaveSurfer.regions.create(),
        WaveSurfer.timeline.create()
    ]
});

wavesurfer.load('audio.wav');