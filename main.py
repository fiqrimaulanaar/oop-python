from geometri.bangun_ruang import BangunRuang
from geometri.persegi_panjang import PersegiPanjang
from geometri.segitiga import Segitiga

p1 = PersegiPanjang(5, 2)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(4, 2)
print(s1.info())
print(s1.hitung_luas())

b1 = BangunRuang()
print(f"\n{b1.info()}")