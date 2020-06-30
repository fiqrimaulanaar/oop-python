from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):  # Tanda kurung dalam class merupakan turunan
    # dalam kasus ini Segitiga merupakan turunan dari kelas Bangun Ruang
    # __init__ adalah Konstruktor

    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return (f"Class persegi panjang untuk menghitung luas dengan panjang : {self.p} dan lebar : {self.l}")

    def hitung_luas(self):
        return self.p * self.l
