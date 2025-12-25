Question:

Python:
* Apa itu virtual environment dan kenapa perlu virtual env?
* Jelaskan apa itu package!

ROS2:
* Jelaskan apa itu Node, Topic, dan Service!
* Apa keunggulan ROS2?

Izin menjawab:
1. venv adalah suatu environtment terpisah dari environtment python yang telah ada dari sistem. Kita perlu venv agar mempermudah dalam pengerjaan project. Misal kita butuh versi python yang lebih tua dari python sistem. Jadinya tidak ada bentrok satu sama lain. Selain itu venv ini bisa diubah ke requirements.txt (hanya berupa text). Ini mempermudah kalau kita mau backup atau mau ngasih env kita ke orang lain.

2. Package adalah cara mengorganisir kode python. File Python (.py) ibarat selembar kertas berisi catatan (kode), maka Package adalah sebuah Map Folder yang membungkus kumpulan kertas-kertas tersebut agar rapi. Di folder packagenya harus ada file bernama __init__.py agar ke detect ini adalah suatu package.

3. Node, Topic, dan Service.
    - Node = program-program yang menjalankan tugas berbeda-beda(misal baca sensor, gerakin servo)
    - Topic = Sang Pengedar. Jadi topic digunain sebagai jalur datang dan keluarnya data. Misal Node A publish data sensor ke topic, lalu Node B bisa subscribe topic dan menerima semua data sensor yang dikirim Node A. Topic komunikasinya async jadi publiser kirim terus tanpa peduli ada subscriber atau tidak. Begitu pun subscriber.
    - Service = Mirip kaya topic tapi dia by-request. Jadi Node A harus req dulu. Si penerima misal Node B,  bakal memproses terlebih dahulu lalu ngirim response dari hasil request. Service komunikasinya sync jadi client harus nunggu response sebelum lanjut.

4. Keunggulan ROS2:
    - program dibuat sbg node node terpisah, ini memudahkan debugging
    - Banyak package siap pakai jadi nggak usah bikin dari scratch
    - node node bisa berkomunikasi satu sama lain secara bersamaan hampir real time, bukan sequential
    - mendukung bahasa c++ dan python
    - open source dan gratis :)
    
