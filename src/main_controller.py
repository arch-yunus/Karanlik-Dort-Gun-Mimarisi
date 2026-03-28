from mikrokarar_ai.grid_manager import GridManager
from termal_simülatör.cooling_model import CoolingModel
from katapult_kontrol.firlatma_simülatörü import calculate_physics
from katapult_kontrol.magnet_timing import MagnetTiming

def run_mission_simulation():
    print("==================================================")
    print("   KARANLIK DÖRT GÜN - ENTEGRE MİSYON SİMÜLASYONU")
    print("==================================================")
    
    # 1. ebeke ve Enerji Durumu
    grid = GridManager()
    grid.allocate_power(demand_kwh=100, is_darkness=True)
    
    # 2. Termal Depo Analizi
    thermal = CoolingModel(mass_kg=50000)
    temp_after_24h = 0
    for _ in range(24):
        temp_after_24h = thermal.simulate_hour()
    print(f"-> 24 Saat Sonra TES Scakl: {temp_after_24h:.1f}C")
    
    # 3. Ktle Frlatma Operasyonu
    print("\n--- Frlatma Hazrlklar ---")
    calculate_physics(mass_kg=500, target_velocity_kms=1.7, accel_g=40)
    
    # 4. Bobin Kontrolü
    magnets = MagnetTiming(rail_length_m=4000)
    magnets.calculate_firing_sequence(mass_kg=500, target_v_ms=1700)
    
    print("\n==================================================")
    print("SİSTEM DURUMU: NOMİNAL | MİSYON BAŞARIYLA TAMAMLANDI")

if __name__ == "__main__":
    run_mission_simulation()
