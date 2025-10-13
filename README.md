
# 🚆 ConfirmTkt Train Availability Checker (GitHub Actions + Telegram Alerts)

This project automatically checks **train seat availability** using the ConfirmTkt API and sends a **Telegram alert** when seats become available.

It runs on a **GitHub Actions runner** every hour — fully automated, no manual setup required.

---

## 🧩 Features
- Checks ConfirmTkt API for live availability.  
- Focuses on a specific journey date (e.g., `31-10-2025`).  
- Sends instant alerts to your Telegram via a bot.  
- Uses GitHub Actions to run every 1 hour (adjustable).  
- Secure: all tokens and keys are stored in **GitHub Secrets**.

---

## 🛠️ Setup Instructions

### 1. Fork or Clone This Repository
```bash
git clone https://github.com/<your-username>/confirmtkt-checker.git
cd confirmtkt-checker


### 2. Create a Telegram Bot

1. Open Telegram and search for `@BotFather`.
2. Run `/newbot` → follow prompts → you’ll receive a **Bot Token** like:

   ```
   123456789:ABCDefghIJKlmnoPQRstuVWxyz
   ```
3. Send a message to your new bot (e.g., “hi”).
4. Visit `https://api.telegram.org/bot<your_token>/getUpdates`
   and note your **chat_id** from the response.

---

### 3. Add GitHub Secrets

Go to
**Repo → Settings → Secrets and variables → Actions → New repository secret**

Add the following secrets (taken from your ConfirmTkt request and Telegram bot):

| Secret Name        | Description                       | Example                                                            |
| ------------------ | --------------------------------- | ------------------------------------------------------------------ |
| `CT_TOKEN`         | ConfirmTkt API token              | `AF5E7DA97C26586C1463ED2D514DFB20A6F22419C74C0B1748F16299F7283F9C` |
| `CT_USERKEY`       | ConfirmTkt user key               | `D34D3D797FE9BD367F64A4FF40F78D890391F7F9F15FB8F30993367B23D923AB` |
| `CT_DEVICEID`      | Device ID                         | `1533ef5b-e513-420d-9eaf-29dc42c69116`                             |
| `TELEGRAM_TOKEN`   | Telegram bot token from BotFather | `123456789:ABCDefghIJKlmnoPQRstuVWxyz`                             |
| `TELEGRAM_CHAT_ID` | Your Telegram chat ID             | `123456789`                                                        |

---

## 📜 Files Overview

| File                                 | Description                                                        |
| ------------------------------------ | ------------------------------------------------------------------ |
| `check_tickets.py`                   | Python script that checks ConfirmTkt API and sends Telegram alerts |
| `.github/workflows/ticket-check.yml` | GitHub Actions workflow (runs every 1 hour)                        |
| `README.md`                          | Documentation (this file)                                          |

---

## ⚙️ How It Works

1. Every hour, GitHub Actions runs `check_tickets.py`.
2. The script sends a POST request to ConfirmTkt API:

   ```
   /api/v1/availability/fetchAvailability?trainNo=06555&travelClass=3A&quota=GN&sourceStationCode=KJM&destinationStationCode=CGY&dateOfJourney=31-10-2025
   ```
3. It parses the response for:

   ```json
   {
     "availablityDate": "31-10-2025",
     "availablityStatus": "AVAILABLE-0578"
   }
   ```
4. If the status contains `"AVAILABLE"`, a Telegram alert is sent instantly.

---

## 🧾 Example Telegram Alert

```
🚆 Train 06555 (KJM → CGY)
Date: 31-10-2025
Status: AVAILABLE-0578
Checked: 2025-10-04 21:30:00
```

---

## 🕒 Scheduling

The job runs automatically every 1 hour.
You can change this frequency in `.github/workflows/ticket-check.yml`:

```yaml
on:
  schedule:
    - cron: "0 */1 * * *"  # every 1 hour
```

**Examples:**

* Every 6 hours → `0 */6 * * *`
* Every 30 minutes → `*/30 * * * *`

---

## 🧰 Requirements

* GitHub account (Free tier sufficient)
* Telegram bot + chat ID
* Python 3.11+ (GitHub handles automatically)

---

## 🛡️ Security

* All sensitive keys are stored in **GitHub Secrets**.
* The script is read-only (no booking actions).
* Safe to run in public or private repositories.

---

## 💡 Notes

* ConfirmTkt is a private API — frequent polling may be rate-limited.
* Use the script responsibly and for personal automation only.
* Works best for monitoring high-demand trains during festive seasons.

---

## 👨‍💻 Author

Developed by [Srinivasan](https://github.com/srinivasans13)
Bringing automation to your travel planning ⚡

---

## 🧾 License

Released under the **MIT License**.
Feel free to fork, modify, and enhance.

