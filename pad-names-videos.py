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
                print("       ")
                #video = str(os.path.join(path,f))

                
                # newfilename = f_text.replace(" ","-") + ".mp4"
                newfilename = f_text.replace("_Trim_3.0","") + ".mp4"

               # cmd = "ffmpeg -i " + filename
                print("rename - ", f,newfilename,)
                os.rename(f,newfilename)

                # print(cmd)

