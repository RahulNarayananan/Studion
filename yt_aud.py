import pafy
from moviepy.editor import *
import os, shutil
import string
import unicodedata
import subprocess

def filevalid(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)


def get_mp3(id_key):
    url ='https://www.youtube.com/watch?v='+id_key
    output = 'wav'
    print("Converting...")

    mp4 = pafy.new(url)
    best = mp4.getbest(preftype='mp4')
    name = filevalid(mp4.title)
    f_name = name+'.'+best.extension
    f_name = f_name.replace('-','')
    f_name = f_name.replace(' ','_')
    best.download(filepath = './'+f_name)
    n_name = 'mod_'+f_name

    f_q = os.path.abspath(f_name)
    n_q = os.path.dirname(f_name) + n_name

    subprocess.run(["python","silencer.py","--input_file","{}".format(f_q),"--output_file","{}".format(n_q),"--sounded_speed", "1", "--silent_speed","20", "--frame_margin", "2"])

    mp3 = n_name[:-4] + f".{output}"

    video_clip = VideoFileClip(n_name)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    os.rename(n_name[:-4]+'.wav',name+'.wav')

    audio_clip.close()
    video_clip.close()

    os.remove(f_name)
    os.remove(n_name)
    aud_file = name+'.wav'
    print('Please Wait...')
    return aud_file
    
##    shutil.move(mp3, r"C:\Users\Nipun\Desktop")


if __name__ == "__main__":
    get_mp3(input('Enter id\n>> '))