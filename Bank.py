class Bank:
    # Variabel kelas
    BANK = "Bank Dunia"
    jmlNasabah = 0

    # Konstruktor untuk inisialisasi data nasabah
    def __init__(self, nomor, nama, saldo):
        self.nomor = nomor
        self.nama = nama
        self.saldo = saldo
        Bank.jmlNasabah += 1  # Menambah jumlah nasabah setiap kali objek dibuat

    # Fungsi untuk menabung
    def nabung(self, jumlah):
        self.saldo += jumlah
        print(f"{self.nama} menabung sebesar {jumlah}. Saldo sekarang: {self.saldo}.")

    # Fungsi untuk menarik uang
    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print(f"{self.nama} gagal menarik uang. Saldo tidak mencukupi.")
        else:
            self.saldo -= jumlah
            print(f"{self.nama} menarik sebesar {jumlah}. Saldo sekarang: {self.saldo}.")

    # Fungsi untuk mencetak informasi nasabah
    def cetak(self):
        print(f"Nomor: {self.nomor}, Nama: {self.nama}, Saldo: {self.saldo}")
