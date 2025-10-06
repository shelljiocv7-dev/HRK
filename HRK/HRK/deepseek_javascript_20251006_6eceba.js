// 主要UI组件
const AudioEditor = () => {
  return (
    <div className="app-container">
      <FileUploader onUpload={handleUpload} />
      <WaveformDisplay 
        wavesurfer={wavesurferRef}
        onRegionSelected={handleRegionSelect}
      />
      <AudioControls 
        onPlay={handlePlay}
        onPause={handlePause}
        onZoom={handleZoom}
      />
      <EditingToolbar operations={availableOperations} />
      <MultiTrackMixer tracks={tracks} />
      <ExportPanel formats={exportFormats} />
    </div>
  );
};