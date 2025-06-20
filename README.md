# [Miss_Dial 💫 — Telegram Number Info Bot](https://t.me/your_bot_username)

**Miss_Dial** is a simple and accurate Telegram bot that reveals essential information about any phone number you send it. Built using Python and the `phonenumbers` library, Miss_Dial tells you the country, region, timezone, local time, and whether it's day or night at that location.

---

## Features✨

- Validates and parses phone numbers with country codes
- Displays:
  -> 📞 Number
  
  -> 🌍 Country

  -> 📍 Region (if available)

  -> 🕒 Local time

  -> ⏱️ Timezone

  -> 🌞 Whether it’s Day or Night
- Clean and structured replies with intuitive emojis
---

## Setup Instructions

1. **Clone this repository** to your local machine.

```bash
git clone https://github.com/your-username/Miss_Dial.git
cd Miss_Dial
```
2. **Install** the required dependencies:

```bash
pip install python-telegram-bot==20.7 phonenumbers pytz pycountry python-dotenv
```
3. Create a **.env file** in the project root and add your Telegram bot token:
   
```bash
BOT_TOKEN=your_telegram_bot_token
```
4. Run the bot:

```bash
python main.py
```
Once the bot is running, open Telegram, search for your bot, and send a number like:

+919876543210
+442083661177
+16502530000

---

## How to Get Your Telegram Bot Token🔑
Use @BotFather on Telegram to create a bot and get your token.

---

## Author
Feel free to star⭐ the repo, open issues, or contribute!
Developed by @aayushirh.
