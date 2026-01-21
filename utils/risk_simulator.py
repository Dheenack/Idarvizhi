import random

def generate_environmental_factors(disaster):
    """Simulated real-world disaster indicators"""

    data = {
        "temperature_c": round(random.uniform(24, 46), 1),
        "rainfall_mm": round(random.uniform(20, 420), 1),
        "humidity_pct": round(random.uniform(40, 98), 1),
        "wind_speed_kmph": round(random.uniform(5, 180), 1),
        "pressure_hpa": round(random.uniform(960, 1025), 1),
        "river_level_m": round(random.uniform(2, 12), 1),
        "soil_moisture_pct": round(random.uniform(20, 95), 1),
        "population_density_sqkm": random.randint(300, 15000),
        "hospital_access_index": round(random.uniform(0.3, 0.95), 2),
        "evacuation_access_index": round(random.uniform(0.4, 0.98), 2),
    }

    # Disaster-specific derived index
    if disaster.lower() == "flood":
        data["disaster_index"] = round(
            (data["rainfall_mm"] * 0.4 +
             data["river_level_m"] * 10 +
             data["soil_moisture_pct"] * 0.3), 2)

    elif disaster.lower() == "cyclone":
        data["disaster_index"] = round(
            (data["wind_speed_kmph"] * 0.6 +
             (1010 - data["pressure_hpa"]) * 2), 2)

    elif disaster.lower() == "heatwave":
        data["disaster_index"] = round(
            (data["temperature_c"] * 1.2 +
             data["humidity_pct"] * 0.4), 2)

    else:
        data["disaster_index"] = round(random.uniform(50, 120), 2)

    return data
