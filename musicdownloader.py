import vk_api
from vk_api import audio
import requests
from time import time
import os
import threading
import time
import getpass

def auth_handler():
        key = input("У вас включена 2-ух факторная аутентификация, введите код: ")
        remember_device = True
        return key, remember_device
def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)
while True:
    login=input("Введите логин: ")
    password=input('Введите пароль: ')
    vk_session = vk_api.VkApi(login=login, password=password,auth_handler=auth_handler,captcha_handler=captcha_handler)
    try:
        vk_session.auth()
        break
    except:
            print("Неверный логин или пароль.")
vk = vk_session.get_api()
getuserid = vk.users.get()
os.system("cls")
while True:
    questid = input("1)Скачать свою музыку\n2)Скачать музыку другого пользователя (необходимо, чтобы вы имели к ней доступ)\nВыбор:")
    if questid == '1':
       user_id=getuserid[0]['id']
       break
    if questid == '2':
       user_id=input("Введите id пользователя:")
       break
    else:
        print("Ошибка")
vk_audio = audio.VkAudio(vk_session)
global_start_time = time.time()
audiocount=0

filepath=input('Введите путь сохранения файлов:')

i = vk_audio.get(owner_id=user_id)
for audiocount in range(len(i)):
        checkname =0
        checkartist=0
        if audiocount < 10:
            audiocount='0'+str(audiocount)
            audiocount=int(audiocount)
        audio = i[audiocount]
        audioartist=audio['artist']
        audioname=audio['title']
        audiourl=audio['url']
        audioartist=audioartist.replace('/', '-')
        audioartist=audioartist.replace('\\', '-')
        audioartist=audioartist.replace('|', '-')
        audioartist=audioartist.replace('*', '-')
        audioartist=audioartist.replace('"', '-')
        audioartist=audioartist.replace(':', '-')
        audioartist=audioartist.replace('<', '-')
        audioartist=audioartist.replace('>', '-')
        audioartist=audioartist.replace('?', '-')
        audioname=audioname.replace('?', '-')
        audioname=audioname.replace('"', '-')
        audioname=audioname.replace('*', '-')
        audioname=audioname.replace('|', '-')
        audioname=audioname.replace('<', '-')
        audioname=audioname.replace('>', '-')
        audioname=audioname.replace('/', '-')
        audioname=audioname.replace('\\', '-')
        audioname=audioname.replace(':', '-')
        fullfilename = filepath+"\\"+audioartist+' - '+audioname+'.mp3'
        checkfile = os.path.exists(fullfilename)
        if checkfile == False:
            print("["+str(audiocount)+"/"+str(len(i))+"]"+"Скачиваю: "+audioartist+' - '+audioname)
            file = open(fullfilename,'wb')
            ufr = requests.get(audiourl)
            file.write(ufr.content)
        else:
            print("["+str(audiocount)+"/"+str(len(i))+"]"+"Уже скачан: "+audioartist+' - '+audioname)

