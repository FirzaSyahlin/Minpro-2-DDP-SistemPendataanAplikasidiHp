from datetime import datetime

# Data akun
akun = {
    "firza": {
        "password": "zaa321",
        "role": "admin"
    },
    "aulia": {
        "password": "lia123",
        "role": "user"
    }
}

# Data aplikasi
aplikasi = []


# Function untuk login
def login():
    print("\n=== LOGIN ===")

    username = input("Username: ")
    password = input("Password: ")

    if username in akun:
        if password == akun[username]["password"]:
            print("Login berhasil.")
            print("Role:", akun[username]["role"])
            print("Waktu login:", datetime.now())

            return akun[username]["role"]
        else:
            print("Password salah.")
    else:
        print("Username tidak ditemukan.")

    return None


# Function untuk menambah aplikasi
def tambah_aplikasi():
    nama = input("Nama aplikasi: ")

    if nama == "":
        print("Nama aplikasi tidak boleh kosong.")
    else:
        data = {
            "nama": nama
        }

        aplikasi.append(data)
        print("Data aplikasi berhasil ditambahkan.")


# Function untuk melihat aplikasi
def lihat_aplikasi():
    if len(aplikasi) == 0:
        print("Belum ada data aplikasi.")
    else:
        print("\n=== DAFTAR APLIKASI ===")

        for i in range(len(aplikasi)):
            print(i + 1, aplikasi[i]["nama"])


# Function untuk mengubah aplikasi
def ubah_aplikasi():
    if len(aplikasi) == 0:
        print("Belum ada data aplikasi.")
    else:
        lihat_aplikasi()

        nomor = int(input("Nomor aplikasi yang ingin diubah: "))

        if nomor >= 1 and nomor <= len(aplikasi):
            nama_baru = input("Nama aplikasi baru: ")

            if nama_baru == "":
                print("Nama aplikasi tidak boleh kosong.")
            else:
                aplikasi[nomor - 1]["nama"] = nama_baru
                print("Data aplikasi berhasil diubah.")
        else:
            print("Nomor aplikasi tidak tersedia.")


# Function untuk menghapus aplikasi
def hapus_aplikasi():
    if len(aplikasi) == 0:
        print("Belum ada data aplikasi.")
    else:
        lihat_aplikasi()

        nomor = int(input("Nomor aplikasi yang ingin dihapus: "))

        if nomor >= 1 and nomor <= len(aplikasi):
            aplikasi.pop(nomor - 1)
            print("Data aplikasi berhasil dihapus.")
        else:
            print("Nomor aplikasi tidak tersedia.")


# Menu untuk admin
def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Aplikasi")
        print("2. Lihat Aplikasi")
        print("3. Ubah Aplikasi")
        print("4. Hapus Aplikasi")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_aplikasi()

        elif pilihan == "2":
            lihat_aplikasi()

        elif pilihan == "3":
            ubah_aplikasi()

        elif pilihan == "4":
            hapus_aplikasi()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak tersedia.")


# Menu untuk user
def menu_user():
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat Aplikasi")
        print("2. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_aplikasi()

        elif pilihan == "2":
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak tersedia.")


# Program utama
print("=== SISTEM PENDATAAN APLIKASI DI HP ===")

role = login()

if role == "admin":
    menu_admin()

elif role == "user":
    menu_user()

else:
    print("Program selesai.")