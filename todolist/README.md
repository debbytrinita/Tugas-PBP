[Link Aplikasi Heroku](https://tugas-3-pbp.herokuapp.com/todolist/)


## Apa kegunaan {% csrf_token %} pada elemen < form >  Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen < form >?
Cross-Site Request Forgery (CSRF) merupakan sebuah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu.
{% csrf_token %} merupakan CSRF Token yaitu value yang unik dan rahasia yang dihasilkan oleh aplikasi di bagian server, kemudian dikirimkan ke klien dalam permintaan HTTP berikutnya yang nantinya akan dibuat juga di sisi klien. CSRF Token berguna untuk menghindari serangan Cross-Site Request Forgery (CSRF). Apabila potongan kode tersebut tidak ada, website milik kita menjadi lebih mudah terkena serangan Cross-Site Request Forgery (CSRF). 

## Apakah kita dapat membuat elemen < form > secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat < form > secara manual.
Ya, kita bisa membuat elemen < form >secara manual dengan memnggunakan tag form (< form > </ form >). Tag form akan dilengkapi dengan tag tag lain seperti label, input, button, dll.   

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Setelah user melakukan submit, akan dicek terlebih dahulu kevalidan dari data yang diberikan oleh user. Jika valid maka data tersebut akan disimpan kedalam database.  Kemudian user akan di redirect ke halaman todolist

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi bernama todolist dengan menjalankan  perintah python manage.py startapp mywatchlist
2. Menambahkan todolist kedalam INSTALLED_APPS di dalam folder settings.py. Untuk dapat mengakses http://localhost:8000/todolist, tambahkan kode berikut ke dalam file urls.py didalam folder project_django 

        path('todolist/',include('todolist.urls')), .
3. Membuat model Task yang memiliki atribut user, date, title, description dengan menambahkan kode berikut ke dalam models.py didalam folder todolist

        class Task(models.Model):
            class Task(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            date = models.DateTimeField()
            title = models.TextField()
            description = models.TextField()
    Kemudian Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi model tersebut ke database Django lokal.
    Setelah itu, jalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
    
4. Mengimplementasikan form registrasi, login, dan logout dengan membuat file `register.html`, `login.html`, dan `todolist.html`. Kemudian membuat 3 fungsi(register, login_user, logout_user) yang menerima parameter request dan mengembalikan render pada views.py

5. Membuat halaman utama todolist pada todolist.html yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

6. Membuat halaman form untuk membuat task baru dengan membuat file forms.py Kemudian membuat fungsi di dalam views.py (add_new_task) dan menambahkan class yang ada di forms.py kedalam context yang ada di fungsi add_new_task agar dapat terhubung dengan file add_new_task.html  

7. Membuat routing sehingga data di atas dapat diakses melalui URL dengan cara menambahkan code berikut ke dalam file urls.py di dalam folder todolist

        path('login/', login_user, name='login'),
        path('register/',register, name='register'),
        path('create-task/',add_new_task, name='add_new_task'),
        path('logout/',logout_user,name='logout')
8. Melakukan *deployment* ke aplikasi heroku

9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.