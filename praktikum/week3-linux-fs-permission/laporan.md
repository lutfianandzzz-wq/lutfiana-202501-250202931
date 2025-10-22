
# Laporan Praktikum Minggu [3]
Topik: [Manajemen File dan Permission di Linux]

---

## Identitas
- **Nama**  : [Asyifani Lutfiana Nadzif]  
- **NIM**   : [250202931]  
- **Kelas** : [1ikrb]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini: 
1.  Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
2. Menggunakan chmod dan chown untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.

---

## Dasar Teori
Manajemen file dan permission di Linux berfungsi untuk mengatur cara penyimpanan, akses, serta keamanan file di dalam sistem. Dengan adanya sistem izin (read, write, execute) yang diterapkan untuk setiap pengguna, Linux mampu menjaga integritas dan keamanan data antar user dalam lingkungan multi-user.
 > **Permission(Hak Akses File)**
 - Read (r) yaitu boleh membaca isi file
 - Write(w) yaitu boleh mengubah isi file
 - Execute (x) yaitu boleh menjalankan file(jika executable)
> Tujuan Manajemen File dan permission:
1. Menjamin keamanan data antar pengguna.
2. Menghindari akses ilegal terhadap file penting sistem.
3. Memungkinkan pembagian sumber daya secara efisien.
4. Menjaga integritas sistem operasi agar stabil.

---

## Langkah Praktikum
1. Persiapkan Aplikasi Linux (Ubuntu/WSL)
2. Melakukan **Eksperimen 1** untuk melihat dan menavigasi sistem file menggunakan  ``pwd``, ``ls -l``, ``cd /tmp ``, ``ls -a``
3. Melakukan **Eksperimen 2** berfungsi untuk membaca file dan hanya menampilkan lima baris pertama ``cat ``/``etc``/``passwd`` | ``head -n 5``  
4. Melakukan **Eksperimen 3** untuk memanipulasi izin dan kepemilikan file menggunakan `` echo``, ``chmod``, dan ``sudo chown``
5. Screenshot  dari hasil eksperimen  1 sampai 3 dan disimpan di folder ``screenshot/.``
6. Mendokumentasikan seluruh hasil dan analisis dalam file ``laporan.md``
7. Lalu ``push`` hasil praktikum di Github dengan pesan commit yang sesuai.

---

## Kode / Perintah
Eksprimen 1
```
pwd
ls -l
cd /tmp
ls -a
```

Eksperimen 2
```
cat /etc/passwd | head -n 5
```

Eksperimen 3 
```
cd
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
sudo chown root percobaan.txt
ls -l percobaan.txt
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/linux_fs.png)

# Eksperimen 1 pwd,ls -l,cd /tmp,ls -a
| Perintah | Hasil Output | Keterangan |
|:---|:---|:---|
|``pwd``| ``/home/lutfiana`` |untuk menampilkan jalur lengkapdari direktori kerja saat ini|
|``ls -l``| ``drwxr-xr-x 2 lutfiana 4096 Oct 17 16:27 praktikum-week-3``| yaitu tampilan daftar panjang dari file dan direktori di direktori kerja saat ini.|
| ``cd/tmp`` | Tidak ada output | digunakan untuk mengubah deriktori aktif.|
| ``ls -a``| menampilkan file ``systemd-private...,unix,dll``|berfungsi untuk mendaftar semua file dan direktori di direktori kerja saat ini, termasuk yang tersembunyi.|

# Eksperimen 2 cat /etc/passwd | head -n 5
|Perintah | Keterangan|
|:---|:---|
|``cd``| mengembalikan direktori ke awal|
|cat| perintah yang digunakan untuk membaca isi file dan menampilkannya ke output standar.|
|``/etc/passwd``|file konfigurasi sistem penting yang berisi informasi tentang semua akun|
| `` head -n 5``| menampilkan baris awal (head) dari input yang diterimanya dan menentukan bahwa hanya 5 baris pertama yang harus ditampilkan.

# Eksperimen 3 

`` echo "Hello Asyifani Lutfiana Nadzif - 250202931" > percobaan.txt``
- perintah ini berfungsi untuk membuat file baru menuliskan string teks di dalamnya.
  
``ls -l percobaan.txt``
|Kode permission | Keterangan|
|:---|:---|
|``rw-``| izin baca dan tulis|
|``rw--``|izin baca|

``chmod 600 percobaan.txt``
- Perintah ini digunakan untuk mengubah hak akses menggunakan notasi numerik.
  
``ls -l percobaan.txt``
|Kode permission | Keterangan |
|:---|:---|
|``rw-``| memiliki izin baca dan tulis|
|``---``| tidak memiliki izin|


``sudo chown root percobaan.txt``
- Perintah ini digunakan untuk mengubah kepemilikan
  
``ls -l percobaan.txt``
- Perintah ini menampilkan detail lengkap (long listing format) dari file untuk memverifikasi perubahan.

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
