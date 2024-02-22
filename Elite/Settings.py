import os, datetime, requests, re, json, platform, subprocess
from urllib.parse import quote
from Utils import clear, CheckDumpFile
from Color import bold_putih, bold_cyan, bold_lime, bold_merah, bold_kuning
from Banner import Choose, Back, BelumTersedia, MenuSettingsUserAgent, MenuSettingsFileManager, MenuOpsiFileManager, ShowFileResult
from Utils import CheckDevice

def Timenow():
    now = datetime.date.today()
    d, m, y = now.day, now.month, now.year
    return(d, m, y)

class UserAgent():

    def Menu(self):
        file = 'tools/manual_device.txt'
        try: x = open(file, 'r').read()
        except Exception as e: open(file, 'w').write(''); x = open(file, 'r').read()
        MenuSettingsUserAgent()
        ch = Choose()
        print('')
        match ch:
            case 0: Back()
            case 1: open(file, 'w').write(''); self.InputManual(file); Back()
            case 2: self.InputManual(file); Back()
            case 3: self.CheckFile(); Back()
            case 4: self.CheckDevice(); Back()
            case _: exit('{}Isi Yang Benar!{}'.format(bold_merah, bold_putih))

    #--> Default Device (Automatic)
    def DefaultSetup(self):
        file = 'tools/default_device.txt'
        try:
            x = open(file, 'r').read()
        except Exception as e:
            open(file, 'w').write('')
            x = open(file, 'r').read()
        self.DefaultSetup2(file, x)
    def DefaultSetup2(self, file, x):
        d1, m1, y1 = [int(i) for i in datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime("%d-%m-%Y").split('-')]
        d2, m2, y2 = Timenow()
        date_format_1 = '{}{}{}'.format(str(d1), str(m1), str(y1))
        date_format_2 = '{}{}{}'.format(str(d2), str(m2), str(y2))
        if (date_format_1 != date_format_2) or (len(x.splitlines()) == 0): # Jika Hari Baru / Jumlah Device 0
            open(file, 'w').write('')
            self.DumpDefaultDevice(file)
    def DumpDefaultDevice(self, filename):
        for i in ['sa|samsung', 'hu|huawei', 'op|oppo', 'vv|vivo', 're|realme','au|asus','xi|xiaomi','on|oneplus','0p|poco','cb|cubot']:
            self.ScrapUA(filename, i.split('|')[0], i.split('|')[1])
        print('\r', end='')
    def ScrapUA(self, filename, dev, device):
        con = ['en-us', 'zh-cn', 'shark', 'redmi', 'zh-tw', 'fr-fr', 'mi', 'harmonyos', 'es-es', 'es-us', 'pl-pl']
        try:
            r = requests.Session()
            req = r.get('https://whatmyuseragent.com/brand/{}/{}'.format(str(dev), str(device)), allow_redirects=True).text.replace('\\','')
            for i in re.findall(r'<td class="useragent">(.*?)</td>',str(req)):
                try:
                    cr = i.split('Android')[1].split(';')[1].strip().split(' ')[0].replace('(','').replace(')','').replace('','')
                    if (device.lower() != cr.lower()) and (cr not in open(filename, 'r').read().splitlines()) and (cr.lower() not in con): open(filename, 'a+').write('{}\n'.format(str(cr)))
                    print('\r{}Scanning {}{} {}Devices'.format(bold_putih, bold_cyan, str(len(open(filename, 'r').read().splitlines())), bold_putih), end='', flush=True)
                except Exception as e: continue
            r.close()
        except Exception as e: pass

    #--> Manual Device
    def InputManual(self, filename):
        my_ua = []
        try: lp = int(input('{}Berapa User Agent : {}'.format(bold_putih, bold_lime)))
        except Exception as e: exit('\n{}Isi Yang Benar!{}\n'.format(bold_merah, bold_putih))
        for i in range(1,lp+1):
            j = input('\n{}User Agent {}{} {}: {}'.format(bold_putih, bold_cyan, str(i), bold_putih, bold_lime))
            r = requests.Session()
            try: device = r.get('https://www.whatsmyua.info/api/v1/ua?ua={}'.format(str(quote(j)))).json()[-1].get('device').get('product')
            except Exception as e: device = None
            print('{}Device {}{} {}Terdeteksi'.format(bold_putih, bold_cyan, str(device), bold_putih) if device != None else '{}Device Tidak Diketahui!{}'.format(bold_merah, bold_putih))
            if (device != None) and (device not in my_ua): my_ua.append(device)
        print('{}'.format(bold_putih))
        for i in my_ua:
            if i not in open(filename, 'r').read().splitlines(): open(filename, 'a+').write('{}\n'.format(str(i)))

    #--> Check All Devices In File
    def CheckFile(self):
        x = open('tools/manual_device.txt', 'r').read().splitlines()
        y = open('tools/default_device.txt', 'r').read().splitlines()
        print('{}Custom Device : {}{}\n'.format(bold_putih, bold_cyan, ('{}, {}'.format(bold_putih, bold_cyan)).join(x)))
        print('{}Default Device : {}{}\n'.format(bold_putih, bold_cyan, ('{}, {}'.format(bold_putih, bold_cyan)).join(y)))

    #--> Check Device
    def CheckDevice(self):
        info = CheckDevice()
        if (info.get('device').lower() == 'computer') and (info.get('system').lower() == 'windows'):
            user_agent = 'Mozilla/5.0 ({} NT {}; {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'.format(info.get('system'), info.get('version'), info.get('model'), info.get('build'))
        elif (info.get('device').lower() == 'android') and (info.get('system').lower() == 'linux'):
            user_agent = 'Mozilla/5.0 ({}; {} {}; {} Build/{}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.0000.00 Mobile Safari/537.36'.format(info.get('system'), info.get('device'), info.get('version'), info.get('model'), info.get('build'))
        else:
            user_agent = '{}Tidak Diketahui{}'.format(bold_merah, bold_putih)
        print('{}Jenis Perangkat : {}{}{}'.format(bold_putih, bold_cyan, info.get('device'),  bold_putih))
        print('{}Sistem Operasi  : {}{}{}'.format(bold_putih, bold_cyan, info.get('system'),  bold_putih))
        print('{}Versi OS        : {}{}{}'.format(bold_putih, bold_cyan, info.get('version'), bold_putih))
        print('{}Model Perangkat : {}{}{}'.format(bold_putih, bold_cyan, info.get('model'),   bold_putih))
        print('{}Versi Build     : {}{}{}'.format(bold_putih, bold_cyan, info.get('build'),   bold_putih))
        print('{}User Agent      : {}{}{}'.format(bold_putih, bold_cyan, user_agent,          bold_putih))
        print('')

class FileManager():

    def __init__(self):
        self.Opt = 1

    def Main(self):
        MenuSettingsFileManager(); ch = Choose()
        MenuOpsiFileManager(); co = Choose()
        match co:
            case 0: Back()
            case 1: self.Opt = 1
            case 2: self.Opt = 2
            case 3: self.Opt = 3; BelumTersedia(); Back()
            case _: exit('\n{}Isi Yang Benar!{}\n'.format(bold_merah, bold_putih))
        match ch:
            case 0: Back()
            case 1: self.ControlFileDump()
            case 2: self.ControlFileResult()
            case 3: BelumTersedia(); Back()
            case _: exit('\n{}Isi Yang Benar!{}\n'.format(bold_merah, bold_putih))

    def ControlFileDump(self):
        choosen_file = []
        all_file = CheckDumpFile(1)
        b = self.ChooseFile()
        for file in all_file:
            for num in b:
                if (int(num) == int(file.split('|')[0])) and (file not in choosen_file): choosen_file.append(file)
        if self.Opt == 1:
            for i in choosen_file:
                d, e = i.split('|')
                self.ShowFileDump('dump/{}'.format(e))
        elif self.Opt == 2:
            for i in choosen_file:
                d, e = i.split('|')
                self.DeleteFile('dump/{}'.format(e))
        print()
        Back()

    def ControlFileResult(self):
        choosen_file = []
        a = self.ScanFileResult()
        b = self.ChooseFile()
        for file in a:
            for num in b:
                if (int(num) == int(file.split('|')[0])) and (file not in choosen_file): choosen_file.append(file)
        if self.Opt == 1:
            for i in choosen_file:
                self.ShowFileResult(i)
        elif self.Opt == 2:
            for i in choosen_file:
                d, e, f, g = i.split('|')
                self.DeleteFile('{}{}'.format(e,f))
        print()
        Back()

    def ShowFileDump(self, path):
        print('\n{}Path : {}{}{}'.format(bold_putih, bold_cyan, path, bold_putih))
        op = open(path, 'r').read().splitlines()
        print('{}Tidak Ada Target{}'.format(bold_merah, bold_putih) if len(op) == 0 else '{}Jumlah Target : {}{}{}'.format(bold_putih, bold_cyan, str(len(op)), bold_putih))
        if len(op) != 0: print('{}, '.format(bold_putih).join(['{}{}'.format(bold_cyan, i) for i in op]))

    def ScanFileResult(self):
        all_file = []
        x = ['{}|result/OK/|{}|{}'.format(str(l+1), str(f.name), str(len(open('result/OK/{}'.format(str(f.name)), 'r').read().splitlines()))) for l, f in enumerate(os.scandir('result/OK'))]
        try: h = int(x[-1].split('|')[0]) + 1
        except Exception as e: h = 1
        y = ['{}|result/CP/|{}|{}'.format(str(h+l), str(f.name), str(len(open('result/CP/{}'.format(str(f.name)), 'r').read().splitlines()))) for l, f in enumerate(os.scandir('result/CP'))]
        all_file = all_file + x + y
        ShowFileResult(x, y)
        return(all_file)

    def ShowFileResult(self, dict_file):
        a, b, c, d = dict_file.split('|')
        print('\n{}Path : {}{}{}{}'.format(bold_putih, bold_cyan, b, c, bold_putih))
        op = open('{}{}'.format(b, c), 'r').read().splitlines()
        print('{}Tidak Ada Hasil{}'.format(bold_merah, bold_putih) if len(op) == 0 else '{}Jumlah Akun : {}{}{}'.format(bold_putih, bold_cyan, str(len(op)), bold_putih))
        for i in op:
            if 'OK' in str(b): print('  {}• {}{}{}'.format(bold_putih, bold_lime, i, bold_putih))
            elif 'CP' in str(b): print('  {}• {}{}{}'.format(bold_putih, bold_kuning, i, bold_putih))
            else: pass

    def DeleteFile(self, path):
        try: os.remove(path)
        except Exception as e: pass

    def ChooseFile(self):
        print('\n{}Banyak File, Pisahkan Dengan Koma ({},{})'.format(bold_putih, bold_cyan, bold_putih))
        try: ip = [int(i) for i in input('{}Pilih File ({}Angka{}) : {}'.format(bold_putih, bold_cyan, bold_putih, bold_lime)).replace(' ','').split(',')]
        except Exception as e: exit('{}Isi Yang Benar!{}'.format(bold_merah, bold_putih))
        return(ip)