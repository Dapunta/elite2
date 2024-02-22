from itertools import zip_longest
from Color import bold_putih, bold_cyan, bold_lime, bold_merah, bold_kuning, reset
from Style import Style, DoublePanel

def Logo1():
    print('{}___________ {}__   __  __        {} ________{}'.format(bold_cyan,bold_lime,bold_cyan,bold_lime))
    print('{}\\_   ___{}__/|  | |__|/  |{}_  ____ \\____{}_  \\  {}Facebook Brute Force'.format(bold_cyan,bold_lime,bold_cyan,bold_lime,bold_cyan))
    print('{} |    {}__)_ |  | |  \\ {}  __\\/ __ \\ {}/  ____/    By Dapunta Ratya  '.format(bold_cyan,bold_lime,bold_cyan,bold_lime))
    print('{} |  {}      \\|  |_{}|  ||  | \\  __{}_//       \\ '.format(bold_cyan,bold_lime,bold_cyan,bold_lime))
    print('{}/_{}________/|_{}___/__||__|  \\{}_____>________\\      {}v 2.0 2024{}\n'.format(bold_cyan,bold_lime,bold_cyan,bold_lime,bold_cyan,reset))

def Choose():
    try: ch = int(input('{}  └─> '.format(bold_cyan)))
    except Exception as e: ch = -1
    print('%s'%(bold_putih),end='')
    return(ch)

def UserPanel(user_id='Unknown', user_name='Unknown', account_id='Unknown', account_name='Unknown', status='{}Tester'.format(bold_merah), ip='Unknown'):
    user_id      = '{}ID   : {}{}'.format(bold_putih, bold_putih, user_id)
    user_name    = '{}Name : {}{}'.format(bold_putih, bold_putih, user_name)
    account_id   = '{}ID   : {}{}'.format(bold_putih, bold_putih, account_id)
    account_name = '{}Name : {}'.format(bold_putih, account_name)
    status       = '{}Stat : {}'.format(bold_putih, status)
    ip           = '{}IP   : {}'.format(bold_putih, ip)
    UP = DoublePanel(border_style=0, border_color=bold_cyan, space=2, padding=3, length_1=28, length_2=29)
    UP.print_top(left_1=9, right_1=9, left_2=8, right_2=8, title1=' {}[ {}User {}] '.format(bold_cyan, bold_putih, bold_cyan), title2=' {}[ {}Account {}] '.format(bold_cyan, bold_putih, bold_cyan))
    UP.print_sid()
    UP.print_mid(text1=user_id, text2=account_id)
    UP.print_mid(text1=user_name, text2=account_name)
    UP.print_mid(text1=status, text2=ip)
    UP.print_sid()
    UP.print_bot(left_1=14, right_1=14, left_2=15, right_2=14)

def MainMenu():
    MM = Style(border_style=0, border_color=bold_cyan)
    tx1 = '{}[{}1{}] {}Dump     {}[{}3{}] {}Bot       {}[{}5{}] {}License    {}[{}0{}] Logout{}'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih)
    tx2 = '{}[{}2{}] {}Crack    {}[{}4{}] {}Result    {}[{}6{}] {}Setting'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih)
    MM.print_top(title='{} [ {}Menu {}] '.format(bold_cyan, bold_putih, bold_cyan), left=25, right=26)
    MM.print_sid(length=61)
    MM.print_mid(text=tx1, left=5, right=4)
    MM.print_mid(text=tx2, left=5, right=18)
    MM.print_sid(length=61)
    MM.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

def MenuDump(isLogin):
    if isLogin: clr = bold_cyan
    else: clr = bold_merah
    belum_jadi = bold_merah
    MD = Style(border_style=0, border_color=bold_cyan)
    tx1 = '{}[{}1{}] {}Email    {}[{}3{}] {}Friend    {}[{}5{}] {}Name    {}[{}7{}] {}Followers'.format(belum_jadi, bold_putih, belum_jadi, bold_putih, clr, bold_putih, clr, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, clr, bold_putih, clr, bold_putih)
    tx2 = '{}[{}2{}] {}Phone    {}[{}4{}] {}Group     {}[{}6{}] {}Post    {}[{}8{}] {}Random ID'.format(belum_jadi, bold_putih, belum_jadi, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, clr, bold_putih, clr, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih)
    MD.print_top(title='{} [ {}Dump {}] '.format(bold_cyan, bold_putih, bold_cyan), left=25, right=26)
    MD.print_sid(length=61)
    MD.print_mid(text=tx1, left=5, right=4)
    MD.print_mid(text=tx2, left=5, right=4)
    MD.print_sid(length=61)
    MD.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

def MenuMethode():
    MD = Style(border_style=0, border_color=bold_cyan)
    tx1 = '{}[{}1{}] {}Api            {}[{}3{}] {}Async        {}[{}5{}] {}Wbloks'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih)
    tx2 = '{}[{}2{}] {}Validate       {}[{}4{}] {}Regular'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih)
    MD.print_top(title='{} [ {}Crack {}] '.format(bold_cyan, bold_putih, bold_cyan), left=25, right=25)
    MD.print_sid(length=61)
    MD.print_mid(text=tx1, left=7, right=8)
    MD.print_mid(text=tx2, left=7, right=24)
    MD.print_sid(length=61)
    MD.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

def MenuSettings():
    MD = Style(border_style=0, border_color=bold_cyan)
    tx1 = '{}[{}1{}] {}User Agent          {}[{}2{}] {}File Manager'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih)
    MD.print_top(title='{} [ {}Settings {}] '.format(bold_cyan, bold_putih, bold_cyan), left=23, right=24)
    MD.print_sid(length=61)
    MD.print_mid(text=tx1, left=11, right=10)
    MD.print_sid(length=61)
    MD.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

def MenuSettingsUserAgent():
    MD = Style(border_style=0, border_color=bold_cyan)
    tx1 = '{}[{}1{}] {}Ganti    {}[{}2{}] {}Tambah    {}[{}3{}] {}Check    {}[{}4{}] {}Device'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih)
    MD.print_top(title='{} [ {}User Agent {}] '.format(bold_cyan, bold_putih, bold_cyan), left=22, right=23)
    MD.print_sid(length=61)
    MD.print_mid(text=tx1, left=6, right=5)
    MD.print_sid(length=61)
    MD.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

def MenuSettingsFileManager():
    MD = Style(border_style=0, border_color=bold_cyan)
    tx1 = '{}[{}1{}] {}File Dump    {}[{}2{}] {}File Result     {}[{}3{}] {}File Lain'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih)
    MD.print_top(title='{} [ {}File Manager {}] '.format(bold_cyan, bold_putih, bold_cyan), left=21, right=22)
    MD.print_sid(length=61)
    MD.print_mid(text=tx1, left=5, right=6)
    MD.print_sid(length=61)
    MD.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

def MenuOpsiFileManager():
    MD = Style(border_style=0, border_color=bold_cyan)
    tx1 = '{}[{}1{}] {}Check        {}[{}2{}] {}Hapus        {}[{}3{}] {}Gabung'.format(bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_merah, bold_putih, bold_merah, bold_putih)
    MD.print_top(title='{} [ {}Opsi File {}] '.format(bold_cyan, bold_putih, bold_cyan), left=23, right=23)
    MD.print_sid(length=61)
    MD.print_mid(text=tx1, left=9, right=8)
    MD.print_sid(length=61)
    MD.print_bot(title='{} [ {}Pilih {}] '.format(bold_cyan, bold_putih, bold_cyan), right=50)

def ShowFileResult(x, y):
    UP = DoublePanel(border_style=0, border_color=bold_cyan, space=1, padding=3, length_1=29, length_2=29)
    UP.print_top(left_1=10, right_1=11, left_2=10, right_2=11, title1=' {}[ {}OK {}] '.format(bold_cyan, bold_putih, bold_cyan), title2=' {}[ {}CP {}] '.format(bold_cyan, bold_putih, bold_cyan))
    UP.print_sid()
    for a, b in zip_longest(x, y, fillvalue=''):
        try: i = '{}[{}{}{}] {}{}... {}[{}{} ID{}]{}'.format(bold_lime, bold_putih, a.split('|')[0], bold_lime, bold_putih, a.split('|')[2][:8], bold_lime, bold_putih, a.split('|')[3], bold_lime, bold_putih)
        except Exception as e: i = ''
        try: j = '{}[{}{}{}] {}{}... {}[{}{} ID{}]{}'.format(bold_kuning, bold_putih, b.split('|')[0], bold_kuning, bold_putih, b.split('|')[2][:8], bold_kuning, bold_putih, b.split('|')[3], bold_kuning, bold_putih)
        except Exception as e: j = ''
        UP.print_mid(text1=i, text2=j)
    UP.print_sid()
    UP.print_bot(left_1=15, right_1=14, left_2=15, right_2=14)

def Back():
    print('{}Proses Selesai, Kembali Ke Menu?'.format(bold_putih))
    input('\n{}[ {}Enter {}]{}'.format(bold_putih, bold_cyan, bold_putih, bold_putih))
    from Menu import Main
    from Utils import clear
    clear()
    Main()

def License():
    print('\n{}Fitur {}Premium {}Belum Tersedia Untuk Saat Ini'.format(bold_putih, bold_lime, bold_putih))
    print('{}Tunggu Update Selanjutnya Ya!\n'.format(bold_putih))

def BelumTersedia():
    print('{}Fitur Ini Belum Tersedia Untuk Saat Ini'.format(bold_putih))
    print('{}Tunggu Update Selanjutnya Ya!\n'.format(bold_putih))