Version = 2.0
Python = 3.12

import os, sys, Menu
from Utils import clear, requirements_module, create_directory

if __name__ == '__main__':
    clear()
    if (sys.version_info.major!=3) or (sys.version_info.minor<=10):
        print('Anda Menggunakan Python Versi {}'.format(str(sys.version).split(' ')[0]))
        print('Versi Tersebut Terlalu Lama Untuk Menjalankan Tools Ini')
        print('Anda Harus Meng-Update Versi Python Ke 3.12 Terlebih Dahulu\n')
        exit()
    if os.get_terminal_size().columns < 63:
        print('Perkecil Layar Anda Agar Tampilan Tidak Berantakan!')
        print("Lakukan 'Zoom Out' Atau 'Cubit' Pada Layar Perangkat Anda")
        print('-'*63)
        print('')
        exit()
    requirements_module()
    create_directory()
    Menu.Main()