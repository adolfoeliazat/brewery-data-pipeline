import json

def store_raw_data(data, file_path="/app/bronze/raw_breweries.json"):
    with open(file_path, 'w') as f:
        json.dump(data, f)
    print(f"Raw data saved at {file_path}")
    