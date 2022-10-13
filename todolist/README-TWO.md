 ## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming melakukan eksekusi secara berurutan, user harus menunggu suatu program selesai dijalankan baru dapat menjalankan program lain. Sedangkan, Asynchronous programming membuat user bisa menjalankan program lain selagi suatu program belum selesai dijalankan, sehingga user tidak perlu menunggu program sebelumnya selesai.

 ## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
 Event-driven adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya. Contoh penerapan Event-Driven Programming pada penerapan tugas ini adalah ketika kita menambahkan task baru melalui tombol add task (yang memnunculkan modal). Setelah kita mengisi form add task dan menekan tombol add. maka data yang kita isi langsung ditampilkan di halaman todolist tanpa melakukan reload. 

 ## Jelaskan penerapan asynchronous programming pada AJAX. 
 AJAX atau Asynchronous JavaScript and XML adalah teknik yang digunakan untuk membuat website yang dinamis, sehingga website mampu mengupdate dan menampilkan data baru dari server tanpa perlu melakukan reload. AJAX bekerja secara asynchronous untuk berkomunikasi dengan server. Proses pertukaran informasi dilakukan di background. Oleh karena itu, saat AJAX JavaScript dan XML bekerja, halaman dapat tetap diakses oleh pengunjung website. Cara kerja AJAX yaitu sebagai berikut. Browser akan memanggil AJAX javascript untuk mengaktifkan XMLHttpRequest dan mengirimkan HTTP Request ke server. XMLHttpRequest dibuat untuk proses pertukaran data di server secara asinkron.Server menerima, memproses, dan mengirimkan data kembali ke browser.  Browser menerima data tersebut dan langsung ditampilkan di halaman website, tanpa perlu reload atau membuat halaman baru. 

 ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 AJAX GET
 1. Membuat view baru yaitu get_todolist_json untuk mengembalikan seluruh data task dalam bentuk JSON.
 2. Menambahkan path /todolist/json yang mengarah ke view get_todolist_json
 3. Menambahkan script pada todolist.html untuk melakukan pengambilan task menggunakan AJAX GET.

 AJAX POST
 1. Mmmbuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
 2. membuat view baru yaitu add untuk menambahkan task baru ke dalam database.
 3. manambahkan path /todolist/add yang mengarah ke view add.
 4. Menghubungkan form yang telah dibuat di dalam modal ke path /todolist/add
