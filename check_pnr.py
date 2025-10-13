import os
import requests
from bs4 import BeautifulSoup

PNR = os.getenv("PNR_NUMBER")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
URL = f"https://www.railyatri.in/pnr-status/{PNR}"

def fetch_current_status():
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(URL, headers=headers)
    if resp.status_code != 200:
        print(f"❌ Failed to fetch page: {resp.status_code}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    status_tags = soup.find_all("p", class_="pnr-bold-txt statusType")
    if len(status_tags) >= 2:
        current_status = status_tags[1].text.strip()
        print(f"🚆 Current status for PNR {PNR}: {current_status}")
        return current_status
    else:
        print("❌ Unable to locate current status on page.")
        return None

def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, data=payload)
        print("✅ Message sent to Telegram")
    except Exception as e:
        print(f"⚠️ Telegram send error: {e}")

if __name__ == "__main__":
    status = fetch_current_status()
    if status:
        send_to_telegram(f"🚆 PNR {PNR} current status: {status}")
