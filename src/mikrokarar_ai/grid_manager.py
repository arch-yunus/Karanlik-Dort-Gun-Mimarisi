class GridManager:
    """
    Ay Gney Kutbu Mikroebeke Yneticisi.
    Gne, Batarya ve Termal Depolama (TES) arasndaki dengeyi ynetir.
    """
    def __init__(self, battery_capacity_kwh=1000, tes_capacity_kwh=5000):
        self.battery_capacity = battery_capacity_kwh
        self.tes_capacity = tes_capacity_kwh
        self.battery_soc = 0.8  # %80 arjla balar
        self.tes_temp = 1000    # 1000C ile balar
        
    def allocate_power(self, demand_kwh, is_darkness=False):
        print(f"--- ebeke Durumu ---")
        print(f"Batarya SOC: %{self.battery_soc*100:.1f}")
        print(f"TES Scaklk: {self.tes_temp}C")
        
        if is_darkness:
            print("(!) Karanlk Periyot: Enerji tasarrufu modu aktif.")
            # lnce TES'ten Stirling motoruyla enerji ekmeye al
            if self.tes_temp > 200:
                print("-> Enerji TES'ten (Stirling) salanyor.")
                self.tes_temp -= 5 # Basit bir azal
            else:
                print("-> TES yetersiz, bataryadan tketiliyor.")
                self.battery_soc -= (demand_kwh / self.battery_capacity)
        else:
            print("-> Gne enerjisi aktif. Sistem arj ediliyor.")
            self.battery_soc = min(1.0, self.battery_soc + 0.1)
            self.tes_temp = min(1000, self.tes_temp + 20)

if __name__ == "__main__":
    manager = GridManager()
    # Karanlk senaryosu simlasyonu
    for hour in range(5):
        manager.allocate_power(demand_kwh=50, is_darkness=True)
