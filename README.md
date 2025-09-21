Annisa Fakhira Cendeki - PBP C
Link PWS: https://annisa-fakhira41-laju.pbp.cs.ui.ac.id

### TUGAS 2
- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat sebuah proyek Django baru, buat direktori utama dengan membuat file kemudian untuk membuat proyek Django di dalamnya maka menggunakan "django-admin startproject <nama_proyek> ." (tanpa ""). Pada tugas ini maka saya menggunakan 'django-admin startproject laju .'(tanpa "") dengan memastikan sudah terdapat virtual environment dan telah diaktivasi virtual environment-nya serta telah install django, dependencies.

    2. Membuat aplikasi dengan nama main pada proyek tersebut, untuk membuat aplikasi main maka menggunakan "python manage.py startapp main" (tanpa "").

    3.  Melakukan routing pada proyek agar dapat menjalankan aplikasi main, setelah melakukan langkah pada checklist 2 kemudian agar aplikasi dapat dijalankan maka tambahkan 'main' ke dalam variable INSTALLED_APPS pada settings.py di dalam direktori proyek.

    4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib, untuk membuatnya maka buka models.py, tambahkan class Product(models.Model) lalu isi dengan atribut wajib yang tertera pada soal. Kemudian agar perubahannya terrefleksi pada database maka gunakan "python manage.py makemigrations" dan "python manage.py migrate" (tanpa "").

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas, sebelumnya tuliskan "from django.shortcuts import render" (tanpa"") untuk render tampilan HTML dengan menggunakan data yang diberikan saat return render, selanjutnya buat fungsi yang menerima request sebagai parameter fungsinya dan fungsi akan dipanggil setiap kali ada user membuka page. Lalu return render dengan "return render(request, <file_HTML>, context)" (tanpa""), pada tahap ini Django akan mengganti datanya dengan isi context sehingga main.html dapat menampilkan NPM, nama, dan kelas.

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py, setelah melakukan langkah pada checklist 2 dan memastikan MVT yang diperlukan ada maka perlu membuat file urls.py di dalam direktori main. Kemudian isi file urls.py di dalam direktori main dengan nama aplikasi dan fungsi pada views.py yang sesuai. Kemudian juga perlu disesuaikan urls.py di direktori proyek dengan menambahkan import include dan path('', include('main.urls')) di urlspattern.
    
    7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet, untuk deployment maka create a new project terlebih dahulu pada PWS dan sesuaikan nama projectnya. Lalu edit environment variables sesuai isi file dari .env.prod. Kemudian, tambahkan URL deployment PWS di ALLOWED_HOSTS pada settings.py. Lalu push ke PWS, kemudian masukkan credentials yang diterima saat project di-create.

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    https://drive.google.com/file/d/1WqTpyvNFydObXMwS1HDC6aXtzHQjzM64/view?usp=sharing

- Jelaskan peran settings.py dalam proyek Django!
    settings.py seperti ruang kontrol yang mengatur izin semua bagian proyek Django sehingga proyek bisa tahu cara kerja dan jalan proyek. 

- Bagaimana cara kerja migrasi database di Django?
    Migrasi pada Django adalah sinkronasi data di models.py dan di database. Jika terjadi perubahan pada model, Django juga perlu memperbarui databasenya. Untuk melakukan migrasi maka tuliskan "python manage.py makemigrations" (tanpa "") untuk mencatat apa saja perubahannya, lalu "python manage.py migrate" (tanpa "") untuk eksekusi perubahan ke database, seperti push di Git.

- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Untuk mahasiswa, web framework Django berbasis Python sehingga bahasa pemrogramannya sudah dipelajari. Django juga menggunakan arsitektur MTV (Model-Template-View) sehingga kode lebih terstruktur dan mudah dipahami. Melihat dari sisi keamanan, Django sudah dilengkapi proteksi terhadap risiko keamanan umum seperti SQL injection, CSRF (Cross-Site Request Forgery), dan XSS (Cross-Site Scripting). Selain itu Django juga dikenal scalable sehingga dapat digunakan baik dalam skala besar maupun kecil, memiliki dokumentasi yang lengkap, serta didukung komunitas besar yang dapat membantu mempelajari atau menangani error dalam Django.

- Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Tidak, penjelasan sudah lengkap dan mudah dipahami. Terima kasih kak!


### TUGAS 3
- Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery seperti kurir yang mengirim data antara server dan user sehingga jika user melakukan pembelian atau menambahkan produk maka data akan terkirim ke server. Selain itu, server juga mengirim data ke user dengan menampilkan informasi mengenai produk. Hal ini diperlukan agar data terupdate secara real-time.

- Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Secara subjektif, JSON lebih mudah digunakan daripada XML karena lebih mudah untuk dibacanya. Kepopuleran JSON juga disebabkan oleh kecepatan pengirimannya karena ukurannya lebih kecil dari XML (tanpa tagging).

- Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() pada form Django berguna untuk validasi form dari user dengan mengecek apakah input sudah sesuai aturan atau belum. Validasi jawabannya akan terlihat dari return boolean valuenya, jika method is_valid() mereturn True maka data akan diproses atau disimpan di database. Apabila method is_valid() mereturn False maka ada kesalahan dalam input, seperti data type tidak sesuai ataupun input yang wajib diisi itu kosong. Hal ini diperlukan agar data yang masuk sudah benar, aman, dan sesuai sehingga tidak menimbulkan bug ataupun error.

- Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf_token adalah token otomatis yang disisipkan di setiap form HTML untuk membedakan setiap user dengan sistem session user. csrf_token dibutuhkan saat membuat form agar terhindar dari CSRF (Cross-Site Request Forgery). Jika tidak menambahkan csrf_token pada form Django maka penyerang bisa berpura-pura mengirim request dengan menyamar menjadi user. Hal tersebut yang dimanfaatkan oleh penyerang.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. Pastikan sudah ada file views.py pada direktori aplikasi, kemudian tambahkan fungsi show_xml dan show_json untuk menampilkan data dalam bentuk XML dan JSON. Selain itu, dua fungsi lainnya adalah show_xml_by_id dan show_json_by_id untuk menampilkan data suatu objek sesuai IDnya. Datanya diambil dari models.py lalu pengubahan format menjadi XML dan JSON dilakukan dengan serializers.serialize. Pada show_xml_by_id pengambilan objek dilakukan dengan filter() serta pada show_json_by_id pengambilan objek dilakukan dengan get()

    2. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1, untuk routing URL masing-masing views maka menggunakan urls.py dengan menambahkan path-path yang sesuai dalam urlspattern pada urls.py di direktori aplikasi. Kemudian dihubungkan ke Djangonya dengan urls.py di direktori proyek melalui penambahan pathnya dengan include dalam urlspattern.

    3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek, untuk membuat halamannya maka gunakan fungsi di views.py untuk mengambil datanya dan akan diperlihatkan dengan main.html dan menambahkan tombol add di atas dengan 
    "<a href="{% url 'main:add_product' %}">
        <button>+ Add Product</button>
    </a>" (tanpa"")
    Selain itu untuk setiap product akan diberikan tombol Detail untuk page khusus informasi dari objek.
    "<p><a href="{% url 'main:show_product' product.id %}"><button>Detail</button></a></p>" (tanpa"")
    Semuanya didasarkan dengan fungsi add_product dan show_product yang ada pada views.py serta untuk buttonnya terlihat dengan main.html
    
    4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya, untuk membuat form maka gunakan forms.py dengan fieldsnya sesuai pada fields di models.py. Kemudian buat fungsi juga yaitu add_product dan show_product di views.py serta hubungkan dan buat HTML nya untuk setiap fungsi agar dapat ditampilkan.
    
    5. Membuat halaman yang menampilkan detail dari setiap data objek model, untuk membuatnya maka buat fungsi (show_product) di views.py yang akan menampilkan satu produk sesuai ID dari URL. Data produk kemudian akan ditampilkan dengan membuat file HTML nya juga.

- Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Tidak, penjelasan sudah lengkap dan mudah dipahami. Terima kasih kak!

- Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
    https://drive.google.com/drive/folders/1emSAwUY_sbiY3q0QaFFXOfmpDhIpzhO5?usp=sharing


### TUGAS 4
- Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    Django AuthenticationForm sesuai namanya, merupakan form bawaan dari Django untuk mempermudah developer dengan menyediakan field otomatis untuk username dan password yang juga mengecek apakah data valid dan sesuai dengan yang ada di database. Kelebihannya tentu saja mempermudah developer karena tidak perlu membuat form manual dan sudah terintegrasi serta tervalidasi dengan database. Akan tetapi, Django AuthenticationForm tidak menyediakan untuk fitur kompleks seperti OTP ataupun login yang terkoneksi dengan aplikasi lain (email, facebook).

- Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Autentikasi itu digunakan untuk memastikan user yang login dan validasi data user di database sedangkan otorisasi mengatur hak akses usernya. Sederhananya, autentikasi itu saat login awal dan user dapat mengakses fitur apa saja itu otorisasi. Pada Django, autentikasi dilakukan dengan AuthenticationForm dan dicek validasinya lalu memanggil login() sementara otorisasi dilakukan dengan membatasi akses melalui @login_required(login_url='/login').

- Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Cookies penyimpanannya langsung di browser sehingga mudah diakses setiap user open new tab serta sedikit memorinya jadi lebih cepat. Akan tetapi lebih berisiko untuk keamanan karena disimpan di client side dan memory sizenya terbatas. Sementara session disimpannya di server dan browser hanya memegang session ID sehingga lebih aman untuk keamanan tetapi berat untuk servernya karena server harus menyimpan data user yang sedang login.

- Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Tidak, salah satu kekurangan cookies memang terletak pada risiko keamanannya karena penyimpanannya langsung di browser milik user sehingga berisiko dicuri atau dimanipulasi (XSS, session hijacking). Pada Django, session cookies disimpan dengan tanda khusus atau yang disebut signed cookies, kemudian HttpOnly juga agar cookies tidak bisa diakses sembarangan, serta Secure flag agar pengiriman cookies lebih aman. Semua pengaturan untuk kontrol keamanan cookies terdapat di settings.py.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
    1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya, untuk membuat web dapat melakukan registrasi, login, logout, dan akses sesuai status login/logoutnya maka menggunakan beberapa class dan fungsi dari Django. UserCreationForm digunakan untuk proses registrasi sedangkan AuthenticationForm digunakan untuk proses login dengan memvalidasi kesesuaian informasinya. Sementara itu untuk logout menggunakan fungsi logout(request) yang juga bawaan dari Django. Kemudian untuk akses fitur yang disesuaikan oleh status login/logoutnya misal harus login untuk mengakses suatu fitur maka menggunakan  @login_required(login_url='/login').

    2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal. Melakukan tahapan ini diawali dengan membuka localhost di browser (linknya terdapat setelah menjalankan python manage runserver). Kemudian lakukan register dan login dengan akun yang sudah dibuat. Setelahnya klik Add Product dan sesuaikan semua detail produknya. Lakukan hingga kedua akun memiliki setidaknya 3 produk.

    3. Menghubungkan model Product dengan User, untuk menghubungkan model product dengan user maka menggunakan 'user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)' (tanpa'') di models.py serta untuk pengisian otomatis informasi data user yang sedang login terdapat di views.py seperti untuk mengetahui sellernya maka menggunakan 'product_entry.user = request.user' (tanpa'').

    4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi. Informasi user yang sedang login diketahui dari 'request.user' (tanpa''). Oleh karena itu, jika ingin menampilkan detail informasi user pada halaman utama aplikasi maka user perlu login terlebih dahulu untuk akses halaman utama aplikasi dan untuk mengeceknya menggunakan '@login_required' (tanpa''). Setelah memastikan data user yang sedang login dapat diambil maka untuk pengambilan data serta untuk menampilkannya nanti di template menggunakan fungsi show_main(request) di views.py pada bagian context (username dengan request.user.username dan last login dengan request.COOKIES.get('last_login', 'Never')). Terakhir, agar informasi last login benar maka saat login set cookienya dengan 'response.set_cookie('last_login', str(datetime.datetime.now()))'  (tanpa'') serta saat logout cookienya dihapus dengan 'response.delete_cookie('last_login')' (tanpa'').