import os
from googleapiclient import discovery
import yt_aud as cc
import aud_txt as pp

def search(search_by):
    api_key='AIzaSyBd_L6MjVsVeGUIapCsKWvVzLarMLw7j_E'
    youtube = discovery.build('youtube', 'v3', developerKey=api_key)
    MAX_COUNT = 50
    nextPageToken =  None
    req = youtube.search().list(q=search_by, part='snippet', type='video', videoDuration = 'short' , maxResults=MAX_COUNT, pageToken=nextPageToken)
    res = req.execute()
    id_key = res['items'][0]['id']['videoId']
    return id_key
    # print(id_key)
    
if __name__ == "__main__":
    id_key = search(search_by = input('>> '))
    fin = cc.get_mp3(id_key)
    pp.generation(fin)