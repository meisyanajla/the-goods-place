# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
**Nama**: Meisya Najla Aqilah
**NPM**: 2306209870
**Kelas**: PBP C
**Link Deploy**: http://meisya-najla-thegoodsplace.pbp.cs.ui.ac.id/

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Checklist tersebut diimplementasikan dengan cara-cara berikut.
1. **Membuat sebuah proyek Django baru**
Pertama, saya membuat direktori lokal dengan nama the-goods-place. Setelah itu, saya membuat virtual environment pada direktori tersebut dengan tujuan agar pengembangan aplikasi yang saya ingin buat terisolasi. Selanjutnya, dalam direktori lokal the-goods-place, saya membuat berkas requirements.txt, yang kemudian saya instalasikan. Setelah terinstalasi, saya membuat proyek Django dengan nama the_goods_place serta membuat kerangka dasar dari proyek Django tersebut.
2. **Membuat aplikasi dengan nama `main` pada proyek tersebut**
Kedua, saya membuat aplikasi baru dengan nama main dalam direktori the-goods-place. Selanjutnya, saya mendaftarkan ‘main’ pada variabel INSTALLED_APPS dalam berkas setting.py.
3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`**
Ketiga, saya membuat berkas urls.py dalam direktori ‘main’ dan menambahkan main.urls pada berkas urls.py pada direktori the_goods_place agar dapat menampilkan ‘main’ ketika URL diakses.
4. **Membuat model pada aplikasi `main` dengan nama Product dan memiliki atribut wajib seperti `name`, `price`, dan `description`**
Keempat, saya membuka berkas models.py dalam direktori aplikasi ‘main’ dan mengubah isi berkas tersebut sesuai ketentuan yang saya inginkan. Setelah itu, saya mengaplikasikan migrasi models untuk melakukan migrasi ke dalam database lokal.
5. **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**
Kelima, saya membuka berkas views.py dlaam direktori aplikasi ‘main’ dan menambahkan import render serta mengatur fungsi show_main sesuai ketentuan yang saya inginkan. Selanjutnya, saya memodifikasi kembali main.htlm yang berada di dalam direktori templates agar menyesuaikan dengan data yang ingin ditampilkan.
6. **Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`**
Keenam, saya kembali membuka berkas urls.py dalam direktori ‘main’ dan menambahkan main.urls pada berkas urls.py pada direktori the_goods_place agar dapat menampilkan ‘main’ ketika URL diakses.

# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
**Link**: https://drive.google.com/file/d/1i7m_kwbv4uCEKAWM8tZ7W3-O8Fn1p2bD/view?usp=sharing

# Jelaskan fungsi git dalam pengembangan perangkat lunak!
Fungsi git dalam pengembangan perangkat lunak adalah sebagai sistem kontrol untuk mengembangkan, mengelola, dan melacak perubahan kode secara terstuktur, aman, dan kolaboratif.
1. Git memungkinan user untuk bekerja pada fitur baru maupun berbaikan dalam branch terpisah sehingga user dapat berkolaborasi dengan tim tanpa mempengaruhi pekerjaan user lainnya.
2. Git membantu dalam pengaturan dan penggabungan perubahan yang dibuat oleh berbagai anggota tim dengan menjaga kode tetap terstruktur.
3. Git mencatat semua perubahan yang dibuat pada kode demi memudahkan user untuk melihat riwayat perubahan, apa yang telah diubah, dan kapan perubahan itu terjadi.

# Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Framework Django dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena  beberapa alasan berikut.
1. Django menggunakan bahasa pemrograman Python yang lebih mudah dipahami oleh pemula.
2. Django menerapkan pola struktur Model-View-Template (MVT) yang memudahkan pengguna untuk lebih memahami alur pengembangan strukturnya.
3. Django memiliki dokumentasi yang sangat lengkap dan lebih dimengerti sehingga memudahkan proses pembelajaran bagi pemula. 

# Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai Object-Relational Mapping (ORM) karena memiliki peran dalam memetakan objek dalam kode Python ke dalam tabel pada struktur database regional tanpa perlu melibatkan query SQL secara langsung.