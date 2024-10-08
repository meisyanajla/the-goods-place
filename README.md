# The Goods Place
**Nama**: Meisya Najla Aqilah <br />
**NPM**: 2306209870 <br />
**Kelas**: PBP C <br />
**Link Deploy**: http://meisya-najla-thegoodsplace.pbp.cs.ui.ac.id/

# Table of Contents
- [The Goods Place](#the-goods-place)
- [Table of Contents](#table-of-contents)
- [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](#tugas-2-implementasi-model-view-template-mvt-pada-django)
  - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step)
  - [Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.](#buatlah-bagan-yang-berisi-request-client-ke-web-aplikasi-berbasis-django-beserta-responnya-dan-jelaskan-pada-bagan-tersebut-kaitan-antara-urlspy-viewspy-modelspy-dan-berkas-html)
  - [Jelaskan fungsi git dalam pengembangan perangkat lunak!](#jelaskan-fungsi-git-dalam-pengembangan-perangkat-lunak)
  - [Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?](#menurut-anda-dari-semua-framework-yang-ada-mengapa-framework-django-dijadikan-permulaan-pembelajaran-pengembangan-perangkat-lunak)
  - [Mengapa model pada Django disebut sebagai ORM?](#mengapa-model-pada-django-disebut-sebagai-orm)
- [Tugas 3: Implementasi Form dan Data Delivery pada Django](#tugas-3-implementasi-form-dan-data-delivery-pada-django)
  - [Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?](#jelaskan-mengapa-kita-memerlukan-data-delivery-dalam-pengimplementasian-sebuah-platform)
  - [Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?](#menurutmu-mana-yang-lebih-baik-antara-xml-dan-json-mengapa-json-lebih-populer-dibandingkan-xml)
  - [Jelaskan fungsi dari method is\_valid() pada form Django dan mengapa kita membutuhkan method tersebut?](#jelaskan-fungsi-dari-method-is_valid-pada-form-django-dan-mengapa-kita-membutuhkan-method-tersebut)
  - [Mengapa kita membutuhkan csrf\_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf\_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?](#mengapa-kita-membutuhkan-csrf_token-saat-membuat-form-di-django-apa-yang-dapat-terjadi-jika-kita-tidak-menambahkan-csrf_token-pada-form-django-bagaimana-hal-tersebut-dapat-dimanfaatkan-oleh-penyerang)
  - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-1)
  - [Dokumentasi Postman](#dokumentasi-postman)
- [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django](#tugas-4-implementasi-autentikasi-session-dan-cookies-pada-django)
  - [Apa perbedaan antara HttpResponseRedirect() dan redirect()?](#apa-perbedaan-antara-httpresponseredirect-dan-redirect)
  - [Jelaskan cara kerja penghubungan model Product dengan User!](#jelaskan-cara-kerja-penghubungan-model-product-dengan-user)
  - [Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.](#apa-perbedaan-antara-authentication-dan-authorization-apakah-yang-dilakukan-saat-pengguna-login-jelaskan-bagaimana-django-mengimplementasikan-kedua-konsep-tersebut)
  - [Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?](#bagaimana-django-mengingat-pengguna-yang-telah-login-jelaskan-kegunaan-lain-dari-cookies-dan-apakah-semua-cookies-aman-digunakan)
  - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-2)
- [Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS](#tugas-5-desain-web-menggunakan-html-css-dan-framework-css)
  - [Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!](#jika-terdapat-beberapa-css-selector-untuk-suatu-elemen-html-jelaskan-urutan-prioritas-pengambilan-css-selector-tersebut)
  - [Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!](#mengapa-responsive-design-menjadi-konsep-yang-penting-dalam-pengembangan-aplikasi-web-berikan-contoh-aplikasi-yang-sudah-dan-belum-menerapkan-responsive-design)
  - [Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!](#jelaskan-perbedaan-antara-margin-border-dan-padding-serta-cara-untuk-mengimplementasikan-ketiga-hal-tersebut)
  - [Jelaskan konsep flex box dan grid layout beserta kegunaannya!](#jelaskan-konsep-flex-box-dan-grid-layout-beserta-kegunaannya)
  - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-3)
- [Tugas 6: JavaScript dan AJAX](#tugas-6-javascript-dan-ajax)
  - [Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!](#jelaskan-manfaat-dari-penggunaan-javascript-dalam-pengembangan-aplikasi-web)
  - [Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?](#jelaskan-fungsi-dari-penggunaan-await-ketika-kita-menggunakan-fetch-apa-yang-akan-terjadi-jika-kita-tidak-menggunakan-await)
  - [Mengapa kita perlu menggunakan decorator csrf\_exempt pada view yang akan digunakan untuk AJAX POST?](#mengapa-kita-perlu-menggunakan-decorator-csrf_exempt-pada-view-yang-akan-digunakan-untuk-ajax-post)
  - [Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?](#pada-tutorial-pbp-minggu-ini-pembersihan-data-input-pengguna-dilakukan-di-belakang-backend-juga-mengapa-hal-tersebut-tidak-dilakukan-di-frontend-saja)
  - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-4)


# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Checklist tersebut diimplementasikan dengan cara-cara berikut.
1. **Membuat sebuah proyek Django baru** <br />
Pertama, saya membuat direktori lokal dengan nama the-goods-place. Setelah itu, saya membuat virtual environment pada direktori tersebut dengan tujuan agar pengembangan aplikasi yang saya ingin buat terisolasi. Selanjutnya, dalam direktori lokal the-goods-place, saya membuat berkas requirements.txt, yang kemudian saya instalasikan. Setelah terinstalasi, saya membuat proyek Django dengan nama the_goods_place serta membuat kerangka dasar dari proyek Django tersebut.
2. **Membuat aplikasi dengan nama `main` pada proyek tersebut** <br />
Kedua, saya membuat aplikasi baru dengan nama main dalam direktori the-goods-place. Selanjutnya, saya mendaftarkan ‘main’ pada variabel INSTALLED_APPS dalam berkas setting.py.
3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`** <br />
Ketiga, saya membuat berkas urls.py dalam direktori ‘main’ dan menambahkan main.urls pada berkas urls.py pada direktori the_goods_place agar dapat menampilkan ‘main’ ketika URL diakses.
4. **Membuat model pada aplikasi `main` dengan nama Product dan memiliki atribut wajib seperti `name`, `price`, dan `description`** <br />
Keempat, saya membuka berkas models.py dalam direktori aplikasi ‘main’ dan mengubah isi berkas tersebut sesuai ketentuan yang saya inginkan. Setelah itu, saya mengaplikasikan migrasi models untuk melakukan migrasi ke dalam database lokal.
5. **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu** <br />
Kelima, saya membuka berkas views.py dlaam direktori aplikasi ‘main’ dan menambahkan import render serta mengatur fungsi show_main sesuai ketentuan yang saya inginkan. Selanjutnya, saya memodifikasi kembali main.htlm yang berada di dalam direktori templates agar menyesuaikan dengan data yang ingin ditampilkan.
6. **Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`** <br />
Keenam, saya kembali membuka berkas urls.py dalam direktori ‘main’ dan menambahkan main.urls pada berkas urls.py pada direktori the_goods_place agar dapat menampilkan ‘main’ ketika URL diakses.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
**Link**: https://drive.google.com/file/d/1i7m_kwbv4uCEKAWM8tZ7W3-O8Fn1p2bD/view?usp=sharing

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Fungsi git dalam pengembangan perangkat lunak adalah sebagai sistem kontrol untuk mengembangkan, mengelola, dan melacak perubahan kode secara terstuktur, aman, dan kolaboratif. 
1. Git memungkinan user untuk bekerja pada fitur baru maupun berbaikan dalam branch terpisah sehingga user dapat berkolaborasi dengan tim tanpa mempengaruhi pekerjaan user lainnya.
2. Git membantu dalam pengaturan dan penggabungan perubahan yang dibuat oleh berbagai anggota tim dengan menjaga kode tetap terstruktur.
3. Git mencatat semua perubahan yang dibuat pada kode demi memudahkan user untuk melihat riwayat perubahan, apa yang telah diubah, dan kapan perubahan itu terjadi.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Framework Django dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena  beberapa alasan berikut.
1. Django menggunakan bahasa pemrograman Python yang lebih mudah dipahami oleh pemula.
2. Django menerapkan pola struktur Model-View-Template (MVT) yang memudahkan pengguna untuk lebih memahami alur pengembangan strukturnya.
3. Django memiliki dokumentasi yang sangat lengkap dan lebih dimengerti sehingga memudahkan proses pembelajaran bagi pemula. 

## Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai Object-Relational Mapping (ORM) karena memiliki peran dalam memetakan objek dalam kode Python ke dalam tabel pada struktur database regional tanpa perlu melibatkan query SQL secara langsung.

# Tugas 3: Implementasi Form dan Data Delivery pada Django
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam pengimplementasian sebuah platform, data delivery diperlukan sebagai proses transfer data secara efektif, efisien, dan terpercaya dari satu titik ke titik lainnya, baik antara sistem, perangkat, maupun pengguna.
1. Data delivery memastikan informasi yang diperlukan pengguna ataupun sistem dapat diakses secara cepat dan efisien untuk menjaga platform beroperasi dengan lancar.
2. Data delivery melibatkan enkripsi serta mekanisme keamanan lainnya yang dilakukan dengan aman untuk mencegah baik kebocoran maupun akses data secara tidak sah.
3. Data delivery memastikan data dapat ditransfer dan diterima antar sistem secara efektif dan efisien sehingga menciptakan platform dengan integrasi yang lancar.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya pribadi, JSON lebih baik daripada XML. Formatnya yang lebih ringan dan sederhana membuat JSON menjadi lebih banyak digunakan, terutama dalam pengembangan website.
1. JSON menggunakan lebih sedikit teks karena tidak memerlukan declaration awal seperti XML, sehingga lebih hemat bandwidth saat mengirimkan data.
2. JSON diproses lebih cepat, karena langsung terintegrasi dengan JavaScript, dan lebih ringan dibandingan XML, yang memerlukan proses parsing lebih kompeks.
3. JSON memiliki struktur yang lebih sederhana dan format objek yang mirip dengan JavaScript, sehingga memudahkan user dalam memahami serta menulis kode.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Dalam Django, method is_valid() merupakan function yang digunakan untuk memvalidasi dan menjaga keamanan data yang diinput ke dalam form.
1. Method is_valid() secara otomatis akan memeriksa setiap field dalam form untuk memeriksa bahwa data yang diberikan sudah benar dan sesuai dengan spesifikasi yang diharapkan.
2. Jika semua data valid, method akan mengembalikan nilai True dan menyimpan data yang sudah divalidasi tersebut. Ini membantu dalam mengelola kesalahan dengan menampilkan pesan error, sehingga dapat mengurasi risiko keamanan yang dapat muncul dari data tidak valid. 

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token dibutuhkan ketika membuat form di Django dengan tujuan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Serangan CSRF merupakan jenis serangan dimana penyerang dapat memanipulasi user yang telah login ke situs untuk mengirimkan permintaan yang tidak sah ke server (seperti mengubah data pengguna, menyebarkan malware, dan/atau melakukan transaksi tidak legal), tanpa diketahui atau disetujui oleh pengguna tersebut. Tanpa crsf_token, website Django akan menjadi rentan terhadap serangan CSRF sehingga dapat menyebabkan kerugian serius baik bagi pengguna maupun bagi sistem.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Checklist tersebut diimplementasikan dengan cara-cara berikut.
1. **Membuat input `form` untuk menambahkan objek model pada app sebelumnya** <br />
Pertama, saya membuat berkas baru dengan nama forms.py dalam direktori main untuk menyimpan struktur form yang akan menerima data tersebut. Kemudian, dalam berkas views.py, ditambahkan beberapa import dari main.forms dengan tujuan untuk memanggil forms ketika dibuka. Setelah itu, saya menambahkan fuction baru create_product_entry dengan menggunakan form.is_valid() dengan tujuan untuk memvalidasi isi input tersebut. Selanjutnya, saya melakukan routing URL dengan mengimport fuction create_product_entry ke urls.py. Pada template HTML, ditambahkan <form method="POST> untuk menandai block form yang menggunakan method POST, {% csrf_token %} untuk mencegah serangan CSRF, serta button Submit untuk mengirimkan request ke view.
2. **Menambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID** <br />
Kedua, saya menambahkan import HttpResoibse dan Serializer pada berkas views.py. Kemudian, saya membuat fuction show_xml, show_json, show_xml_by_id, dan show_json_by_id yang akan melakukan return HttpResponse menyesuaikan dengan format yang digunakan.
3. **Membuat routing URL untuk masing-masing `views` yang telah ditambahkan sebelumnya** <br />
Ketiga, pada berkas urls.py, saya mengimport keempat function tersebut, lalu menambahkan path URL pada urlpatterns dengan formatnya masing-masing. Dengan demikian, proyek Django dapat dijalankan dengan perintah python manage.py runserver dan membuka link website sesuai dengan ketentaun format masing-masing.

## Dokumentasi Postman
1. **Membuka XML dengan show_xml**
<img src = "./images/show_xml.jpg" width = "800" height = "600">

2. **Membuka JSON dengan show_json**
<img src = "./images/show_json.jpg" width = "800" height = "600">

3. **Membuka XML dengan show_xml_by_id**
<img src = "./images/show_xml_by_id.jpg" width = "800" height = "600">

4. **Membuka JSON dengan show_json_by_id**
<img src = "./images/show_json_by_id.jpg" width = "800" height = "600">

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
## Apa perbedaan antara HttpResponseRedirect() dan redirect()?
Secara umum, HttpResponseRedirect() dan redirect() merupakan dua metode pada framework Django yang berjuan untuk mengarahkan pengguna ke URL lain. Namun, keduanya memiliki perbedaan dalam tingkat abstraksi, parameter input yang diterima, serta fleksibilitas dalam penulisan kode.
1. HttpResponseRedirect() merupakan class Django yang berada pada tingkat dasar dengan tujuan mengembalikan respons HTTP 302 dengan URL yang ditentukan secara manual, sementara redirect() merupakan shortcut penyederhana proses HttpResponseRedirect().
2. Berdasarkan parameter inputnya, HttpResponseRedirect() hanya menerima URL dalam bentuk string. Di sisi lain, redirect() dapat menerima string URL, nama view Django, args dan kwargs untuk membangun URL, ataupun objek model yang mendukung.
3. Dari segi fleksibilitas dalam penulisan kode, HttpResponseRedirect() memerlukan lebih banyak kode karena perlu menangani URL secara manual. Sementara itu, redirect() lebih efisien dalam penulisan kode karena dapat menangani URL dari berbagai sumber.

## Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan model User dalam Django dapat dilakukan menggunakan relasi foreign key untuk menunjukkan bahwa setiap produk yang dimiliki oleh seorang pengguna tertentu. Modul Product dihubungkan dungeon User menggunakan atribut ForeignKey(User, on_delete=models.CASCADE) yang bertujuan memastikan setiap produk hanya berkaitan dengan satu pengguna. Jika pengguna dihapus, semua produk yang dimiliki oleh pengguna tersebut juga akan dihapus. Relasi ini memungkinkan pengguna untuk mendapatkan akses semua produk yang terkait dengannya menggunakan user.product_set.all().

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Perbedaan antara authentication dan authorization terletak pada fokus prosesnya, dimana:
1. Autentikasi, yaitu proses verifikasi identitas pengguna dengan meminta informasi, seperti username dan password, untuk memastikan bahwa pengguna yang mencoba masuk adalah benar.
2. Autorisasi, merupakan proses di mana sistem menentukan apakah pengguna yang telah terautentikasi mendapatkan hak atau izin untuk mengakses data atau melakukan tindakan tertentu dalam sistem.

Django mengimplementasi konsep autentikasi dan autorisasi melalui modul bawaan django.contrib.auth, yang menyediakan sistem untuk mengelola informasi login, logout, dan pengelolaan sistem. Untuk autentikasi, Django menggunakan fungsi seperti authenticate() untuk memverifikasi username dan password serta login() untuk memulai sesi jika autentikasi berhasil. Sementara itu, untuk autorisasi, Django memungkinkan sistem untuk mengontrol tindakan yang dilakukan pengguna yang telah terautentikasi melalui decorator seperti @permission_required atau metode user.has_perm().

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django dapat mengingat pengguna yang telah login, dengan membuat sesi yang menyimpan informasi pengguna dalam bentuk ID, serta mengidentifikasi sesi pengguna menggunakan cookies.
1. Ketika pengguna login, Django membuat entri baru dalam database untuk sesi tersebut (ID pengguna dan data lainnya). Database tersebut disimpan dalam cookies yang akan dikirim ke browser pengguna.
2. Ketika pengguna mengakses aplikasi, cookies yang menyimpan ID sesi akan mengirimkan ID tersebut kembali ke server untuk mengidentifikasi sesi pengguna yang sedang aktif.

Selain untuk menyimpan ID sesi, cookies memiliki berbagai kegunaan seperti melacak dan menganalisis user behaviour serta personalisasi konten website.
1. Cookies berfungsi untuk memantau aktivitas pengguna di website dengan mengumpulkan informasi tentang perilaku pengguna untuk membantu pemilik website dalam menganalisis pola perilaku dan meningkatkan konten serta strategi pemasaran.
2. Cookies memungkinkan website untuk menyimpan preferensi pengguna seperti pilihan bahasa, tema, dan pengaturan tampilan untuk membantu menciptakan pengalaman pengguna yang lebih sesuai dengan kebutuhan dan keinginan mereka.

Namun, tingkat keamanan cookies bergantung pada bagaimana cookies tersebut diimplementasikan. Untuk memastikan pengunaan cookies aman, Django menyediakan atribut HttpOnly dan Secure, yang dapat melindungi data pengguna dari potensi risiko keamanan. Atribut HttpOnly mencegah cookies diakses oleh kode JavaScript sehingga hanya dapat dimodifikasi oleh server melalui protokol HTTP/HTTPS. Sementara itu, atribut Secure memastikan bahwa cookies hanya dikirim melalui koneksi HTTPS yang terenkripsi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Checklist tersebut diimplementasikan dengan cara-cara berikut.
1. **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar** <br />
Pertama, virtual environment diaktifkan pada terminal. Setelah itu, melakukan import UseCreationForm dan message (untuk membuat registrasi), authenticate, login, dan AuthenticationForm (untuk membuat login), serta logout (untuk membuat logout) pada berkas views.py. Kemudian, saya membuat fungsi register, login_user, dan logout_user dengan parameternya masing-masing pada berkas yang sama. Setelah membuat fungsi, saya membuat berkas html baru untuk register.html dan login.html serta menambahkan logout button pada main.html agar register, login, dan logout dapat diakses melalui website. Agar berkas-berkas tersebut dapat dieksekusi, pada berkas urls.py dilakukan import register, login_user, dan logout_user serta menambahkan path url ketiga import tersebut pada urlpatterns. Terakhir, untuk merestriksi akses halaman main, pada views.py dilakukan import login_required dan menambahkan @login_required dengan parameternya di atas fungsi show_main.
2. **Menghubungkan model `Product` dengan `User`** <br />
Pertama, saya mengimport model User pada models.py dan menambahkan models.ForeignKey(User, on_delete=models.CASCADE) dalam class ProductEntry agar product entry terhubung hanya dengan satu orang. Kemudian, pada views.py, saya menambahkan form.save(commit=False) serta request.user pada fungsi create_product_entry. Selain itu, saya juga menambahkan ProductEntry.objects.filter(user=request.user) pada fungsi show_main di berkas yang sama. Karena saya telah mengubah models.py, saya perlu melakukan migrasi model dengan python manage.py makemigration dan python manage.py migrate. Terakhir, pada settings.py, saya melakukan import os, lalu mengganti variabel DEBUG serta menambahkan variabel PRODUCTION.
3. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi** <br />
Pertama, saya melakukan import datetime, HttpResponseRedirect, dan reverse pada berkas views.py. Setelah itu, saya mengubah pernyataan if form.is_valid menjadi HttpResponseRedirect(reverse("main:show_main")) dan melakukan set_cookie berdasarkan last login dan datetime. Kemudian, saya nembahkan last_login dengan request.COOKIES[‘last_login’] pada context yang berada pada fungsi show_main. Selain itu, saya juga menambahkan HttpResponseRedirect pada fungsi logout_user untuk menghapus cookies last_login saat pengguna logout. Terakhir, untuk menampilkan last login tersebut, saya menambahkannya pada berkas main.html.

# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
CSS selector memiliki urutan prioritas pengambilan dimulai dari inline styles, ID selectors, class selectors, attribute selectors, dan terakhir element selectors.
1. Inline styles memiliki prioritas tertinggi karena style tersebut ditetapkan langsung dalam atribut style pada elemen HTML.
2. ID Selector, yang ditandai dengan simbol pagar, memiliki prioritas lebih tinggi karena ID telah dirancang untuk bersifat unik dalam sebuah dokumen dengan tujuan memberikan kontrol yang lebih tepat dalam penataan elemen individual.
3. Class Selector, yang diidentifikasikan dengan simbol titik, memiliki prioritas lebih tinggi karena dirancang untuk menerapkan gaya pada sekelompok elemen, memberikan kontrol yang lebih luas terhadap styling.
4. Attribute Selector memiliki prioritas lebih rendah karena berlaku berdasarkan keberadaan atribut tertentu pada elemen, sehingga spesifisitasnya tidak sekuat kelas.
5. Element Selector memiliki prioritas terendah karena hanya berlaku pada tipe elemen tertentu dan tidak memberikan kontrol spesifik yang sama seperti selector lainnya.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Menurut saya, responsive design merupakan konsep yang sangat penting dalam pengembangan aplikasi website karena meningkatkan pengalaman pengguna dengan menyesuaikan interface sesuai dengan berbagai ukuran layar, serta meningkatkan aksesibilitas bagi lebih banyak orang. Dengan semakin banyaknya penggunaan perangkat mobile untuk menjelajah internet, responsive design menjadi semakin penting untuk menjangkau audiens yang lebih luas. Sebagai contoh, https://twitter.com dan https://pinterest.com telah menerapkan responsive design untuk memastikan bahwa pengguna dapat mengakses konten mereka dengan mudah di berbagai perangkat. Namun, di sisi lain, https://academic.ui.ac.id belum menerapkan responsive design, yang mengakibatkan tampilan dan navigasi yang kurang optimal saat diakses melalui perangkat mobile.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Secara garis besar, margin, border, dan padding merupakan elemen dari box model dalam CSS yang digunakan untuk menentukan tata letak elemen pada halaman web.
1. Margin merupakan ruang kosong di luar batas elemen yang berfungsi mengatur jarak antar elemen pada halaman web. Dalam mengimplementasikannya, margin dapat diatur untuk semua sisi (atas, kanan, bawah, kiri) atau untuk sisi tertentu saja.
2. Border merupakan garis yang mengelilingi elemen, terletak di antara margin dan padding, dan dapat disesuaikan ketebalan, gaya, serta warnanya. Dalam mengimplementasikannya, border dapat diatur untuk setiap sisi secara terpisah atau sekaligus untuk semua sisi.
3. Padding merupakan ruang kosong di dalam elemen yang memisahkan konten dari batas elemen dan memberi jarak antara isi elemen dengan tepinya.  Dalam mengimplementasikannya, padding dapat diterapkan secara merata pada semua sisi elemen atau diatur secara khusus untuk tiap sisi atas, bawah, kanan, dan kiri.

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Dalam CSS, flexbox merupakan metode tata letak satu dimensi untuk mengatur elemen secara fleksibel dalam satu arah. Sementara itu, grid layout adalah metode tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan.
1. Konsep flexbox memudahkan distribusi ruang dan perataan elemen, terutama dalam konteks ukuran layar yang berbeda-beda. Kegunaan Flexbox terletak pada kemampuannya untuk menciptakan tata letak yang fleksibel dan responsif, seperti navbar dan galeri gambar, dengan perataan elemen yang mudah.
2. Konsep grid layout memungkinkan pembagian halaman menjadi baris dan kolom. Kegunaan Grid Layout terletak pada kemampuannya untuk menciptakan tata letak kompleks dan terstruktur, seperti halaman web dengan header, footer, sidebar, dan konten utama.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Checklist tersebut diimplementasikan dengan cara-cara berikut.
1. **Implementasikan fungsi untuk mengedit product** <br />
Pertama, saya membuat fungsi baru dengan nama edit_product dengan parameter request dan id pada berkas views.py serta menambahkan import reverse dari django.shortcuts dan juga import HttpResponseRedirect dari django.http. Kemudian, saya membuat berkas baru dengan nama edit_product.html yang akan menjadi windows ketika melakukan edit product. Setelah itu, pada berkas urls.py, saya melakukan import edit_product dengan menambahkan path url ke dalam urlpatterns. Terakhir, pada berkas main.html, saya membuat button yang menghubungkan windows utama ke windows edit_product.
2. **Implementasikan fungsi untuk menghapus product** <br />
Pertama, pada berkas views.py, saya membuat fungsi baru dengan nama delete_product dengan parameter request serta id. Selanjutnya, saya melakukan import delete_product pada berkas urls.py serta menambahkan path urlnya ke dalam urlpatterns. Terakhir, saya membuat button yang akan menghapus product yang telah dibuat sebelumnya pada berkas main.html
3. **Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)** <br />
Pertama, saya menambahkan script dengan source website tailwind (karena saya menggunakan tailwind) pada berkas base.html. Kemudian, untuk menambahkan kelas custom, saya membuat berkas global.css pada folder static/css agar dapat menjalankan CSS. Selanjutnya, pada global.css, saya memodifikasi file berdasarkan format yang saya inginkan. Terakhir, saya melakukan styling pada halaman login, register, home, create product entry, dan juga edit product agar sesuai dengan UI yang saya harapkan.
4. **Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.** <br />
Pertama, pada templates, saya membuat berkas navbar.html yang berisikan styling navbar dengan fitur home, create, favorites, cart, user, dan logout button. Selanjutnya, pada main.html, create_product_entry.html, dan edit_product.html saya menambahkan {% include 'navbar.html' %} agar program dapat melakukan load navigation bar tersebut.

# Tugas 6: JavaScript dan AJAX
## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript memiliki beberapa penggunaan dalam pengembangan aplikasi website, seperti meningkatkan interaktivitas, mendukung pemrosesan asikron menggunakan AJAX (Asynchronous JavaScript and XML), serta mempermudah integrasi karena dapat dioperasikan dengan beberapa bahasa pemrograman.
1. JavaScript memungkinkan para pengguna untuk menciptakan elemen interaktif seperti menu dropdown, slider, dan validasi formulir yang dapat berfungsi langsung di browser tanpa perlu memuat ulang halaman.
2. Dengan menggunakan AJAX, JavaScript memungkinkan aplikasi web untuk mengirim dan menerima data dari server backend tanpa perlu memuat ulang halaman, yang pada gilirannya meningkatkan efisiensi dan pengalaman pengguna.
3. JavaScript dapat diintegrasikan dengan berbagai bahasa pemrograman lain seperti PHP, Python, CSS, dan Java untuk mengembangkan aplikasi full-stack yang lebih dinamis dan lebih interaktif.

## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Secara keseluruhan, penggunaan await saat menggunakan fetch() dapat mempermudah pengelolaan respons dari permintaan jaringan. Ini karena penggunannya memungkinkan kode untuk berjalan secara berurutan (di mana await akan menunggu hasil dari eksekusi fetch()). Dengan cara ini, penggunaan callback atau chaining dari Promise dapat dikurangi, sehingga kompleksitas berkurang dan alur logika menjadi lebih jelas.

Jika kode tidak menggunakan await, fetch() akan mengembalikan sebuah Promise, yang perlu ditangani hasilnya secara manual dengan menggunakan method .then() serta .catch(). Tanpa await, eksekusi kode akan terus berlanjut tanpa menunggu respons dari server, yang dapat menyulitkan pengelolaan alur eksekusi dan penanganan kesalahan. Akibatnya, kode bisa menjadi lebih kompleks dan sulit dipahami.

## Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator csrf_exempt pada view yang digunakan untuk AJAX POST memiliki fungsi untuk menonaktifkan perlindungan CSRF sehingga permintaan AJAX dapat diproses tanpa memerlukan token CSRF. CSRF merupakan serangan yang mengeksploitasi sesi pengguna yang aktif untuk melakukan aksi yang tidak diinginkan atas nama pengguna tersebut. Tanpa menggunakan decorator csrf_exempt, permintaan AJAX yang tidak menyertakan token CSRF akan ditolak oleh Django, sehingga mengakibatkan kesalahan dan membuat permintaan tidak dapat diproses.

## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Selain dilakukan di fontend, pembersihan data input pengguna juga perlu dilakukan di backend karena dapat mencegah serangan keamanan, menjamin integritas data yang masuk ke sistem, serta memberikan fleksibilitas untuk mengubah aturan pembersihan tanpa mengganggu frontend.
1. Apabila hanya mengandalkan pembersihan di frontend, program dapat menciptakan kerentanan terhadap serangan, sehingga memiliki backend yang kuat sangat penting untuk melindungi aplikasi dari potensi eksploitasi oleh pengguna yang tidak bertanggung jawab.
2. Dengan melakukan pembersihan di backend, dapat dipastikan bahwa semua data yang masuk ke sistem adalah valid dan sesuai dengan standar yang ditetapkan, sehingga menjaga kualitas dan konsistensi data.
3. Backend dapat dengan mudah diubah atau diperbarui tanpa mempengaruhi kode frontend, sehingga pembersihan di backend memungkinkan penyesuaian aturan tanpa mengganggu pengalaman pengguna di sisi frontend.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Checklist tersebut diimplementasikan dengan cara-cara berikut.
1. **Mengubah kode `cards` data product agar dapat mendukung AJAX `GET`** <br />
Pertama, saya menghapus mood_entries serta ‘mood_entries’: mood_entries yang ada pada berkas views.py serta mengubah variabel data pada function show_json dan show_xml menjadi Product.objects.filter(user=request.user). Setelah itu, pada berkas main.html, saya kembali menghapus kode bagian block conditional untuk melakukan print product_entries dan menggantinya menjadi  id=“product_entry_cards".
2. **Melakukan pengambilan data prodyct menggunakan AJAX `GET` serta pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.** <br />
Selanjutnya, tetap dalam berkas main.html, saya membuat function getProductEntries() yang akan melakukan fetch() API pada data JSON serta membuat function refreshProductEntries() yang melakukan refresh data secara asinkronus. Jangan lupa untuk memanggil function tersebut agar dapat dijalankan.
3. **Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.** <br />
Setelah membuat add_product_entry_ajax, saya melakukan implementasi modal tailwind pada berkas main.html dengan menggunakan crudModal dan crudModalContent. Agar kedua class modal tersebut dapat diakses, pada bagian bawah berkas main.html, saya membuat function showModal serta hideModal. Kemudian, saya menambahkan button Create New Product Entry by AJAX dengan data-modal-targetnya adalah crudModal. 
4. **Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.** <br />
Kemudian, pada berkas views.py, saya membuat fungsi baru bernama add_product_entry_ajax() dengan memanggil decorator @csrf_exempt dan @require_POST agar program hanya dapat diakses oleh pengguna yang melakukan login.
5. **Buatlah path `/create-ajax/` yang mengarah ke fungsi view yang baru kamu buat.** <br />
Tidak lupa, pada berkas urls.py, saya melakukan import add_product_entry_ajax dan menambahkannya pada urlpatterns.
6. **Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/create-ajax/`.** <br />
Untuk menghubungkan form tersebut, saya membuat function baru bernama addProductEntry() yang pada mula-mula akan melakukan fetch dari add_product_entry_ajax dan menambahkan agar response mengarah pada refreshProductEntries() yang telah dibuat sebelumnya. Di bawahnya, saya menambahkan getElementByID lalu memanggil function addProductEntry() tersebut.
7. **Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan.** <br />
Refresh halaman utama secara asinkronus dapat dilakukan dengan pemanggilan function refreshProductEntries() yang telah dibuat sebelumnya. Terakhir, untuk menjaga agar website tidak mendapatkan error Cross Site Scriptig (XSS), saya akan melakukan import strip_tags pada views.py dengan menambahkan strip_tags() pada variabel di add_product_entry_ajax() yang data fieldnya merupakan Character atau Text. Lalu, pada forms.py saya membuat method clean_name() dan clean_description() yang akan menghapus jika terjadi error. Kemudian, pada berkas main.html saya akan menambahkan link dompurify seta membuat const name dan description dengan DOMPurify.sanitize(item.fields). Akibatnya, ketika melakukan input XSS, program tidak akan memunculkan alert box error lagi.