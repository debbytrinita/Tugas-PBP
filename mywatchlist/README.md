[Link Aplikasi Heroku](https://tugas-3-pbp.herokuapp.com/mywatchlist/)

**Jelaskan perbedaan antara JSON, XML, dan HTML!**

Perbedeaan antara JSON dan XML:
1. JSON menyimpan elemen secara efisien, sedangkan penyimpanan elemen oleh XML kurang efisien 
2. Nama file JSON diakhiri dengan ekstensi .json sedangkan file XML diakhiri dengan ekstensi .xml
3. Objek JSON memiliki tipe seperti string, number, array, Boolean sedangkan data XML harus berupa string 
4. JSON hanya support tipe data text dan number sedangkan XML support berbagai macam data seperti number, text, images, charts, graphs, dll
5. XML lebih aman dibandingkan dengan JSON

Perbedaan HTML dengan JSON:

1. Dalam pengembangannya, JSON menggunakan bahasa seperti JavaScript, bukan markup language seperti HTML
2. JSON bersifat lebih fleksibel dibandingkan dengan HTML
3. JSON pada umumnya digunakan untuk menyimpan dan mentransfer data sedangkan HTML difokuskan pada penyajian data 

Perbedanaan HTML dengan XML:

1. HTML menitikberatkan pada bagaimana format tampilan dari data sedangkan XML menitikberatkan pada struktur dan konteksnya
2. XML berfokus pada transfer data sedangkan HTML difokuskan pada penyajian data.
3. XML *Case Sensitive* sedangkan XML *Case Insensitive*
4. *Tag* XML tidak ditentukan sebelumnya sedangkan HTML memiliki *tag* yang telah ditentukan sebelumnya.

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Kita memerlukan *data delivery* dalam mengimplementasikan platform adalah karena dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Selain itu *data delivery* berguna untuk melakukan pertukaran data atau menukar informasi dari web server sehingga dapat dibaca oleh para pengguna

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Membuat suatu aplikasi bernama mywatchlist di proyek Django dengan perintah python manage.py startapp mywatchlist
2. Menambahkan mywatchlist kedalam INSTALLED_APPS di dalam folder settings.py. Untuk dapat mengakses http://localhost:8000/mywatchlist, tambahkan kode berikut ke dalam file urls.py didalam folder project_django 

        path('mywatchlist/',include('mywatchlist.urls')), .
3. Membuat model mywatchlist yang memiliki atribut watched, title, rating, release_date, dan review dengan menambahkan kode berikut ke dalam models.py didalam folder mywatchlist

        class MyWatchList(models.Model):
            watched = models.TextField()
            title = models.TextField()
            rating = models.TextField()
            release_date = models.TextField()
            review = models.TextField()
    Kemudian Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi model tersebut ke database Django lokal.
    Setelah itu, jalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
4. Menambahkan 10 data untuk objek MyWatchList di dalam file initial_mywatchlist_data.json didalam folder fixtures nya mywatchlist. Kemudian jalankan perintah python manage.py loaddata initial_mywatchlist_data.json untuk memasukkan data tersebut ke dalam database Django lokal
5. Mengimplementasikan dalam format HTML dengan membuat file mywatchlist.html kemudian membuat fungsi yang menerima parameter request dan mengembalikan render(request, "mywatchlist.html") di dalam file views.py.

     Mengimplementasikan dalam format XML dengan membuat fungsi yang menerima parameter request dan me-return HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml.Kemudian tambahkan kode berikut kedalam fungsi tersebut

        data = BarangWishlist.objects.all() 
        
    Mengimplementasikan dalam format JSON dengan membuat fungsi yang menerima parameter request dan me-return HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json". Kemudian tambahkan kode berikut kedalam fungsi tersebut

        data = BarangWishlist.objects.all()
6. Membuat routing sehingga data di atas dapat diakses melalui URL dengan cara menambahkan code berikut ke dalam file urls.py di dalam folder mywatchlist

        path('html/', show_mywatchlist, name='show_mywatchlist'),
        path('xml/',show_xml,name='show_xml'),
        path('json/',show_json name='show_json'),
7. Melakukan *deploy* dengan cara membuat aplikasi baru pada heroku. Kemudian masukkan API key dan nama aplikasi kedalam secret di github kemudian lakukan *deploy*


**SCREENSHOT POSTMAN**

http://localhost:8000/mywatchlist/html
![Postman_html](../asset/postman_html.png)

http://localhost:8000/mywatchlist/xml
![postman_xml](../asset/postman_xml.png)

http://localhost:8000/mywatchlist/json
![postman_json](../asset/postman_json.png)