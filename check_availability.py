import os
import requests

# --- Config ---
URL = "https://cttrainsapi.confirmtkt.com/api/v1/availability/fetchAvailability"
params = {
    "trainNo": "06555",
    "travelClass": "3A",
    "quota": "GN",
    "sourceStationCode": "KJM",
    "destinationStationCode": "CGY",
    "dateOfJourney": "31-10-2025",
    "enableTG": "true",
    "tGPlan": "CTG-A9",
    "showTGPrediction": "false",
    "tgColor": "DEFAULT",
    "showPredictionGlobal": "true",
    "showNewMealOptions": "true"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Clientid": "ct-web",
    "Ct-Token": os.getenv("CT_TOKEN"),
    "Ct-Userkey": os.getenv("CT_USERKEY"),
    "Apikey": os.getenv("CT_APIKEY"),
}

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        resp = requests.post(url, json=payload, timeout=10)
        #print(resp.status_code, resp.text)
        resp.raise_for_status()
        result = resp.json()
        if not result.get("ok", False):
            print("Telegram API returned error:", result.get("error_code"), result.get("description"))
    except Exception as e:
        print("Exception sending Telegram message:", e)


def main():
    response = requests.post(URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    status = None
    for item in data["data"]["avlDayList"]:
        if item["availablityDate"] == "31-10-2025":
            status = item["availablityStatus"]
            break

    if status:
        message = f"🚆 Train 06555 (3A) availability for 31-10-2025: {status}"
        print(message)
        send_telegram_message(message)
    else:
        send_telegram_message("No availability info found for 31-10-2025.")


if __name__ == "__main__":
    main()
