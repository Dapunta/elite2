# Elite2 - Facebook Brute Force

[Elite2](https://github.com/Dapunta/elite2) adalah sebuah alat yang dikembangkan dengan bahasa pemrograman Python yang berfungsi untuk menebak kata sandi dan otomatisasi akun Facebook. Project ini merupakan pengembangan lanjutan dari [Elite1](https://github.com/Dapunta/elite)  
<br>
<img width="100%" height="auto" src="IMG/MenuElite2.jpg">

### Fitur Global
- [Dump](#fitur-dump) : Mengumpulkan ID, username, dan nama akun Facebook
- [Crack](#fitur-crack) : Menebak dan mencoba kata sandi terhadap akun Facebook
- Bot : Otomatisasi akun Facebook (belum tersedia)
- Result : Menampilkan akun hasil crack
- License : Membership untuk pemakaian tools ini (belum tersedia)
- Setting : Pengaturan, pengelolaan file, dll
- Logout : Keluar dari sesi login Facebook

### Fitur Dump
- Email : Generate email secara acak (belum tersedia)
- Phone : Generate nomor HP secara acak (belum tersedia)
- Friend : Mengumpulkan ID dari daftar pertemanan akun Facebook
- Group : Mengumpulkan ID dari anggota grup
- Name : Generate nama secara acak
- Post : Mengumpulkan ID dari reaksi dan komentar postingan
- Followers : Mengumpulkan ID dari daftar pengikut akun Facebook
- Random ID : Generate ID secara acak

### Fitur Crack
- API : Login API Facebook
- Validate : Login validasi kata sandi
- Async : Login terbaru, asinkronus Facebook
- Regular : Login standar, payload lama
- Wblock : Login aplikasi (belum tersedia, kemungkinan premium)

### Instalasi
- Windows ( Powershell, Cmd )  
Install [Git](https://git-scm.com/downloads) dan [Python](https://www.python.org/downloads/release/python-3122/) terlebih dahulu
    ```bash
    git clone --depth 1 https://github.com/Dapunta/elite2
    ```
- Linux ( Termux )  
Install [Termux](https://f-droid.org/repo/com.termux_118.apk) terlebih dahulu
    ```bash
    pkg update -y && pkg upgrade -y
    pkg install git python
    git clone --depth 1 https://github.com/Dapunta/elite2
    ```
- Run
    ```bash
    cd elite2
    git pull
    pip install -r requirements.txt
    python run.py
    ```

### Informasi
- Author : [**Dapunta Khurayra X**](https://web.facebook.com/Dapunta.Khurayra.X)
- Release : 01/01/2024
- Last Update : 24/01/2024
- Version : 2.0.0 ( Test Version )

### Peringatan
Segala bentuk kerugian yang disebabkan oleh alat ini, adalah murni **tanggung jawab user**, bukan tanggung jawab Author, terima kasih.