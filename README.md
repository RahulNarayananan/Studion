# Studion
## Inspiration
In The current (2020) corona pandemic, where we students were facing troubles in online classes, we thought to build something that will help blind, deaf and even us as students.

## What it does
It helps the teacher and students connect via a chat box available as well as allows them to stream study content from youtube directly along with downloading the text spoken in video in both text and braille, along with downloading facilities of audio and video. It also attempts to summarize the hence obtained text and present that in braille as well.
 
## How we built it
We built this using python language and some python libraries and api available on net

## Prepare to use
Before using this project following python files needed to be installed\
python-vlc\
pafy\
googleclient\
youtube-dl\
moviepy\
shutil\
SpeechRecognition\
ntlk\
socket\
ffmpeg\
ffprobe\
webrtcvad\
should have enabled Youtube_api

After installing, StudIon.py should be lanched to start the project.\
To exit the client-server chat you may use Ctrl+C or close the window directly

## Challenges we ran into
We faced many challenges like finding the apt library to extract youtube content, we were stuck when the audio extracted from video won't convert to text at all for which we had to speed forward the silent parts of it while keeping the rest of audio as it is. Some more challenges that we faced were related to client-server chat wherein the socket connection would not connect. Even while converting to braille the encryption pattern didn't match for a few tries and audio to text conversion still is not completely accurate and there is scope of missing words and errors.

## Accomplishments that we are proud of
We are proud that we have reached wherever we are currently.
I didn't think I would be able to download youtube video, audio or infact text from it using python like this and I am proud that we did do it. 
I am also proud that we could make a socket connection and be able to chat using that

## What we learned
We learned the following things:\
youtube video extraction\
video to audio extraction\ 
audio to text conversion and dividing it into chunks based on silent parts\
modify video to speed up silent parts and keep other parts at same speed\
we learned about connection based on sockets and flask \
we learned the ways to summarise text and different potential algorithms\
text to brailler conversion and about encoding of braille language\
learned a bit more about ip addresses and how to potentially use them for file transfer (recieving and sending)\
Discord bots via python

## What's next for Studion
We are attempting to make it optionally voice activated so students work at ease with it\
We are looking for potential solutions as to enable video conferencing skills within the project\
We are trying to make it so multiple teachers and students can work on it together at same time via multiple devices\
We are attempting to make a discord bot which can let students know if the teacher is online and available to answer their queries\
We are trying include other video providers along with existing youtube \
We are aiming to provide a better text and summarization of the youtube video.\
Attempts are also being made to present this using a GUI (Graphical User Interface)\
We are also trying to add file upload system from students and teachers side and if it is a text document then possibly even convert that to audio and braille if requested by user students and teachers.

## Credits
My teammate who i worked on this project with: https://github.com/Nipunx23
Check out the following repositories which we took help to and modified as needed:\
https://github.com/LazoCoder/Braille-Translator   \
https://github.com/carykh/jumpcutter
