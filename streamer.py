import python_vlc.vlc as vlc
import pafy

def stream(id_key):
    url ='https://youtu.be/watch?v='+id_key
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)
    player.play()

if __name__ == "__main__":
    stream(input('Enter the video id\n>> '))
