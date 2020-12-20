from tkinter import messagebox
import yt
import yt_aud as cc
import aud_txt as pp
import sumariser as ss
import streamer as st
import client
import serverC

search_history = []
text_history = []

def m1():
    global search_history
    history_key = yt.search(input('Enter content to search\n>> '))
    search_history.append(history_key)
    print('\n\nSEARCH DONE YOU MAY NOW PROCEDE\n\n')
    menu()

def m2():
    global search_history
    st.stream(search_history[-1])
    menu()

def m3():
    global search_history, text_history
    id_key = search_history[-1]
    fin = cc.get_mp3(id_key)
    txt = pp.generation(fin)
    text_history.append(txt)
    menu()

def m4():
    global text_history
    ss.generate_summary(text_history[-1])
    menu()

def m5():
    serverC.run()
    menu()

def m6():
    client.run()
    menu()

def menu():
    global search_history, text_history
    command_list = {'1':m1,'2':m2,'3':m3,'4':m4,'5':m5,'6':m6}
    print('''
    +++++++++++++++++++++++++++++++ STUDION +++++++++++++++++++++++++++++++++++++++++\n
    ---------Command Menu-----------\n
    Code                           Command
      1                 search for video
      2                 stream searched video (Please ensure to have vlc 64-bit version installed)
      3                 convert video content to text+braille
      4                 summarise content to text+braille
      5                 login as teacher
      6                 login as student\n
      NOTE:
      ->command 1 should be used before all other commands      
      ->command 4 should only be run after running command 3
    ''')
    ch = input('Enter code choice\n>> ')
    if search_history == [] and ch not in '156':
        messagebox.showwarning('Empty Search','Please Search Something before running other commands')
        menu()
    elif text_history == [] and ch=='4':
        messagebox.showwarning('Empty Convert','Please run command 3')
        menu()
    else:
        command_list[ch]()

menu()