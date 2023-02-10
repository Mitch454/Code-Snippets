from pyffmpeg import FFmpeg


f = "test.mkv"


ff = FFmpeg()
# ff.options(f"-i {f}  output.png")
ff.options(f"-ss 0.5  -i {f} -frames:v 1 -s 480x300 -f image2 imagefile.png")