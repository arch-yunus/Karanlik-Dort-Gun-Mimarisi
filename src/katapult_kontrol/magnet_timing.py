import time

class MagnetTiming:
    """
    Elektromanyetik bobinlerin (solenoid) sral atefleme kontrolü.
    Kargonun anlk konumu ve hzna göre akm zamanlamasn yönetir.
    """
    def __init__(self, rail_length_m, num_coils=100):
        self.rail_length = rail_length_m
        self.num_coils = num_coils
        self.coil_spacing = rail_length_m / num_coils
        
    def calculate_firing_sequence(self, mass_kg, target_v_ms):
        accel = (target_v_ms**2) / (2 * self.rail_length)
        print(f"--- Bobin Atefleme Zamanlamas Planlanıyor ---")
        print(f"Toplam Bobin: {self.num_coils} | Bobin Aral: {self.coil_spacing:.2f} m")
        
        timings = []
        for i in range(1, self.num_coils + 1):
            distance = i * self.coil_spacing
            # d = 0.5 * a * t^2 => t = sqrt(2d/a)
            t_firing = (2 * distance / accel)**0.5
            timings.append(t_firing)
            
            if i % 20 == 0:
                print(f"Bobin {i:03d}: T + {t_firing:.6f}s | Hz: {(accel * t_firing):.1f} m/s")
                
        return timings

if __name__ == "__main__":
    controller = MagnetTiming(rail_length_m=3000)
    controller.calculate_firing_sequence(mass_kg=250, target_v_ms=1700)
