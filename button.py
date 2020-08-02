#!/usr/bin/python2
# coding=utf-8

import os,sys,time,datetime,json,urllib,re,cookielib,requests
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')


os.system('clear')

print """\033[32;1m
████████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ ██╗     
╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗██║     
   ██║   ██║   ██║██╔████╔██║██████╔╝██║   ██║██║     
   \033[1;30m██║   ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║██║     
   ██║   ╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝███████╗
   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                      
"""
print "\033[91m•\033[1;30m# \033[1;33mAuthor  : \033[32;1mVx "
print "\033[91m•\033[1;30m# \033[1;33mYoutube : \033[32;1mOmVx "
print "\033[91m•\033[1;30m# \033[1;33mTeam    : \033[32;1mOrca Security Leader "
print "\033[91m•\033[1;30m# \033[1;33mIg      : \033[32;1m@NoborrerTermux "
print ""

if __name__=='__main__':
    
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/":
            print "\033[1;32mProcess\033[1;33m...."
            sleep(0.1)

print ""
print " \033[91m» \033[1;32mSudah Selesai..., Jangan Lupa Check "
time.sleep(0.75)
print " \033[91m» \033[1;32mIg @NoborrerTermux "
time.sleep(0.75)
print ""
print " \033[91m» \033[1;32mTerimakasi Blo ^_^ "
time.sleep(0.75)
print ""
