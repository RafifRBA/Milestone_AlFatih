Question:
- Apa itu servo Dynamixel?
- Apa yang membedakan servo Dynamixel dengan servo biasa?
- Apa kegunaan U2D2?

- Jelaskan apa itu URDF!
- Package apa saja yang diperlukan untuk memvisualisasikan URDF di RViz2?
- URDF bisa digunakan untuk simulasi di software apa saja?

Jawaban:
- Servo Dynamixel adalah servo yang canggih (smart actuator) buatan ROBOTIS yang dirancang khusus untuk aplikasi robotika. Dia tidak perlu connect ke pin pake PWM. Dynamixel memiliki kemampuan feedback posisi, kecepatan, torsi, suhu, dan tegangan secara real-time melalui komunikasi serial. Kita juga bisa mengatur posisi, kecepatan melalui python.

- Perbedaan Dynamixel dengan servo biasa:
  - Dynamixel menggunakan komunikasi serial (TTL/RS-485), sedangkan servo biasa menggunakan sinyal PWM
  - Dynamixel bisa dihubungkan berantai, servo biasa memerlukan koneksi terpisah ke controller
  - Dynamixel memiliki feedback lengkap (posisi, kecepatan, torsi, suhu), servo biasa hanya posisi atau tanpa feedback
  - Dynamixel bisa dikontrol dengan presisi tinggi dan memiliki berbagai mode operasi (position, velocity, torque control)
  - Dynamixel memiliki ID unik untuk setiap motor, memungkinkan kontrol banyak motor dalam satu bus

- U2D2 adalah converter dari USB ke TTL/RS-485 yang digunakan untuk menghubungkan servo Dynamixel ke komputer. U2D2 memungkinkan komunikasi antara PC dan servo Dynamixel untuk konfigurasi, programming, dan kontrol.

- URDF (Unified Robot Description Format) adalah format file XML yang digunakan untuk mendeskripsikan model robot secara lengkap, contohnya link, joint, visual geometry, collision geometry, dan properti inertial. URDF mendefinisikan struktur kinematik dan dinamik robot.

- Package yang diperlukan untuk visualisasi URDF di RViz2:
  - `robot_state_publisher` untuk mempublikasikan state robot ke TF
  - `joint_state_publisher` atau `joint_state_publisher_gui` untuk mengatur atau mempublikasikan nilai joint
  - `rviz2`  untuk visualisasi
  - `urdf`  untuk parsing file URDF
  - `xacro`

- Software simulasi yang mendukung URDF:
  - Gazebo
  - RViz/RViz2
  - PyBullet

  Software lain:
  - MuJoCo
  - CoppeliaSim
  - Webots
  - Isaac Sim (NVIDIA) 