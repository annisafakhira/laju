Annisa Fakhira Cendeki - PBP C

Link PWS: https://annisa-fakhira41-laju.pbp.cs.ui.ac.id

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