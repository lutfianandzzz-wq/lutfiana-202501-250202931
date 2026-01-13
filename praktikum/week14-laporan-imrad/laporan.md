
# Laporan Praktikum Minggu [14]
Topik: [Penyusunan Laporan Praktikum Format IMRAD]

---

## Identitas
- **Nama**  : [Asyifani Lutfiana Nadzif]  
- **NIM**   : [250202931]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
>1. Menyusun laporan praktikum dengan struktur ilmiah (Pendahuluan–Metode–Hasil–Pembahasan–Kesimpulan).
>2. Menyajikan hasil uji dalam bentuk tabel dan/atau grafik yang jelas.
>3. Menuliskan analisis hasil dengan argumentasi yang logis.
>4. Menyusun sitasi dan daftar pustaka dengan format yang konsisten.
>5. Mengunggah draft laporan ke repositori dengan rapi dan tepat waktu.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Menentukan Topik Laporan**

   Pilih 1 topik dari praktikum sebelumnya (mis. Minggu 9/10/11/13) dan tetapkan tujuan eksperimen yang ingin disampaikan.

2. **Menyiapkan Bahan**

   - Kode/program yang digunakan.
   - Dataset/parameter uji (jika ada).
   - Bukti hasil eksekusi (screenshot) dan/atau grafik.

3. **Menulis Laporan dengan Struktur IMRAD**

   Tulis `praktikum/week14-laporan-imrad/laporan.md` dengan struktur minimal berikut:
   - **Pendahuluan (Introduction):** latar belakang, rumusan masalah/tujuan.
   - **Metode (Methods):** lingkungan uji, langkah eksperimen, parameter/dataset, cara pengukuran.
   - **Hasil (Results):** tabel/grafik hasil uji, ringkasan temuan.
   - **Pembahasan (Discussion):** interpretasi hasil, keterbatasan, perbandingan teori/ekspektasi.
   - **Kesimpulan:** 2–4 poin ringkas menjawab tujuan.

4. **Menyajikan Tabel/Grafik**

   - Tabel harus diberi judul/keterangan singkat.
   - Jika menggunakan grafik: jelaskan sumbu dan arti grafik.

5. **Sitasi dan Daftar Pustaka**

   - Cantumkan referensi minimal 2 sumber.
   - Gunakan format konsisten (mis. daftar bernomor).

6. **Commit & Push Draft**

   ```bash
   git add .
   git commit -m "Minggu 14 - Draft Laporan IMRAD"
   git push origin main
   ```


---

## Pendahuluan (Introduction)
### Latar Belakang
Perkembangan teknologi komputer mendorong penggunaan virtualisasi untuk meningkatkan efisiensi pemanfaatan perangkat keras. Virtualisasi memungkinkan satu komputer fisik menjalankan beberapa sistem operasi secara bersamaan tanpa saling mengganggu. Salah satu bentuk virtualisasi yang banyak digunakan adalah Virtual Machine (VM).
Virtual Machine bekerja dengan bantuan perangkat lunak yang disebut hypervisor, yang bertugas mengelola dan membagi sumber daya seperti CPU, memori, dan penyimpanan kepada setiap sistem operasi guest. Teknologi ini banyak dimanfaatkan dalam bidang pendidikan, pengujian sistem operasi, serta simulasi lingkungan kerja. Oleh karena itu, pemahaman mengenai konsep Virtual Machine dan pengaruh alokasi resource terhadap kinerjanya menjadi hal yang penting.

### Rumusan Masalah
1. Berdasarkan latar belakang tersebut, rumusan masalah dalam praktikum ini adalah:
2. Bagaimana cara menginstal dan menjalankan sistem operasi guest menggunakan Virtual Machine?
3. Bagaimana pengaruh alokasi CPU dan RAM terhadap kinerja Virtual Machine?
4. Bagaimana Virtual Machine menyediakan isolasi antara sistem host dan guest?
   
### Tujuan
Tujuan dari praktikum ini adalah:
1. Memahami konsep dasar virtualisasi menggunakan Virtual Machine.
2. Menginstal dan menjalankan sistem operasi guest pada lingkungan Virtual Machine.
3. Menganalisis pengaruh pengaturan CPU dan RAM terhadap performa Virtual Machine.
4. Mengetahui peran Virtual Machine dalam menyediakan isolasi dan keamanan sistem.

## Metode (Methods)
### Lingkungan Uji
Praktikum virtualisasi ini dilakukan menggunakan lingkungan pengujian sebagai berikut:
- Sistem Operasi Host : Windows 10 64-bit
- Perangkat Lunak Virtualisasi : Oracle VirtualBox 7.2.4
- Sistem Operasi Guest : Ubuntu Linux 24.04 (64-bit)
- File ISO : ubuntu-24.04-desktop-amd64.iso
- Spesifikasi Host : RAM 16 GB

Lingkungan uji ini digunakan untuk memastikan Virtual Machine dapat berjalan dengan stabil serta memungkinkan pengujian pengaruh alokasi resource terhadap performa sistem operasi guest.

### Langkah Eksperimen
Langkah-langkah eksperimen yang dilakukan dalam praktikum ini adalah sebagai berikut:
1. Menginstal Oracle VirtualBox pada sistem operasi host.
2. Mengaktifkan fitur virtualisasi (VT-x/AMD-V) pada BIOS jika diperlukan.
3. Membuat Virtual Machine baru dan memilih sistem operasi guest Ubuntu Linux.
4. Mengatur konfigurasi awal VM, meliputi alokasi CPU, RAM, dan kapasitas penyimpanan.
5. Melakukan instalasi sistem operasi Ubuntu Linux menggunakan file ISO.
6. Menjalankan VM dan memastikan sistem operasi guest dapat digunakan dengan normal.
7. Melakukan pengujian performa dengan menjalankan aplikasi di dalam VM.
8. Mengubah konfigurasi resource VM dan melakukan pengujian ulang.

### Parameter / Dataset
Parameter yang digunakan dalam praktikum ini berupa konfigurasi resource Virtual Machine dengan dua skenario pengujian, yaitu:

- Skenario 1 (Normal) :
    - RAM : 4 GB
    - CPU : 2 Core

- Skenario 2 (Rendah) :
    - RAM : 2 GB
    - CPU : 1 Core

Dataset pengujian berupa aktivitas penggunaan aplikasi, yaitu membuka beberapa tab browser Firefox (YouTube dan E-learning) di dalam sistem operasi guest.

### Cara Pengukuran

Pengukuran performa Virtual Machine dilakukan dengan cara:
- Mengamati penggunaan memori menggunakan perintah free -h.
- Mengamati kondisi sistem melalui System Monitor pada Ubuntu.
- Menilai respons sistem berdasarkan kelancaran saat membuka dan menjalankan aplikasi.

## Hasil (Results)
### Tabel Hasil Pengujian
| Skenario Pengujian | RAM | CPU | Beban Uji | Penggunaan Memori | Kondisi Sistem |
|------------------|-----|-----|-----------|-------------------|----------------|
| Normal | 4 GB | 2 Core | Membuka 5 tab Firefox (YouTube & E-learning) | ±90–95% (±3.8 GB) | Sistem berjalan lancar dan responsif |
| Rendah | 2 GB | 1 Core | Membuka 3–5 tab Firefox | ±95–97% (±2.0 GB) | Sistem lambat, Firefox sering tidak merespons |

### Ringkasan Temuan
- Pada konfigurasi RAM 4 GB, penggunaan memori mencapai lebih dari 90% namun sistem tetap responsif.
- Pada konfigurasi RAM 2 GB, sistem mengalami lag dan penurunan performa secara signifikan.

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/os_guest_running.png)
 ![Screenshot hasil](./screenshots/konfigurasi_resource.png)
 ![Screenshot hasil](./screenshots/os_guest_running.png)
 ![Screenshot hasil](./screenshots/firefox.png)

## Pembahasan (Discussion)
### Interpretasi Hasil
Berdasarkan hasil pengujian, terlihat bahwa alokasi resource, khususnya RAM dan CPU, sangat memengaruhi kinerja Virtual Machine. Pada skenario normal dengan RAM 4 GB dan CPU 2 core, sistem operasi Ubuntu dapat berjalan dengan lancar meskipun penggunaan memori mencapai lebih dari 90%. Hal ini menunjukkan bahwa alokasi resource yang cukup mampu mendukung aktivitas multitasking pada VM.
Sebaliknya, pada skenario rendah dengan RAM 2 GB dan CPU 1 core, performa sistem mengalami penurunan yang signifikan. Sistem menjadi lambat dan aplikasi sering mengalami kondisi tidak merespons (not responding) akibat keterbatasan memori. Kondisi ini menunjukkan bahwa resource yang tidak mencukupi dapat menghambat kinerja sistem operasi guest.

### Keterbatasan Praktikum
Keterbatasan dalam praktikum ini adalah pengujian hanya dilakukan menggunakan satu jenis sistem operasi guest dan satu jenis aplikasi uji, yaitu browser Firefox. Selain itu, pengujian performa dilakukan secara observasi tanpa menggunakan alat benchmarking khusus, sehingga hasil bersifat deskriptif.

### Perbandingan dengan Teori / Ekspektasi
Hasil praktikum ini sesuai dengan teori virtualisasi yang menyatakan bahwa Virtual Machine membutuhkan alokasi resource yang memadai agar dapat berjalan optimal. Secara teori, VM memiliki overhead lebih besar dibandingkan container karena menjalankan sistem operasi lengkap. Oleh karena itu, ketika resource dibatasi, penurunan performa pada VM merupakan hal yang sesuai dengan ekspektasi.

---

## Kesimpulan
1. Virtual Machine memungkinkan satu komputer fisik menjalankan sistem operasi guest secara terisolasi.
2. Alokasi CPU dan RAM sangat berpengaruh terhadap performa Virtual Machine.
3. Konfigurasi resource yang sesuai kebutuhan menghasilkan sistem yang stabil dan responsif.
4. Pembatasan resource yang terlalu rendah menyebabkan penurunan performa secara signifikan.

## Daftar Pustaka

Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts. Wiley.

Tanenbaum, A. S., & Bos, H. (2015). Modern Operating Systems. Pearson.

---

## Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi? 
   **Jawaban:**  
Format IMRAD membuat laporan tersusun rapi dan sistematis, mulai dari tujuan, metode, hasil, hingga pembahasan. Dengan struktur ini, pembaca dan dosen lebih mudah memahami proses praktikum dan menilai hasil yang diperoleh.
2. Apa perbedaan antara bagian Hasil dan Pembahasan?
   **Jawaban:**  
 Bagian Hasil berisi data atau output dari praktikum, seperti tabel dan gambar, tanpa penjelasan panjang. Sedangkan bagian Pembahasan berisi penjelasan dan analisis terhadap hasil tersebut serta kaitannya dengan teori.
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?
   **Jawaban:**  
Sitasi dan daftar pustaka penting untuk menunjukkan sumber teori yang digunakan serta menghindari plagiarisme. Selain itu, referensi membantu memperkuat keilmiahan laporan praktikum.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
