import os

extensions= ['mp4','mkv']

path= os.path.abspath(".")


if __name__ == "__main__":
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext= os.path.splitext(f)
            f_ext= f_ext[1:].lower()
            if f_ext in extensions:
                #cmd =  'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "' + f + '"'
                #os.system(cmd)
                # print(f)
                cmd = "bash trim.sh " + f + " 3.0 "
                print(cmd)
                os.system(cmd)
                #video = str(os.path.join(path,f))
