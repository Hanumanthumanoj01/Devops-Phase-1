import requests
import time

# Replace this with your Render or Fly.io URL
URL = "https://devops-phase-1.onrender.com/"

while True:
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("✅ App is UP")
        else:
            print("⚠️ App returned status:", response.status_code)
    except Exception as e:
        print("❌ App is DOWN:", e)
    time.sleep(10)  # check every 10 seconds
