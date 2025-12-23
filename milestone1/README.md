# Milestone_AlFatih
Kata mas dzul disuruh jawab ini:


- Jelaskan pin apa saja yang ada di Servo!
- ESP32 menggunakan baudrate 115200, jelaskan apa itu baudrate? Dan apakah di program python juga harus 115200?
- Jelaskan alur program yang telah dibuat!

1. Pin yang ada di servo ada 3 (CMIIW, gak sempet ngecek)
   
   VCC -> inputan 3,3V
   
   GND -> Ground
   
   SERVO_PIN -> pin untuk menggerakkan servo

3. Baudrate intinya adalah kecepatan transmisi data. Baudrate mencatat jumlah perubahan sinyal per detik dalam saluran komunikasi. Apakah di python juga harus 115200? Iya baudrate harus sama persis di kedua sisi agar kecepatan menerima dan mengirim datanya sama. Keduanya akan sinkron kalau sama. jika ada perbedaan sedikit saja, maka data yang ditangkap akan beda. 

4. Alur program:

   Jadi kita akan membuat kode arduino(.ino) nya terlebih dahulu.
   1. Setup servo pake attach
   2. Pada bagian loop kita akan mengecek apakah ada bytes yang disimpan di buffer oleh serial. kita menggunakan Serial.available() > 0. Jadi serial available ini mengembalikan jumlah bytes yang ada. Jika lebih dari 0 otomatis si buffer ada isinya.
   3. Kalau ada isinya kita lanjut ubah bytes ini jadi integer pake Serial.parseInt();
   4. Misal di buffer nyimpen "9" "0" "\n". Maka si parseInt akan ngubah bytes 9 dan 0 jadi integer 90. yang bukan angka nggak akan ikut diubah ke integer, dia akan tetap di buffer. Nah kenapa pake \n ? agar si parseInt ini nggak timeout karena parseInt hanya berhenti setelah tidak ada angka di buffer. Alih-alih kita nunggu parseInt mending langsung stop aja pake non angka \n atau enter.
   5. Nah karena masih ada satu karakter nyangkut di buffer ("\n"), maka kita buat looping. Selama di buffer Serial.available() nya masih lebih dari 0, maka kita buang. Cara buangnya pake Serial.read(). Serial.read() ini cuman baca 1 bytes dari buffer lalu dihapus makanya butuh looping jaga-jaga kalau karakter yang dibuffer nyisa lebih dari satu.
   6. Setelah itu kita check, kalau inputan user 0-180 servo akan gerak mengikuti sudut tersebut menggunakan servo.write(angle).

   Lanjut yang python(.py) nya
   1. setup port, baudrate, dan serial nya
   2. bikin fungsi buat handle sudut. Jadi kita bakal ubah degree yang dimasukin user ditambah "\n" buat handle parseInt nya tadi. Kalau udah, kita gunakan serial.write() untuk mengirimnya ke mikon. Nah Serial ini tadi kan bacanya bytes. maka sebelum dikirim ke mikon kita ubah dulu string degree+\n nya jadi bytes pake .encode().
  

   Jadi intinya nanti user masukin degree sesuai keinginan dengan range 0-180. Kalau udah, hasil ketikan user ditambah "\n" di akhir. Setelah ditambah "\n", string akan diencode menjadi bytes dan dikirim ke mikon. Mikon akan menerima data itu, kemudian mendecode menjadi integer. Setelah di decode jadi integer, mikon akan menggerakkan servo sesuai dengan integer tadi.


   

   
