import os, sys
from Color import reset, bold_putih

def clear(): os.system('cls' if 'win' in sys.platform.lower() else 'clear')

def GetBorderStyle(border_style):
        list_border = [
            ['─','│','╭','╮','╰','╯']
        ]
        return(list_border[border_style])

def GetLength(text):
    length = 0
    ansii  = 0
    in_ansii = False
    for i in text:
        if i == '\x1b' or i == '\033': ansii += 1; in_ansii = True
        elif in_ansii and i == 'm': ansii += 1; in_ansii = False
        elif in_ansii: ansii += 1
        elif not in_ansii: length += 1
    return (length, ansii)

def CutString(text, max):
    lgt, ans = GetLength(text)
    if len(str(text)) > max:
        if lgt > max: out = str(text)[:max+ans-3] + '...'
        else: out = str(text) + ' '*(max-lgt)
    else: out = str(text) + ' '*(max-ans-lgt)
    return(out)

class Style():

    def __init__(self, text_color=reset, border_color=reset, border_style=0, padding=0, align='center', margin_top=0, margin_bottom=0, margin_left=0, margin_right=0):

        self.text_color    = text_color
        self.border_color  = border_color
        self.border_style  = GetBorderStyle(border_style)
        self.padding       = padding
        self.align         = align
        self.margin_top    = margin_top
        self.margin_bottom = margin_bottom
        self.margin_left   = margin_left
        self.margin_right  = margin_right

    def print_top(self, title='', left=0, right=0, length=0):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        if title == '' and length != 0:   out = '{}{}{}{}'.format(self.border_color, atas_kiri, horizontal*(length), atas_kanan)
        elif title != '' and length == 0: out = '{}{}{}{}{}{}{}'.format(self.border_color, atas_kiri, horizontal*left, title, self.border_color, horizontal*right, atas_kanan)
        else: out = '{}Parametermu Salah Cok!'.format(reset)
        print(out)

    def print_sid(self, length=0):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        out = '{}{}{}{}'.format(self.border_color, vertikal, ' '*length ,vertikal)
        print(out)

    def print_mid(self, text='', left=0, right=0):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        out = '{}{}{}{}{}{}{}'.format(self.border_color, vertikal, ' '*left, text, self.border_color, ' '*right, vertikal)
        print(out)

    def print_bot(self, title='', left=0, right=0, length=0):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        if title == '' and length != 0:   out = '{}{}{}{}'.format(self.border_color, bawah_kiri, horizontal*(length), bawah_kanan)
        elif title != '' and length == 0: out = '{}{}{}{}{}{}{}'.format(self.border_color, bawah_kiri, horizontal*left, title, self.border_color, horizontal*right, bawah_kanan)
        else: out = '{}Parametermu Salah Cok!'.format(reset)
        print(out)

class DoublePanel():

    def __init__(self, border_color=reset, border_style=0, length=0, space=0, padding=0, length_1=28, length_2=29):
        self.border_color  = border_color
        self.border_style  = GetBorderStyle(border_style)
        self.length        = length
        self.length_1      = length_1
        self.length_2      = length_2
        self.space         = space
        self.padding       = padding

    def print_top(self, title1='', title2='', left_1=0, right_1=0, left_2=0, right_2=0):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        out = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(self.border_color, atas_kiri, horizontal*left_1, title1, self.border_color, horizontal*right_1, atas_kanan, ' '*self.space, atas_kiri, horizontal*left_2, title2, self.border_color, horizontal*right_2, atas_kanan)
        print(out)

    def print_sid(self):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        out = '{}{}{}{}{}{}{}{}'.format(self.border_color, vertikal, ' '*(self.length_1), vertikal, ' '*self.space, vertikal, ' '*(self.length_2), vertikal)
        print(out)

    def print_mid(self, text1='', text2=''):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        maxp1, maxp2 = self.length_1 - 2*self.padding, self.length_2 - 2*self.padding
        p1, p2 = CutString(text1, maxp1), CutString(text2, maxp2)
        out = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(self.border_color, vertikal, ' '*self.padding, p1, self.border_color, ' '*self.padding, vertikal, ' '*self.space, vertikal, ' '*self.padding, p2, self.border_color, ' '*self.padding, vertikal)
        print(out)

    def print_bot(self, title1='', title2='', left_1=0, right_1=0, left_2=0, right_2=0):
        horizontal, vertikal, atas_kiri, atas_kanan, bawah_kiri, bawah_kanan = self.border_style
        out = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(self.border_color, bawah_kiri, horizontal*left_1, title1, self.border_color, horizontal*right_1, bawah_kanan, ' '*self.space, bawah_kiri, horizontal*left_2, title2, self.border_color, horizontal*right_2, bawah_kanan)
        print(out)