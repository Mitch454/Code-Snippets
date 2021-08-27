## converts most without need to specify formats
```
ffmpeg -i iput.VOB output.mp4
ffmpeg -i iput.m4b output.mp3
```

### Crop pixels from the bottom
```
ffmpeg -i input.mp4 -filter_complex "[0:v]crop=in_w:in_h-10:0:0[cropped]" -map "[cropped]" output.mp4
```

### rotate,  res++
```
ffmpeg -i input.mov  -r 30 -b:v 50000k -vf "transpose=dir=2" output.mp4

```


### speed
```
ffmpeg -i input.mp4 -filter:v "setpts=0.5*PTS" faster.mp4

ffmpeg -i input.mp4 -filter:v setpts=2.0*PTS slower.mp4
```


