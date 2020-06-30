from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):  # Tanda kurung dalam class merupakan turunan
    # dalam kasus ini Segitiga merupakan turunan dari kelas Bangun Ruang
    # __init__ adalah Konstruktor

    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return (f"Class Segitiga untuk menghitung luas dengan Alas : {self.alas} dan Tinggi : {self.tinggi}")

    def hitung_luas(self):
        return self.alas * self.tinggi / 2
