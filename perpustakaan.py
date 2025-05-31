import os
import datetime

# Data buku disimpan di memori
stock_data = [
    ["Harry Potter", "Jk Rowling", 20, 100000],
    ["Kalkulus", "I Wayan Suletra", 20, 80000],
    ["Program Komputer", "Yusuf Priyandari", 20, 100000],
    ["Security Analysis", "Benjamin", 20, 100000],
    ["Habis Gelap Terbitlah Terang", "Raden Ajeng Kartini", 20, 70000]
]

# Simpan log peminjaman dan pengembalian
log_pinjaman = {}
log_pengembalian = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    input("\nTekan tombol apa saja untuk kembali...")
    clear_screen()

def getDate():
    return str(datetime.datetime.now().date())

def getTime():
    return str(datetime.datetime.now().time())

def display_buku():
    print("\nDaftar Buku:")
    for i, (judul, pengarang, stok, harga) in enumerate(stock_data):
        print(f"{i+1}. {judul} oleh {pengarang} - Stok: {stok} - Harga: Rp{harga}")
    print()

def tambah_buku():
    judul = input("Judul = ")
    pengarang = input("Pengarang = ")
    stok = int(input("Stok = "))
    harga = int(input("Harga = Rp "))
    stock_data.append([judul, pengarang, stok, harga])
    print("✅ Buku berhasil ditambahkan.\n")

def pinjamkan_buku():
    nama = input("Masukkan nama lengkap peminjam: ").strip()
    display_buku()
    daftar_pinjaman = []
    total = 0
    while True:
        try:
            idx = int(input("Masukkan nomor buku yang ingin dipinjam: ")) - 1
            if stock_data[idx][2] > 0:
                stock_data[idx][2] -= 1
                daftar_pinjaman.append(idx)
                total += stock_data[idx][3]
                print(f"📚 '{stock_data[idx][0]}' berhasil dipinjam.")
            else:
                print("❌ Stok buku habis.")
        except (ValueError, IndexError):
            print("⚠️ Masukkan nomor yang valid.")

        lanjut = input("Ingin meminjam buku lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    if daftar_pinjaman:
        log_pinjaman[nama] = {
            "buku": daftar_pinjaman,
            "tanggal": getDate(),
            "waktu": getTime(),
            "total": total
        }
        print(f"\n✅ Peminjaman oleh {nama} berhasil disimpan.")
    else:
        print("⚠️ Tidak ada buku yang dipinjam.")

def kembalikan_buku():
    nama = input("Masukkan nama peminjam: ").strip()
    if nama not in log_pinjaman:
        print("❌ Tidak ditemukan data peminjaman atas nama tersebut.")
        return

    data = log_pinjaman[nama]
    daftar_buku = data["buku"]
    total = data["total"]

    print("\n📋 Buku yang dikembalikan:")
    for i, idx in enumerate(daftar_buku, start=1):
        print(f"{i}. {stock_data[idx][0]} (Rp{stock_data[idx][3]})")
        stock_data[idx][2] += 1  # Kembalikan stok

    terlambat = input("Apakah buku dikembalikan terlambat? (y/n): ").strip().lower()
    denda = 0
    if terlambat == 'y':
        hari = int(input("Berapa hari keterlambatan? "))
        denda = hari * 3000
        total += denda
        print(f"Denda keterlambatan: Rp{denda}")

    log_pengembalian[nama] = {
        "tanggal": getDate(),
        "waktu": getTime(),
        "total": total,
        "denda": denda
    }

    print(f"\n✅ Pengembalian oleh {nama} berhasil. Total pembayaran: Rp{total}")

def lihat_log():
    print("\n📁 Log Peminjaman:")
    if not log_pinjaman:
        print("Belum ada peminjaman.")
    for nama, info in log_pinjaman.items():
        print(f"- {nama} | {info['tanggal']} {info['waktu']} | Total: Rp{info['total']}")

    print("\n📁 Log Pengembalian:")
    if not log_pengembalian:
        print("Belum ada pengembalian.")
    for nama, info in log_pengembalian.items():
        print(f"- {nama} | {info['tanggal']} {info['waktu']} | Total Bayar: Rp{info['total']} (Denda: Rp{info['denda']})")

def menu_awal():
    while True:
        print("📚 Selamat Datang di Perpustakaan HMTI 📚")
        print("1. Tampilkan Daftar Buku")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Tambah Buku Baru")
        print("5. Lihat Log Peminjaman/Pengembalian")
        print("6. Keluar")
        try:
            pilihan = int(input("Pilih menu (1-6): "))
            clear_screen()
            if pilihan == 1:
                display_buku()
                kembali()
            elif pilihan == 2:
                pinjamkan_buku()
                kembali()
            elif pilihan == 3:
                kembalikan_buku()
                kembali()
            elif pilihan == 4:
                tambah_buku()
                kembali()
            elif pilihan == 5:
                lihat_log()
                kembali()
            elif pilihan == 6:
                print("👋 Terima kasih telah menggunakan sistem perpustakaan.")
                break
            else:
                print("⚠️ Pilihan hanya 1-6.")
        except ValueError:
            print("⚠️ Masukkan angka yang benar.")
            kembali()

# Jalankan program
menu_awal()
