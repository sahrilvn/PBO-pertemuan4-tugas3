class sepatu:
    def __init__(self, merk, warna, ukuran):
        self.merk = merk
        self.warna = warna
        self.ukuran = ukuran

    def printname(self):
        print(self.merk)
        print(self.warna)
        print(self.ukuran)

class running(sepatu):
     def __init__(self, merk, warna, ukuran):
         sepatu.__init__(self, merk, warna, ukuran)
         self.harga = "Rp. 200.000"

     def running(Self):
        print("Merk       : ", Self.merk)
        print("Warna      : ", Self.warna)
        print("Ukuran     : ", Self.ukuran)
        print("Harga      : ", Self.harga)


class casual(sepatu):
    def __init__(self, merk, warna, ukuran):
          sepatu.__init__(self, merk, warna, ukuran)
          self.harga = "Rp. 150.000"

    def casual(Self):
        print("Merk       : ", Self.merk)
        print("Warna      : ", Self.warna)
        print("Ukuran     : ", Self.ukuran)
        print("Harga      : ", Self.harga)

x = running("Adidas", "Merah", "40")
y = casual("Converse", "Biru", "41")

x.running()
y.casual()