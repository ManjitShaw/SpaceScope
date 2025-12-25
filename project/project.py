import requests
import os
from dotenv import load_dotenv
import datetime
import json

# ----------------------------
# SpaceScope Class
# ----------------------------
class SpaceScope:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("NASA_API_KEY")

    def fetch_nasa_asteroids(self):
        """Fetch top 5 near-Earth asteroids from NASA API and return entries"""
        today = datetime.date.today().strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&api_key={self.api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print("Error fetching data:", e)
            return []

        if not data or "near_earth_objects" not in data:
            print("Failed to fetch asteroid data. Try again later.")
            return []

        asteroids = data["near_earth_objects"][today][:5]  # first 5 only
        entries = []

        for asteroid in asteroids:
            entry = {
                "name": asteroid["name"],
                "diameter_km": float(asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]),
                "speed_kmh": float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]),
                "miss_distance_km": float(asteroid["close_approach_data"][0]["miss_distance"]["kilometers"])
            }

            print(
                f"\nAsteroid Name: {entry['name']}\n"
                f"Estimated Diameter (km): {entry['diameter_km']:.3f} km\n"
                f"Relative Speed (km/h): {entry['speed_kmh']:.0f} km/h\n"
                f"Miss Distance (km): {entry['miss_distance_km']/1_000_000:.2f} M km"
            )

            entries.append(entry)

        return entries

    def save_log(self, entries):
        """Save entries to JSON log"""
        if not entries:
            return

        log_data = {
            "category": "nasa_asteroids",
            "timestamp": str(datetime.datetime.now()),
            "asteroids": entries
        }

        try:
            with open("activity.json", "a") as f:
                json.dump(log_data, f, indent=2)
                f.write("\n")  # separate entries
        except Exception as e:
            print("Error saving log:", e)

# ----------------------------
# Wrapper top-level functions 
# ----------------------------

def fetch_asteroids():
    app = SpaceScope()
    return app.fetch_nasa_asteroids()

def save_asteroid_log(entries):
    app = SpaceScope()
    app.save_log(entries)

def get_top_asteroids():
    """Return asteroid entries without printing (for testing)"""
    app = SpaceScope()
    return app.fetch_nasa_asteroids()

# ----------------------------
# Main
# ----------------------------
def main():
    print("Welcome to SpaceScope!")

    while True:
        try:
            user_input = input("Press Enter to view today's NASA Near-Earth Asteroids: ")

            if user_input == "":
                entries = fetch_asteroids()
                save_asteroid_log(entries)
                break
            else:
                print("Please press only Enter. Try again.\n")

        except Exception:
            print("Unexpected error. Try again.")

if __name__ == "__main__":
    main()
