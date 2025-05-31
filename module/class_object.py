class Mobil():
    merk = None
    warna = None
    transmisi = None
    bahan_bakar = None

    def klakson(self):
        print("Pim..Pim")

    def klakson2(self):
        return "brum..brum"

    def autopilot(self):
        print(f"mode autopilot mobil {self.merk} on")

class Persegi:
  def __init__(self, sisi):
    self.sisi = sisi

  def hitung_keliling(self):
    return 4*self.sisi

mobil1 = Mobil()
mobil1.merk = "Toyota Agya"
mobil1.autopilot()
print(mobil1.klakson2())

psg1 = Persegi(4)
print(psg1.hitung_keliling())