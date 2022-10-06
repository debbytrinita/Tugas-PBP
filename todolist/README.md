[Link Aplikasi Heroku](https://tugas-3-pbp.herokuapp.com/todolist/)

## TUGAS 4 ##
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

## TUGAS 5 ##
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style? ##
**Inline CSS** adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

**kelebihan**: Sangat membantu ketika ingin menguji, melihat perubahan dan memperbaiki kode pada satu elemen.

**kekurangan**: Tidak efisien karena hanya bisa diterapkan pada satu elemen HTML.

**Internal CSS** adalah kode CSS yang ditulis di dalam tag < style > dan kode HTML dituliskan di bagian atas (header) file HTML

**kelebihan**:
Tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file

**kekurangan**:
Tidak efisien ketika ingin menggunakan CSS yang sama dalam beberapa file.

**Eksternal CSS** adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css.

**kelebihan**:
Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi dan File CSS dapat digunakan di beberapa halaman website sekaligus

**kekurangan**:
Halaman akan menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML (dapat terjadi jika koneksi internet lambat)

## Jelaskan tag HTML5 yang kamu ketahui.
**< header >** yaitu tag untuk mendefinisikan sebuah header dalam sebuah dokumen 

**< nav >** yaitu tag untuk mendefinisikan navigasi yang biasanya berisi link untuk menuju kehalaman lain

**< footer >** yaitu tag untuk mendefinisikan sebuah footer dalam sebuah dokumen 

**< canvas >** yaitu tag yang digunakan untuk menggambar(render) grafik, image, dan teks

**< video >** yaitu tag untuk menyisipkan sebuah video atau film ke dalam halaman HTML

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selector tag yaitu selector yang akan memilih elemen berdasarkan nama tag. Contoh:

         p {
           color: blue;
        }
     Kode diatas akan mengubah seluruh elemen yang memiliki tag p menjadi warna biru. 

2. Class selector yaitu selector yang memilih elemen berdasarkan nama class yang diberikan. Class selector dimulai dengan tanda titik(.) Contoh:

        .container {
           margin: 10px;
           padding: 5px;
        }
   Kode diatas akan diterapkan pada semua elemen yang ada di dalam class container

3. ID selector yaitu selector yang memilih elemen berdasarkan id, bedanya dengan class adalah id hanya boleh digunakan untuk satu elemen saja. ID selector dimulai dengan tanda pagar (#) Contoh:

        #header {
           background: red;
           color: white;
        }
   Kode diatas akan diterapkan pada elemen yang memiliki ID berupa header

4. Attribute Selector yaitu selector yang memilih elemen berdasarkan atribut. Contoh:
 
        input[type=text] {
           padding: 10px;
           border: 1px solid black;
        }
   Kode di atas akan memilih semua elemen input yang memiliki atribut type='text'
5. Universal selector yaitu selector yang digunakan untuk menyeleksi semua elemen. Contoh:

        * {
           border: 1px solid black;
        }
   Kode diatas artinya semua elemen akan memiliki garis solid dengan ukuran 1px dan berwarna hitam
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya melakukan kostumisasi template HTML menggunakan Bootstrap sehingga bersifat responsive. Untuk **halaman login**, saya membuat container yang disertai dengan border berwarna pink. Di dalam container tersebut saya masukkan form untuk mengisi username dan password. Kemudian di bawahnya saya tambahkan button untuk men-submit form yang telah diisi. Lalu, dibawahnya terdapat link untuk melakukan registrasi jika belum mempunyai akun. Untuk **halaman register**, karena form nya dibuat dengan UserCreationForm, maka saya melakukan for loop kepada masing-masing label dan inputnya. Kemudian menambahkan button untuk men-submit formulir dan menambahkan link menuju halaman login jika sudah memiliki akun. Untuk **halaman add_new_task**, saya menambahkan navbar di atasnya yang dilengkapi button untuk logout dan kembali ke halaman todolist. Setelah itu saya membuat container yang didalamnya terdapat formulir untuk menambahkan task dan disertai button untuk men-submit task tersebut. 
Untuk **halaman todolist**, saya juga membuat navbar yang dilengkapi button untuk logout dan untuk menambah task baru/menuju ke halaman add_new_task. Di pojok kiri task bar terdapat nama user/akun yang sedang login. Kemudian saya mengimplementasikan card untuk setiap todolist. Pada setiap card terdapat judul, deskripsi task, dan tanggal task tersebut dibuat. Selain itu saya juga tambahkan hover disetiap card todolist