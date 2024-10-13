from prettytable import PrettyTable
# Daftar username dan password yang valid menggunakan dictionary
users = {
    'user1': 'user1123',
    'user2': 'user2123',
    'admin': 'admin123'
}

def login():
    print("=== Menu Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
   # Mengecek apakah username dan password valid
    if username in users and users[username] == password:
        if username == 'admin':
            return 1  # Jika username 'admin', return 1
        else:
            return 2  # Jika user biasa, return 2
    else:
        return 3  # Jika username atau password salah, return 3

# Data akan disimpan dalam list dictionary
kamus =	{
  "nama_brg": "Udang",
  "harga_brg": 2000
 }
data_list = [kamus]

kamus =	{
  "nama_brg": "Kerang",
  "harga_brg": 5000
 }
data_list.append(kamus)
kamus =	{
  "nama_brg": "Kepiting",
  "harga_brg": 7000
 }
data_list.append(kamus)
kamus =	{
  "nama_brg": "Ikan Bandeng",
  "harga_brg": 6000
 }
data_list.append(kamus)

# Fungsi untuk menambahkan data (Create)
def create_data(nama_brg, harga_brg):
    try:
        # Mengonversi harga_brg menjadi integer
        harga_brg = int(harga_brg)
        # Membuat dictionary data barang
        data = {'nama_brg': nama_brg, 'harga_brg': harga_brg}
        # Menambahkan data ke dalam data_list
        data_list.append(data)
        print(f"Data {nama_brg} berhasil ditambahkan!")
    except ValueError:
        # Menampilkan pesan jika harga_brg tidak bisa dikonversi menjadi integer
        print("Harga harus berupa angka.")

# Fungsi untuk menampilkan data (Read)
def read_data():
    if len(data_list) == 0:
        print("Tidak ada data yang tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Barang", "Harga/ons"]
        for i, data in enumerate(data_list, 1):
            table.add_row([i, data['nama_brg'], data['harga_brg']])
        print(table)

# Fungsi untuk mengubah data (Update)
def update_data(index, nama_brg=None, harga_brg=None):
    if 0 <= index < len(data_list):
        if nama_brg:
            data_list[index]['nama_brg'] = nama_brg
        if harga_brg:
            data_list[index]['harga_brg'] = harga_brg
        print(f"Data pada nomor {index + 1} berhasil diubah!")
    else:
        print("Indeks tidak valid!")

# Fungsi untuk menghapus data (Delete)
def delete_data(index):
    if 0 <= index < len(data_list):
        deleted_data = data_list.pop(index)
        print(f"Data {deleted_data['nama_brg']} berhasil dihapus!")
    else:
        print("Indeks tidak valid!")

    

# Program Utama
# Menjalankan fungsi login
print("SELAMAT DATANG DI GUDANG MAKANAN")
login_result = login()
while True:
    

    if login_result == 3:
        print("Username atau password salah.")
        login_result = login()
       # break  # Menghentikan perulangan jika login gagal
    elif login_result == 1: #rule admin
        print("Selamat datang, ADMIN!")
        while True:
            print("\n=== Menu CRUD Untuk Admin (Rule 1) ===")
            print("1. Tambah Data")
            print("2. Lihat Data")
            print("3. Ubah Data")
            print("4. Hapus Data")
            print("5. Login")
            print("6. Keluar")
            pilihan = input("Pilih opsi: ")
        
            if pilihan == '1':
                nama = input("Masukkan Nama Barang: ")
                harga = input("Masukkan Harga Barang/Ons (Rp): ")
                create_data(nama, harga)
                  
            elif pilihan == '2':
                read_data()
            
            elif pilihan == '3':
                read_data()
                indeks = int(input("Masukkan nomor data yang ingin diubah: ")) - 1
                nama_baru = input("Masukkan barang baru (kosongkan jika tidak diubah): ")
                harga_baru = input("Masukkan harga baru (kosongkan jika tidak diubah): ")
                update_data(indeks, nama_brg=nama_baru if nama_baru else None, harga_brg=harga_baru if harga_baru else None)
            
            elif pilihan == '4':
                read_data()
                indeks = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
                delete_data(indeks)
            
            elif pilihan == '5':
                login_result = login()
                break

            elif pilihan == '6':
                print("Program selesai.")
                exit()
        
        
            else:
                print("Pilihan tidak valid, coba lagi.")
                break
    else: #rule pembelian
        print("Selamat datang, USER!")
        while True:
            print("\n=== Menu Penjualan (Rule 2) ===")
            print("1. Lihat Data")
            print("2. Penjualan")
            print("3. Login")
            print("4. Keluar")
            
            
            pilihan = input("Pilih opsi: ")
            
            if pilihan == '1':
                read_data()
            elif pilihan =='2':
                read_data()
                total = 0
               # daftarbrg= [] # membuat list barang penjualan
                tabel= PrettyTable()  # Membuat PrettyTable
                tabel.field_names = ["Nama Barang", "Harga/Ons (Rp)", "Berat (Ons)", "Total (Rp)"]  # Menambahkan header tabel
                while True:
                    try:
                        # Meminta input indeks nomor barang, dikurangi 1 untuk indeks array
                        indeks = int(input("Masukkan nomor barang yang dibeli : ")) - 1
                        
                        # Memastikan indeks valid
                        if indeks < 0 or indeks >= len(data_list):
                            print("Nomor barang tidak valid. Coba lagi.")
                            continue
                        
                        nama_barang = data_list[indeks]['nama_brg']
                        harga_barang = data_list[indeks]['harga_brg']
                        
                        # Menampilkan nama dan harga barang yang dipilih
                        print(f"Nama Barang : {nama_barang}")
                        print(f"Harga/Ons : Rp {harga_barang}")
                        
                        # Meminta jumlah barang yang dibeli
                        jumlah = float(input("Berat Barang (Ons) : "))
                        
                        # Menghitung total harga
                        total_per_barang = harga_barang * jumlah
                        total += total_per_barang

                        # Menambahkan baris ke dalam tabel
                        tabel.add_row([nama_barang, f"Rp {harga_barang}", jumlah, f"Rp {total_per_barang}"])
                        # Menampilkan tabel hasil penjualan
                        print(tabel)
                        
                        # Menanyakan apakah ingin melanjutkan atau tidak
                        x = input("Lanjut Penjualan ? (y/n): ").lower()
                        
                        # Jika pengguna memilih tidak, keluar dari loop
                        if x != 'y':
                            break
                    except (ValueError, IndexError):
                        print("Input tidak valid. Silakan coba lagi.")

                 

                # Menampilkan total keseluruhan
                print(f"Total keseluruhan: Rp {total}")

                
            elif pilihan == '3':
                login_result = login()
                break
                
            elif pilihan == '4':
                print("Program selesai.")
                exit()
            
            else:
                print("Pilihan tidak valid, coba lagi.")
                break

   
    

