###Ross Lynch - On My Own (From Teen Beach 2).wav

import speech_recognition as sr
from braille.main import open_text as ot
from tkinter import messagebox

def generation(aud_file):
#    print(sr.__version__)
   r = sr.Recognizer()

   ff = aud_file

   file_audio = sr.AudioFile(ff)

   with file_audio as source:
      audio_text = r.record(source)

   print('\n\nExtracting Audio...\n\n')

   file_t = ff[:-4]+'.txt'

   # print(type(audio_text))
   try:
       conv = r.recognize_google(audio_text)
   
       with open(file_t,'w+') as f:
            f.write(conv)
       print('\n\ntext file created\n\n')

       ot(file_t)
       print('\n\nbraille file created\n\n')
       messagebox.showinfo('DONE','COMMAND EXECUTED SUCCESSFULY!!')
       return file_t
   except: messagebox.showerror('SOME ERROR!!','An Error occured while converting the video, please check language or fluency!')

if __name__ == "__main__":
    generation(input('Enter Audio FIle\n>> '))