import argparse
import math

def calculate_physics(mass_kg, target_velocity_kms):
    target_velocity_ms = target_velocity_kms * 1000
    kinetic_energy = 0.5 * mass_kg * (target_velocity_ms ** 2)
    print(f"--- Ktle Frlatma Simlatr ---")
    print(f"Kargo Ktlesi: {mass_kg} kg")
    print(f"Hedef Hz: {target_velocity_kms} km/s")
    print(f"Gerekli Kinetik Enerji: {kinetic_energy / 1e6:.2f} MJ")
    return kinetic_energy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mass Driver Simulation")
    parser.add_argument("--kargo_kg", type=float, default=100.0, help="Cargo mass in kg")
    parser.add_argument("--hedef_hiz_kms", type=float, default=1.7, help="Target velocity in km/s")
    
    args = parser.parse_args()
    calculate_physics(args.kargo_kg, args.hedef_hiz_kms)
