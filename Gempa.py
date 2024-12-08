class Gempa:
    # Konstruktor inisialisasi atribut dan skala
    def __init__(self, lokasi, skala):
        # Atribut
        self.lokasi = lokasi
        self.skala = skala

    # Method menentukan dampak skala gempa
    def dampak(self):
        # Statement / logika
        if self.skala < 2:
            print("Dampak Gempa: Tidak berasa")
        elif self.skala >= 2 and self.skala <= 4:
            print("Dampak Gempa: Bangunan Retak-Retak")
        elif self.skala > 4 and self.skala <= 6:
            print("Dampak Gempa: Bangunan Roboh")
        elif self.skala > 6:
            print("Dampak Gempa: Berpotensi Tsunami")

        # Menampilkan lokasi dan skala
        print(f"Lokasi Gempa: {self.lokasi}")
        print(f"Skala Gempa: {self.skala}")



          
    
        
