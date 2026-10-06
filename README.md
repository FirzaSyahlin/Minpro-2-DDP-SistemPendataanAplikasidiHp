# Minpro-2-DDP-SistemPendataanAplikasidiHp

Nama= Firza Aulia Syahlin
I NIM= 2609116107

1. Deskripsi Program

Program ini dibuat untuk mendata aplikasi yang ada di HP. Sebelum masuk ke menu, pengguna harus melakukan login terlebih dahulu. Program memiliki 2 jenis pengguna, yaitu admin dan user. Admin bisa menambah, melihat, mengubah, dan menghapus data aplikasi. Sedangkan user hanya bisa melihat data aplikasi. Program ini dibuat menggunakan Python dan menggunakan list serta dictionary untuk menyimpan data.

2. Flowchart
<img width="2399" height="3212" alt="Minpro 2 drawio" src="https://github.com/user-attachments/assets/f7162f0c-386a-4383-88ed-a865ed81780f" />
Alur program dimulai dari tampilan awal, kemudian pengguna melakukan login dengan memasukkan username dan password. Jika username atau password salah, maka program selesai.
Jika login berhasil, program akan melihat role pengguna.
Jika role admin, pengguna masuk ke menu admin. Admin bisa memilih tambah, lihat, ubah, hapus aplikasi, atau keluar.
Jika role user, pengguna masuk ke menu user. User hanya bisa melihat aplikasi atau keluar.

3. Dokumentasi program dan output

<img width="240" height="229" alt="Screenshot 2026-10-06 233406" src="https://github.com/user-attachments/assets/71f43fb0-62ba-4c13-b545-e1eeb55fff53" />
Bagian ini digunakan untuk menyimpan data akun dan data aplikasi. Terdapat dua akun, yaitu akun admin dan akun user. Data aplikasi disimpan dalam list "aplikasi" yang awalnya masih kosong.

<img width="413" height="365" alt="Screenshot 2026-10-06 231534" src="https://github.com/user-attachments/assets/7606a700-3ddf-4118-8524-49e9beaa1148" />
Function "login()" digunakan untuk melakukan proses login. Pengguna memasukkan username dan password. Program akan mengecek username yang dimasukkan. Jika username ditemukan, password akan diperiksa. Jika benar, program menampilkan pesan login berhasil, role pengguna, dan waktu login.

<img width="418" height="233" alt="Screenshot 2026-10-06 231547" src="https://github.com/user-attachments/assets/7749753b-7beb-46cb-b248-85479c3c3c47" />
Function ini digunakan untuk menambahkan nama aplikasi. Jika nama aplikasi tidak diisi, program menampilkan pesan bahwa nama aplikasi tidak boleh kosong. Jika diisi, data aplikasi akan dimasukkan ke dalam list "aplikasi".

<img width="365" height="154" alt="Screenshot 2026-10-06 231555" src="https://github.com/user-attachments/assets/9544f161-99d9-4bbb-a2fb-2499754d30e8" />
Function ini digunakan untuk melihat daftar aplikasi yang sudah dimasukkan. Jika belum ada data, program menampilkan pesan bahwa belum ada data aplikasi. Jika sudah ada, program menampilkan nomor dan nama aplikasi.

<img width="505" height="347" alt="Screenshot 2026-10-06 231607" src="https://github.com/user-attachments/assets/5025075d-dd47-4edc-8c01-38d97af87fe4" />
Function ini digunakan untuk mengubah nama aplikasi. Admin memilih nomor aplikasi yang ingin diubah, kemudian memasukkan nama aplikasi baru. Program juga mengecek apakah nomor yang dipilih tersedia.

<img width="520" height="252" alt="Screenshot 2026-10-06 231615" src="https://github.com/user-attachments/assets/24240ad2-b537-431f-9c91-ec25e47904aa" />
Function ini digunakan untuk menghapus aplikasi. Admin memilih nomor aplikasi yang ingin dihapus. Jika nomor tersedia, data aplikasi akan dihapus dari list menggunakan "pop()".

<img width="403" height="554" alt="Screenshot 2026-10-06 231851" src="https://github.com/user-attachments/assets/45f2c924-a228-4e07-86c9-55aad6561f38" />
Menu admin digunakan untuk mengelola data aplikasi. Admin memiliki lima pilihan, yaitu:

1. Tambah Aplikasi
2. Lihat Aplikasi
3. Ubah Aplikasi
4. Hapus Aplikasi
5. Keluar

Menu akan terus ditampilkan selama admin belum memilih menu keluar.

<img width="392" height="333" alt="Screenshot 2026-10-06 231907" src="https://github.com/user-attachments/assets/21d7729b-c0c7-4310-9714-a6e12ca5c085" />
Menu user memiliki dua pilihan, yaitu melihat aplikasi dan keluar. User tidak memiliki akses untuk menambah, mengubah, atau menghapus data aplikasi.

<img width="388" height="230" alt="Screenshot 2026-10-06 231938" src="https://github.com/user-attachments/assets/da492ee5-4d28-41ed-b38a-a4f779d2b091" />
Program utama menampilkan nama sistem dan memanggil function "login()". Setelah login berhasil, program akan mengecek role pengguna. Jika role "admin", program menjalankan "menu_admin()". Jika role "user", program menjalankan "menu_user()". Jika login gagal, program akan selesai.

<img width="383" height="871" alt="Screenshot 2026-10-06 233835" src="https://github.com/user-attachments/assets/5658391b-1597-459b-90b5-f628287dd53b" />
<img width="274" height="226" alt="Screenshot 2026-10-06 233845" src="https://github.com/user-attachments/assets/c261f465-bc0b-40b6-ad81-9359efb815fc" />
<img width="299" height="339" alt="Screenshot 2026-10-06 233931" src="https://github.com/user-attachments/assets/032a23ae-cc0a-432b-b1c2-a5283d8f6927" />

4. Nilai Tambah

Program ini memiliki beberapa tambahan, yaitu:

- Login dengan username dan password
- Pembagian role admin dan user
- Admin bisa melakukan tambah, lihat, ubah, dan hapus data
- Program menggunakan function agar kode lebih teratur
- Ada pengecekan jika nama aplikasi kosong
- Program menampilkan waktu saat berhasil login
