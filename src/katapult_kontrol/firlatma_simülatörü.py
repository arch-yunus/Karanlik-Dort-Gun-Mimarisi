import argparse
import math

def calculate_physics(mass_kg, target_velocity_kms, accel_g=None):
    target_velocity_ms = target_velocity_kms * 1000
    kinetic_energy = 0.5 * mass_kg * (target_velocity_ms ** 2)
    
    print(f"--- Gelimi Ktle Frlatma Simlatr ---")
    print(f"Kargo Ktlesi: {mass_kg} kg")
    print(f"Hedef Hz: {target_velocity_kms} km/s")
    print(f"Gerekli Kinetik Enerji: {kinetic_energy / 1e6:.2f} MJ")
    
    if accel_g:
        accel_ms2 = accel_g * 9.81
        # L = v^2 / 2a
        rail_length = (target_velocity_ms ** 2) / (2 * accel_ms2)
        duration = target_velocity_ms / accel_ms2
        
        print(f"Ivmelenme: {accel_g} G ({accel_ms2:.2f} m/s^2)")
        print(f"Gereken Ray Uzunluu: {rail_length / 1000:.2f} km")
        print(f"Frlatma Sresi: {duration:.2f} saniye")
        
    return kinetic_energy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Mass Driver Simulation")
    parser.add_argument("--kargo_kg", type=float, default=100.0, help="Cargo mass in kg")
    parser.add_argument("--hedef_hiz_kms", type=float, default=1.7, help="Target velocity in km/s")
    parser.add_argument("--accel_g", type=float, help="Acceleration limit in Gs")
    
    args = parser.parse_args()
    calculate_physics(args.kargo_kg, args.hedef_hiz_kms, args.accel_g)
