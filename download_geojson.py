import requests

url = "https://raw.githubusercontent.com/datameet/maps/master/States/india_states.geojson"
file_name = "india_states.geojson"

response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.text)
    print("✅ india_states.geojson saved successfully")
else:
    print("❌ Failed to download GeoJSON")
