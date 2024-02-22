import os, sys, json, re, requests, time, datetime, random, platform, subprocess
from Color import bold_putih, bold_cyan, bold_merah
from Banner import Back

DefaultUAWindows   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
HeadersGetWindows  = lambda i=DefaultUAWindows : {'Host':'www.facebook.com','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9, id-ID,id;q=0.8','Cache-Control':'max-age=0','Dpr':'2','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Windows"','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Ch-Ua-Model':'','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','Priority':'u=0, i','User-Agent':i}
HeadersPostWindows = lambda i=DefaultUAWindows : {'Host':'www.facebook.com','Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9, id-ID,id;q=0.8','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Windows"','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Ch-Ua-Model':'','Sec-Fetch-Site':'same-origin','User-Agent':i}

DefaultUAAndroid   = 'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.0.65;]'
HeadersGetAndroid  = lambda i=DefaultUAAndroid : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'2','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i}
HeadersPostAndroid = lambda i=DefaultUAAndroid : {'Host':'m.facebook.com','Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9, id-ID,id;q=0.8','Content-Type':'application/x-www-form-urlencoded','Origin':'https://m.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Android"','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Ch-Ua-Model':'','Sec-Fetch-Site':'same-origin','User-Agent':i}

DefaultUADalvik = '[FBAN/FB4A;FBAV/417.0.0.33.65;FBBV/480086274;FBDM/{density=3.0,width=1440,height=2560};FBLC/id_ID;FBRV/0;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3740;FBSV/7.1.2;FBOP/1;FBCA/x86:armeabi-v7a;]'
HeadersPostDalvik = lambda i = DefaultUADalvik : {'Host':'graph.facebook.com', 'X-Fb-Request-Analytics-Tags':json.dumps({"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}), 'X-Fb-Rmd':'state=URL_ELIGIBLE', 'X-Fb-Sim-Hni':'51002', 'X-Fb-Net-Hni':'51002', 'X-Fb-Friendly-Name':'FriendListContentQuery', 'X-Graphql-Client-Library':'graphservice', 'Content-Type':'application/x-www-form-urlencoded', 'X-Fb-Connection-Type':'WIFI', 'X-Fb-Background-State':'1', 'X-Graphql-Request-Purpose':'fetch', 'User-Agent':i, 'X-Fb-Privacy-Context':'2368177546817046', 'X-Fb-Device-Group':'5000', 'X-Tigon-Is-Retry':'False', 'Priority':'u=3,i', 'Accept-Encoding':'gzip, deflate', 'X-Fb-Http-Engine':'Liger', 'X-Fb-Client-Ip':'True', 'X-Fb-Server-Cluster':'True', 'Content-Length':'1000'}
DefultDataDalvik = lambda : {'method':'post', 'pretty':False, 'format':'json', 'server_timestamps':True, 'locale':'id_ID', 'purpose':'fetch', 'fb_api_analytics_tags':'["At_Connection","GraphServices"]'}

#--> Clear Terminal
def clear(): os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

#--> Install Module & Library
def requirements_module():
    try: import requests
    except Exception as e: os.system('pip install requests'); import requests
    try: import bs4; from bs4 import BeautifulSoup as bs
    except Exception as e: os.system('pip install bs4'); import bs4; from bs4 import BeautifulSoup as bs

#--> Create Directory
def create_directory():
    try: os.mkdir('login')
    except Exception as e: pass
    try: os.mkdir('dump')
    except Exception as e: pass
    try: os.mkdir('result')
    except Exception as e: pass
    try: os.mkdir('tools')
    except Exception as e: pass
    try: os.makedirs('result/OK', exist_ok=True)
    except Exception as e: pass
    try: os.makedirs('result/CP', exist_ok=True)
    except Exception as e: pass

#--> Get Time
def GetTime():
    now = datetime.datetime.now()
    bul = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
    tem = [now.second, now.minute, now.hour, now.day, bul[now.month-1], now.year]
    return(tem)

#--> Visitor Count
def GetUserCount():
    filename = 'tools/user_id.txt'
    try:
        try:
            user_id = open(filename, 'r').read()
            return({'user_id':user_id, 'visitor':'0', 'online':'0'})
        except Exception as e:
            r = requests.Session()
            req = r.get('https://justpaste.it/dm4w2').text.replace('\\','')
            visitor = str(re.search(r'"viewsText":"(.*?)"',str(req)).group(1))
            online = str(re.search(r'"onlineText":"(.*?)"',str(req)).group(1))
            user_id = 'TSTLCHG00{}{}'.format('0'*(5-len(visitor)), visitor)
            open(filename, 'w').write(user_id)
            return({'user_id':user_id, 'visitor':str(visitor), 'online':str(online)})
    except Exception as e: return({'user_id':'TSTLCHGUNKNOWN', 'visitor':'0', 'online':'0'})

#--> Convert Cookie
def ConvertCookie(cok):
    try:
        sb     = re.search('sb=(.*?);',     str(cok)).group(1)
        datr   = re.search('datr=(.*?);',   str(cok)).group(1)
        c_user = re.search('c_user=(.*?);', str(cok)).group(1)
        xs     = re.search('xs=(.*?);',     str(cok)).group(1)
        fr     = re.search('fr=(.*?);',     str(cok)).group(1)
        cookie = f'sb={sb}; datr={datr}; c_user={c_user}; xs={xs}; fr={fr};'
    except Exception as e: cookie = cok
    return(cookie)

#--> IP Geolocator
def GeoLocator():
    try:
        _r_ = requests.Session()
        _g_ = _r_.get('https://ipinfo.io/json').json()
        ip = _g_['ip']
    except Exception as e: ip = 'Unknown'
    return(ip)

#--> Delay
def Delay(t):
    for x in range(t+1):
        print('\r%sTunggu %s Detik                                 '%(bold_putih,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

#--> Convert ID To URL
def ConvertURL(i):
    if 'http' in str(i):
        if   'www.facebook.com'    in str(i): url = i
        elif 'm.facebook.com'      in str(i): url = i.replace('m.facebook.com','www.facebook.com')
        elif 'mbasic.facebook.com' in str(i): url = i.replace('mbasic.facebook.com','www.facebook.com')
        elif 'web.facebook.com'    in str(i): url = i.replace('web.facebook.com','www.facebook.com')
    else:
        if   'www.facebook.com'    in str(i): url = 'https://' + i
        elif 'm.facebook.com'      in str(i): url = 'https://' + i.replace('m.facebook.com','www.facebook.com')
        elif 'mbasic.facebook.com' in str(i): url = 'https://' + i.replace('mbasic.facebook.com','www.facebook.com')
        elif 'web.facebook.com'    in str(i): url = 'https://' + i.replace('web.facebook.com','www.facebook.com')
        else:
            if 'facebook.com' in str(i).lower(): url = 'https://www.facebook.com' + i.replace('facebook.com','').replace('Facebook.com','')
            else: url = 'https://www.facebook.com/%s'%(i)
    return(url)

#--> Scrap Data
def GetData(req):
    try:
        av = re.search(r'"actorID":"(.*?)"',str(req)).group(1)
        __user = av
        __a = str(random.randrange(1,6))
        __hs = re.search(r'"haste_session":"(.*?)"',str(req)).group(1)
        __ccg = re.search(r'"connectionClass":"(.*?)"',str(req)).group(1)
        __rev = re.search(r'"__spin_r":(.*?),',str(req)).group(1)
        __spin_r = __rev
        __spin_b = re.search(r'"__spin_b":"(.*?)"',str(req)).group(1)
        __spin_t = re.search(r'"__spin_t":(.*?),',str(req)).group(1)
        __hsi = re.search(r'"hsi":"(.*?)"',str(req)).group(1)
        fb_dtsg = re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
        jazoest = re.search(r'jazoest=(.*?)"',str(req)).group(1)
        lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
        Data = {'av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd}
        return(Data)
    except Exception as e: return({})

#--> Scrap Data No login
def GetDataNoLogin(req):
    try:
        av = '0'
        __user = av
        __a = str(random.randrange(1,6))
        __hs = re.search(r'"haste_session":"(.*?)"',str(req)).group(1)
        __ccg = re.search(r'"connectionClass":"(.*?)"',str(req)).group(1)
        __rev = re.search(r'"__spin_r":(.*?),',str(req)).group(1)
        __spin_r = __rev
        __spin_b = re.search(r'"__spin_b":"(.*?)"',str(req)).group(1)
        __spin_t = re.search(r'"__spin_t":(.*?),',str(req)).group(1)
        __hsi = re.search(r'"hsi":"(.*?)"',str(req)).group(1)
        jazoest = re.search(r'jazoest=(.*?)"',str(req)).group(1)
        lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
        Data = {'av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','jazoest':jazoest,'lsd':lsd}
        return(Data)
    except Exception as e: return({})

#--> Check File Dump
def CheckDumpFile(type=0):
    path, loop, tur = 'dump', 0, {}
    try:
        print('\n{}[ {}File Dump {}]'.format(bold_putih, bold_cyan, bold_putih))
        for entry in os.scandir(path):
            if entry.is_file():
                loop += 1
                name = str(entry.name) if len(str(entry.name)) <= 26 else str(entry.name)[:23]+'...'
                total_id = len(open('{}/{}'.format(path, entry.name), 'r').read().splitlines())
                times = datetime.datetime.fromtimestamp(os.path.getmtime('{}/{}'.format(path, entry.name))).strftime('%d-%m-%Y %H:%M:%S')
                fm = '{}[{}{}{}] {}{} {} ID{}{}'.format(bold_putih, bold_cyan, str(loop), bold_putih, str(name), ' '*(27-len(str(name))), str(total_id), ' '*(8-len(str(total_id))), times)
                print(fm); tur.update({loop:str(entry.name)})
    except Exception as e: exit('\n{}Terjadi Kesalahan{}, Folder Tidak Ditemukan\nAtau Anda Belum Mengizinkan Tools Ini\nUntuk Mengakses File Pada Perangkat Anda\n'.format(bold_merah, bold_putih))
    if type == 1:
        if loop == 0: print('\n{}Anda {}Belum Memiliki {}File Dump!\n'.format(bold_putih, bold_merah, bold_putih)); Back()
        else: return(['{}|{}'.format(str(i), str(j)) for i, j in tur.items()])
    elif type == 2:
        if loop == 0: print('\n{}Anda {}Belum Memiliki {}File Dump!\nDump Terlebih Dahulu Sebelum Lanjut Ke Proses Crack\n'.format(bold_putih, bold_merah, bold_putih)); Back()
        else:
            try: res = tur[int(input('{}Pilih : {}'.format(bold_putih, bold_cyan)))]; return(res)
            except Exception as e: exit('\n{}Isi Yang Benar!{}\n'.format(bold_merah, bold_putih))

#--> Check System
def CheckDevice():
    try:
        system = platform.system()
        if system.lower() == 'windows':
            device  = 'Computer' if 'computer' in str(os.environ).lower() else 'Unknown'
            version = '.'.join(str(platform.version()).split('.')[:2])
            model   = 'Win64' if '64' in str(platform.architecture()[0]) else 'Win32'
            build   = 'x64' if '64' in str(platform.architecture()[0]) else 'x86'
        elif system.lower() == 'linux':
            device  = 'Android' if 'android' in str(os.environ).lower() else 'Unknown'
            version = str(subprocess.check_output("getprop ro.build.version.release", shell=True).decode("utf-8").replace("\n",""))
            model   = str(subprocess.check_output("getprop ro.product.model", shell=True).decode("utf-8").replace("\n",""))
            build   = str(subprocess.check_output("getprop ro.build.id", shell=True).decode("utf-8").replace("\n",""))
        return({'system':system, 'device':device, 'version':version, 'model':model, 'build':build})
    except Exception as e:
        return({'system':'Unknown', 'device':'Unknown', 'version':'Unknown', 'model':'Unknown', 'build':'Unknown'})

#--> Convert ID
def ConvertID(raw_id):
    try:
        r = requests.Session()
        url = 'https://www.facebook.com/' + raw_id
        req = r.get(url, allow_redirects=True).text.replace('\\','')
        if ('ab_test_data' in str(req)) or ('page_id_type' in str(req)) or ('facebook' not in str(re.search(r'name="description" content="(.*?)"',str(req)).group(1)).lower()):
            return({'raw_id':raw_id, 'id':'0', 'username':'0', 'name':'0'})
        else:
            id = str(re.search(r'"fb://profile/(.*?)"',str(req)).group(1))
            cek = str(re.search(r'href="https://web.facebook.com/(.*?)"',str(req)).group(1))
            username = id if ('people' in cek) or ('profile.php' in cek) else cek
            name = str(re.search(r'property="og:title" content="(.*?)"',str(req)).group(1))
            r.close()
            return({'raw_id':raw_id, 'id':id, 'username':username, 'name':name})
    except Exception as e:
        return({'raw_id':raw_id, 'id':'0', 'username':'0', 'name':'0'})

# Get Token
def GetTokenEAAQ(cookie):
    r = requests.Session() 
    r1 = r.get('https://graph.facebook.com/v18.0/device/login/?method=POST&access_token=1174099472704185|0722a7d5b5a4ac06b11450f7114eb2e9').json()
    f1 = re.search(r'<form method="post"(.*?)</form>',str(r.get('https://mbasic.facebook.com/device', cookies={'cookie':cookie}).text.replace('\\','').replace('amp;',''))).group(1)
    p1 = r.post('https://mbasic.facebook.com'+re.search(r'action="(.*?)"',str(f1)).group(1), data={**{i[0]:i[1] for i in re.findall(r'name="(.*?)" value="(.*?)"',str(f1))}, **{'user_code':r1['user_code']}}, cookies={'cookie':cookie}).text.replace('\\','').replace('amp;','')
    f2 = re.search(r'<form method="post"(.*?)</form>',str(p1)).group(1)
    p2 = r.post('https://mbasic.facebook.com'+re.search(r'action="(.*?)"',str(f2)).group(1), data={'fb_dtsg':re.search(r'name="fb_dtsg" value="(.*?)"',str(f2)).group(1), 'jazoest':re.search(r'name="jazoest" value="(.*?)"',str(f2)).group(1), 'scope':re.search(r'name="scope" value="(.*?)"',str(f2)).group(1), 'display':re.search(r'name="display" value="(.*?)"',str(f2)).group(1), 'user_code':re.search(r'name="user_code" value="(.*?)"',str(f2)).group(1), 'logger_id':re.search(r'name="logger_id" value="(.*?)"',str(f2)).group(1), 'auth_type':re.search(r'name="auth_type" value="(.*?)"',str(f2)).group(1), 'encrypted_post_body':re.search(r'name="encrypted_post_body" value="(.*?)"',str(f2)).group(1), 'return_format[]':re.search(r'name="return_format\[\]" value="(.*?)"',str(f2)).group(1), 'sdk':'', 'sdk_version':'', 'domain':'', 'sso_device':'', 'state':'', 'auth_nonce':'', 'code_challenge':'', 'code_challenge_method':''}, cookies={'cookie':cookie}).text.replace('\\','').replace('amp;','')
    r3 = r.get('https://graph.facebook.com/v18.0/device/login_status?method=post&code={}&access_token=1174099472704185|0722a7d5b5a4ac06b11450f7114eb2e9'.format(r1['code'])).json()['access_token']
    return(r3)
def GetTokenEAAB(cookie):
    r = requests.Session()
    req1 = r.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cookie},allow_redirects=True).text
    nek1 = re.search(r'window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
    req2 = r.get(nek1,cookies={'cookie':cookie},allow_redirects=True).text
    tok  = re.search(r'accessToken="(.*?)"',str(req2)).group(1)
    return(tok)
def GetTokenEAAG(cookie):
    r = requests.Session()
    req = r.get('https://business.facebook.com/business_locations', cookies={'cookie':cookie})
    tok = re.search(r'(\["EAAG\w+)', req.text).group(1).replace('["','')
    return(tok)