import math

class CoolingModel:
    """
    Regolit Is Depolama Bloklar iin Souma Modeli.
    Stefan-Boltzmann Yasas kullanarak radyasyon kaybnn simlasyonu.
    """
    def __init__(self, mass_kg=10000, initial_temp_c=1000):
        self.mass = mass_kg
        self.temp_k = initial_temp_c + 273.15
        self.specific_heat = 800 # J/kg.K 
        self.sigma = 5.67e-8    # Stefan-Boltzmann sabiti
        self.emissivity = 0.3   # Yaltm sayesinde düürülmüş yayn gücü
        self.area = 1.0         # Maruz kalan yzey alan (m2)

    def simulate_hour(self):
        # Radyasyonla kaybolan g: P = epsilon * sigma * A * T^4
        power_lost_watts = self.emissivity * self.sigma * self.area * (self.temp_k**4)
        energy_lost_joules = power_lost_watts * 3600
        
        # Scaklk deiimi: dT = Q / (m * c)
        temp_drop = energy_lost_joules / (self.mass * self.specific_heat)
        self.temp_k -= temp_drop
        
        # Mutlak sfrn altna dümemesini sala
        self.temp_k = max(self.temp_k, 50) # Ay yzeyi yaklak 50K
        return self.temp_k - 273.15 # Celsius'a geri dn

if __name__ == "__main__":
    model = CoolingModel()
    print("--- Termal Souma Simlasyonu (24 Saat) ---")
    for hour in range(1, 25):
        temp_c = model.simulate_hour()
        if hour % 4 == 0:
            print(f"Saat {hour}: {temp_c:.1f}C")
