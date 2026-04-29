import requests
import json

base_url = "http://localhost:8000/api/v1"

try:
    collections = requests.get(f"{base_url}/collections").json()
    if not collections:
        print("❌ Ingen collections fundet i ChromaDB.")
    else:
        for col in collections:
            col_id = col['id']
            col_name = col['name']
            count = requests.get(f"{base_url}/collections/{col_id}/count").json()
            print(f"✅ Collection: '{col_name}' (ID: {col_id})")
            print(f"   Antal chunks: {count}")
            
            # Hent de første par stykker data
            data = requests.post(f"{base_url}/collections/{col_id}/get", 
                               json={"limit": 2}).json()
            if data['documents']:
                print(f"   Eksempel på indhold: {data['documents'][0][:100]}...")
except Exception as e:
    print(f"Fejl ved kontakt til ChromaDB: {e}")
