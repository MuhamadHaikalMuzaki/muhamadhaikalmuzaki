# Mengimpor semua dari file Bank
from Bank import *

# Ciptakan objek nasabah
gigi = Bank('001', 'Buffon', 5000000)
cr7 = Bank('007', 'Ronaldo', 7000000)
leo = Bank('010', 'Messi', 8000000)
salah = Bank('011', 'Mohammad Salah', 11000000)

# Gunakan member class
gigi.nabung(2000000)
leo.nabung(1000000)
cr7.tarik(2000000)
leo.tarik(6000000)

# Cetak informasi bank dan nasabah
print(Bank.BANK, "\n==========================")
gigi.cetak()
cr7.cetak()
leo.cetak()
salah.cetak()
print(f"Jumlah Nasabah: {Bank.jmlNasabah} orang")
