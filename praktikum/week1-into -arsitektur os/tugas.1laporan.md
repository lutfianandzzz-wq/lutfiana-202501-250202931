#  Perbedaan monolithic karnel, mickrokarnel,dan layerd architecture:
## Monolithic karnel merupakan model arsitektur karnel yang menggabungkan seluruh fungsi utama sistem oprasi ke dalam satu ruang karnel(karnel space). kelebihan dan kekurangan:
## Kelebihan:
### a. performa sangat cepat karena tidak ada overhead komunikasi antar proses.
### B. Akses langsung terhadap sumber daya
## Kekurangan:
### a. kompleks dan sulit dipelihara          
###  B. jika terjadi Bug pada satu modul bisa menyebabkan seluruh sistem crash.
### C. Sulit untuk melakukan isolasi antar komponen.
## Microkarnel yaitu yang berusaha meminimalkan fungsi yang berjalan di dalam karnel. Kelebihan dan kekurangan:
## Kelebihan:
### A.stabilitas dan keamanan lebih tinggi karena kegagalan satu server tidak menjatuhkan karnel.
### B. Lebih mudah dikembangkan dan di uji.
### C. cocok untuk sistem real time.
## Kekurangan:
### A. Performa lebih lambat karena kebanyakan komunikasi antar proses.
### B. Desain lebi rumit dan memerlukan manajemen komunikasi yang efisien.
## Layerd architecture yaitu yang membagi sistem oprasi menjadi beberapa lapisan yang terususun secara hierarki. lapisan terendah berinteraksi dengan perangkat keras,sementara lapisan tertinggi berinteraksi dengan aplikasi dan pengguna. Kelebihan dan kekurangan:
# Kelebihan:
### A. Struktur yang jelas dan rapi, memudahkan perancangan dan pemeliharaan.
### B.Memudahkan isolasi kesalahan karena tiap lapisan memiliki fungsi spesifik.
# Kekurangan:
### A. Performa dapat lebih lambat  karena permintaan harus melewati banyak lapisan. 
### B. Tidak selalu mudah untuk membagi sistem menjadi lapisan yang benar2 terpisah.
## Contoh sistem oprasi (Os):
# Microsoft Word ,macOs,Android,Chrome OS,IOS
## Sistem yang relevan Pada sistem modern,
### tidak ada satu model murni yang dominan. Banyak sistem menggunakan pendekatan hybrid, yang menggabungkan kelebihan dari beberapa model. Misalnya, Linux secara teknis adalah monolithic kernel, tetapi mendukung modul kernel yang dapat dimuat/dilepas secara dinamis, memberikan fleksibilitas layaknya microkernel. macOS menggunakan kernel XNU yang menggabungkan microkernel Mach dengan komponen BSD monolithic.
### Model microkernel menawarkan keandalan dan keamanan lebih tinggi, sangat cocok untuk sistem kritis seperti embedded system atau server dengan kebutuhan uptime tinggi. Namun, model monolithic tetap banyak dipakai karena performanya yang tinggi dan kematangan ekosistemnya.
### Secara keseluruhan, hybrid kernel yang mengambil elemen dari microkernel dan monolithic kernel adalah pendekatan paling relevan untuk sistem modern. Kombinasi modularitas, performa tinggi, dan stabilitas membuat model hybrid mendominasi pada OS besar seperti Windows NT, macOS, dan Linux.