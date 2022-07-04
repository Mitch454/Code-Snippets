## converts most without need to specify formats
```
ffmpeg -i iput.VOB output.mp4
ffmpeg -i iput.m4b output.mp3
```
## split by timestamp
```
ffmpeg -ss 00:00:00 -t 00:50:00 -i largefile.mp4 -acodec copy \-vcodec copy smallfile.mp4
```

## Crop 16:9 to 9:16
```
 ffmpeg -i input.mkv -filter:v "crop=9/16*ih:ih" output33.mp4
```

## letterbox pad for 9:16
```
ffmpeg -i input.mkv -vf "pad=iw:2*trunc(iw*16/18):(ow-iw)/2:(oh-ih)/2,setsar=1" -c:a copy output_letterbox.mp4
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


### compress 
```
ffmpeg -i input.mp4 -vcodec libx264 -crf 24 output.mp4
```

### scale down 1/3
```
ffmpeg -i input.mp4 -vf "scale=iw/3:ih/3" output.mp4
```
