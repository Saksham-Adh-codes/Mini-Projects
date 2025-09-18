import requests
import json
from datetime import date

url = "https://www.nrb.org.np/api/forex/v1/rates"
parameters = {
    "page": 1,
    "per_page": 10, 
    "from": date.today().strftime("%Y-%m-%d"),  
    "to": "2025-09-18" 
}

resp = requests.get(url, params=parameters)
data = resp.json()
print(json.dumps(data, indent=2))