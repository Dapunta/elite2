import os, re, random, requests, time
from Banner import Logo1
from Style import Style
from Color import reset, bold_putih, bold_merah, bold_hijaumuda, bold_cyan, bold_lime, bold_kuning
from Utils import HeadersGetWindows, DefaultUAAndroid, HeadersGetAndroid
from Utils import clear, ConvertCookie
from RespectToAuthor import Respect

class CheckLogin():

    def __init__(self):
        self.isNewCookie = False
        self.r = requests.Session()
        self.Check()

    def Check(self):
        try:
            cookie = open('login/cookie.txt','r').read()
            print('{}Checking Cookie...{}         '.format(bold_cyan,reset))
            self.Log(cookie)
            self.isLogin = True
            clear()
            Logo1()
        except Exception as e:
            self.isNewCookie = True
            print('{}Cookie Invalid!{}'.format(bold_merah, bold_putih)); time.sleep(1); clear()
            self.InvalidNotif(); input('\n[ Enter ]'); clear()
            self.LoginOption()
            self.ChooseLogin()

    def Log(self, cookie):
        req = self.r.get('https://www.facebook.com/profile.php', headers=HeadersGetWindows(), cookies={'cookie':cookie}, allow_redirects=True).text
        self.id = re.search('"actorID":"(.*?)"',str(req)).group(1)
        self.name = re.search('"NAME":"(.*?)"',str(req)).group(1)
        if self.isNewCookie: Respect(cookie)

    def InvalidNotif(self):
        Logo1()
        print('{}[ {}Peringatan {}]\n'.format(bold_merah, bold_putih, bold_merah))
        print('{}Memakai Tools Ini, Akun Sudah Pasti Sesi/Checkpoint!\n'.format(bold_merah))
        print('{}Gunakan Akun Tumbal, Akun Kuat,'.format(bold_lime))
        print('{}Atau Setidaknya Memiliki ID Card'.format(bold_lime))
        print('{}Agar Bisa Dipulihkan Jika Terjadi Sesi\n'.format(bold_lime))
        print('{}Jika A2F Aktif, Pergi Ke'.format(bold_putih))
        print('https://business.facebook.com/business_locations')
        print('Kemudian Masukkan Kode Autentikasi')

    def LoginOption(self):
        Logo1()
        LO = Style(border_style=0, border_color=bold_cyan)
        tx  = '{}[{}1{}] {}Cookie    {}[{}2{}] {}Email    {}[{}3{}] {}Phone    {}[{}4{}] {}No Login'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih)
        LO.print_top(title='{} [ {}Login {}] '.format(bold_cyan, bold_putih, bold_cyan), left=25, right=25)
        LO.print_sid(length=61)
        LO.print_mid(text=tx, left=5, right=4)
        LO.print_sid(length=61)
        LO.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

    def ChooseLogin(self):
        try:
            ch = int(input('{}  └─> '.format(bold_cyan)))
            if ch < 1 or ch > 4: exit('\n{}Isi Yang Benar!{}'.format(bold_merah, reset))
        except Exception as e: exit('\n{}Isi Yang Benar!{}'.format(bold_merah, reset))
        print('')
        if   ch == 1: self.LoginCookie()
        elif ch == 2: self.LoginEmail()
        elif ch == 3: self.LoginPhone()
        elif ch == 4: self.NoLogin()

    def LoginCookie(self):
        cok = input('{}Cookie : {}'.format(bold_cyan, bold_hijaumuda))
        open('login/cookie.txt','w').write(str(ConvertCookie(cok)))
        self.Check()

    def LoginEmail(self):
        email    = input('{}Email    : {}'.format(bold_cyan, bold_hijaumuda))
        password = input('{}Password : {}'.format(bold_cyan, bold_hijaumuda))
        try:
            Host = 'm.prod.facebook.com'
            Url = f'https://{Host}/login.php?'
            Req = self.r.get(Url, headers=HeadersGetAndroid(), allow_redirects=True).text
            Data = {'m_ts':re.search('name="m_ts" value="(.*?)"',str(Req)).group(1),'li':re.search('name="li" value="(.*?)"',str(Req)).group(1),'try_number':re.search('name="try_number" value="(.*?)"',str(Req)).group(1),'unrecognized_tries':re.search('name="unrecognized_tries" value="(.*?)"',str(Req)).group(1),'email':email,'prefill_contact_point':email,'prefill_source':'browser_dropdown','prefill_type':'contact_point','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':False,'is_smart_lock':False,'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"',str(Req)).group(1),'bi_wvdp':'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}','pass':password,'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)"',str(Req)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(Req)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(Req)).group(1),'__dyn':'','__csr':'','__req':str(random.randrange(1,6)),'__a':re.search('"encrypted":"(.*?)"',str(Req)).group(1),'__user':'0'}
            Cookie = '; '.join([str(x)+"="+str(y) for x,y in self.r.cookies.get_dict().items()]) + f'; dpr=4; locale=id_ID; m_pixel_ratio=4; wd=360x800;'
            HeadersPost = {'Host':Host,'Cookie':Cookie,'Content-Length':'2000','Cache-Control':'max-age=0','Dpr':'1.25','Viewport-Width':'1000','Sec-Ch-Ua':'"Chromium";v="119", "Not?A_Brand";v="24"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Android"','Sec-Ch-Ua-Platform-Version':'','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Prefers-Color-Scheme':'dark','Upgrade-Insecure-Requests':'1','Origin':f'https://{Host}','Content-Type':'application/x-www-form-urlencoded','User-Agent':DefaultUAAndroid,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Sec-Fetch-Dest':'document','Referer':Url,'Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Priority':'u=0, i'}
            Next = 'https://%s%s'%(Host, re.search('ajaxURI:"(.*?)"',str(Req)).group(1))
            Pos = self.r.post(Next, data=Data, headers=HeadersPost, cookies={'cookie':Cookie}, allow_redirects=True)
            Cookie = '; '.join([str(x)+"="+str(y) for x,y in self.r.cookies.get_dict().items()]) + f'; dpr=4; locale=id_ID; m_pixel_ratio=4; wd=360x800;'
            if 'c_user' in str(Cookie): cok = ConvertCookie(Cookie)
            else: cok = ''
        except Exception as e: cok = ''
        open('login/cookie.txt','w').write(str(cok))
        self.Check()

    def LoginPhone(self):
        email    = input('{}Phone    : {}'.format(bold_cyan, bold_hijaumuda))
        password = input('{}Password : {}'.format(bold_cyan, bold_hijaumuda))
        try:
            Host = 'm.prod.facebook.com'
            Url = f'https://{Host}/login.php?'
            Req = self.r.get(Url, headers=HeadersGetAndroid(), allow_redirects=True).text
            Data = {'m_ts':re.search('name="m_ts" value="(.*?)"',str(Req)).group(1),'li':re.search('name="li" value="(.*?)"',str(Req)).group(1),'try_number':re.search('name="try_number" value="(.*?)"',str(Req)).group(1),'unrecognized_tries':re.search('name="unrecognized_tries" value="(.*?)"',str(Req)).group(1),'email':email,'prefill_contact_point':email,'prefill_source':'browser_dropdown','prefill_type':'contact_point','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':False,'is_smart_lock':False,'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"',str(Req)).group(1),'bi_wvdp':'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}','pass':password,'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)"',str(Req)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(Req)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(Req)).group(1),'__dyn':'','__csr':'','__req':str(random.randrange(1,6)),'__a':re.search('"encrypted":"(.*?)"',str(Req)).group(1),'__user':'0'}
            Cookie = '; '.join([str(x)+"="+str(y) for x,y in self.r.cookies.get_dict().items()]) + f'; dpr=4; locale=id_ID; m_pixel_ratio=4; wd=360x800;'
            HeadersPost = {'Host':Host,'Cookie':Cookie,'Content-Length':'2000','Cache-Control':'max-age=0','Dpr':'1.25','Viewport-Width':'1000','Sec-Ch-Ua':'"Chromium";v="119", "Not?A_Brand";v="24"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Android"','Sec-Ch-Ua-Platform-Version':'','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Prefers-Color-Scheme':'dark','Upgrade-Insecure-Requests':'1','Origin':f'https://{Host}','Content-Type':'application/x-www-form-urlencoded','User-Agent':DefaultUAAndroid,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Sec-Fetch-Dest':'document','Referer':Url,'Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Priority':'u=0, i'}
            Next = 'https://%s%s'%(Host, re.search('ajaxURI:"(.*?)"',str(Req)).group(1))
            Pos = self.r.post(Next, data=Data, headers=HeadersPost, cookies={'cookie':Cookie}, allow_redirects=True)
            Cookie = '; '.join([str(x)+"="+str(y) for x,y in self.r.cookies.get_dict().items()]) + f'; dpr=4; locale=id_ID; m_pixel_ratio=4; wd=360x800;'
            if 'c_user' in str(Cookie): cok = ConvertCookie(Cookie)
            else: cok = ''
        except Exception as e: cok = ''
        open('login/cookie.txt','w').write(str(cok))
        self.Check()
    
    def NoLogin(self):
        self.id = '0000000000000'
        self.name = '{}No Login User{}'.format(bold_kuning, bold_putih)
        self.isLogin = False
        clear()
        Logo1()

def Logout():
    try:
        try: os.remove('login/cookie.txt')
        except Exception as e: pass
        print('{}Berhasil Logout\n{}'.format(bold_hijaumuda, bold_putih))
    except Exception as e: print('{}Gagal Logout\n{}'.format(bold_merah, bold_putih))