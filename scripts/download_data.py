import os
import urllib.request

def download_datasets():
    # Create the directory structure as per project requirements
    os.makedirs('data/raw', exist_ok=True)
    
    # Official UK Road Traffic Statistics URL
    url = "https://downloads.dft.gov.uk/road-traffic-statistics-data/traffic_major_roads_local_authority.csv"
    target_path = 'data/raw/Traffic_local.csv'
    
    print(f"📡 Attempting to fetch data from: {url}")
    
    # Adding a header to mimic a browser request
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(target_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"✅ Successfully downloaded to {target_path}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")
        print("💡 PhD Tip: If you are offline, manually ensure 'Traffic_local.csv' is in 'data/raw/'.")

if __name__ == "__main__":
    download_datasets()